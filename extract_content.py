#!/usr/bin/env python3
import json
import sys

def extract_json_content(filename, content_key):
    """Extract all content from a potentially malformed JSON file"""
    all_content = []
    
    with open(filename, 'r') as f:
        content = f.read()
    
    # First, try to extract the initial {content_key: [...]} object
    try:
        # Find the first complete object
        depth = 0
        end_pos = 0
        for i, char in enumerate(content):
            if char == '{':
                depth += 1
            elif char == '}':
                depth -= 1
                if depth == 0:
                    end_pos = i + 1
                    break
        
        first_obj = json.loads(content[:end_pos])
        if content_key in first_obj:
            all_content.extend(first_obj[content_key])
            print(f"Extracted {len(first_obj[content_key])} from first object", file=sys.stderr)
        
        # Now parse remaining individual objects
        remaining = content[end_pos:].strip()
        if remaining.startswith(','):
            remaining = remaining[1:].strip()
        
        # Split by pattern: }\n    , and try to parse each
        parts = []
        current = ""
        depth = 0
        
        for char in remaining:
            if char == '{':
                depth += 1
            elif char == '}':
                depth -= 1
            
            current += char
            
            if depth == 0 and current.strip() and current.strip() != ',':
                clean = current.strip().rstrip(',').strip()
                if clean:
                    parts.append(clean)
                current = ""
        
        print(f"Found {len(parts)} additional parts", file=sys.stderr)
        
        for i, part in enumerate(parts):
            try:
                obj = json.loads(part)
                if isinstance(obj, dict) and 'section_id' in obj:
                    all_content.append(obj)
                elif isinstance(obj, list):
                    all_content.extend(obj)
            except json.JSONDecodeError as e:
                print(f"Skipping part {i}: {str(e)[:50]}", file=sys.stderr)
    
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
    
    return all_content

# Extract exercises
exercises = extract_json_content('sample_lab_content.json', 'exercises')
print(f"Total exercises extracted: {len(exercises)}", file=sys.stderr)

# Save to file
with open('exercises_clean.json', 'w') as f:
    json.dump(exercises, f, indent=2)

print(f"Saved {len(exercises)} exercises to exercises_clean.json", file=sys.stderr)

# Do the same for quizzes
quizzes = extract_json_content('sample_quiz_questions_1.json', 'quiz_questions')
print(f"Total quizzes extracted: {len(quizzes)}", file=sys.stderr)

with open('quizzes_clean.json', 'w') as f:
    json.dump(quizzes, f, indent=2)

print(f"Saved {len(quizzes)} quizzes to quizzes_clean.json", file=sys.stderr)

print("SUCCESS")
