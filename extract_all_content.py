#!/usr/bin/env python3
import json
import re

def extract_all_exercises(filename):
    """Extract ALL exercise objects from file, regardless of structure"""
    with open(filename, 'r') as f:
        content = f.read()
    
    all_exercises = []
    
    # Method 1: Find all exercise objects using regex
    # Pattern: {"section_id": N, "exercise_id": "...", ...}
    pattern = r'(\{\s*"section_id"\s*:\s*\d+\s*,\s*"exercise_id"\s*:.*?\n\s*\})'
    
    # Find matches with proper nesting
    in_object = False
    brace_count = 0
    current_obj = ""
    
    for char in content:
        if char == '{':
            if brace_count == 0:
                current_obj = ""
            brace_count += 1
            current_obj += char
        elif char == '}':
            current_obj += char
            brace_count -= 1
            if brace_count == 0 and current_obj.strip():
                # Try to parse as exercise
                try:
                    obj = json.loads(current_obj.strip())
                    if isinstance(obj, dict) and 'section_id' in obj and 'exercise_id' in obj:
                        all_exercises.append(obj)
                except:
                    pass
                current_obj = ""
        elif brace_count > 0:
            current_obj += char
    
    return all_exercises

def extract_all_quizzes(filename):
    """Extract ALL quiz objects from file"""
    with open(filename, 'r') as f:
        content = f.read()
    
    all_quizzes = []
    
    in_object = False
    brace_count = 0
    current_obj = ""
    
    for char in content:
        if char == '{':
            if brace_count == 0:
                current_obj = ""
            brace_count += 1
            current_obj += char
        elif char == '}':
            current_obj += char
            brace_count -= 1
            if brace_count == 0 and current_obj.strip():
                # Try to parse as quiz
                try:
                    obj = json.loads(current_obj.strip())
                    if isinstance(obj, dict) and 'section_id' in obj and 'question' in obj:
                        all_quizzes.append(obj)
                except:
                    pass
                current_obj = ""
        elif brace_count > 0:
            current_obj += char
    
    return all_quizzes

# Extract all exercises
print("Extracting exercises...")
exercises = extract_all_exercises('sample_lab_content.json')
print(f"Found {len(exercises)} exercises")

# Count by section
section_counts = {}
for ex in exercises:
    sid = ex['section_id']
    section_counts[sid] = section_counts.get(sid, 0) + 1

print("Exercises by section:")
for sid in sorted(section_counts.keys()):
    print(f"  Section {sid}: {section_counts[sid]} exercises")

# Save
with open('all_exercises.json', 'w') as f:
    json.dump(exercises, f, indent=2)
print(f"Saved to all_exercises.json\n")

# Extract all quizzes
print("Extracting quizzes...")
quizzes = extract_all_quizzes('sample_quiz_questions_1.json')
print(f"Found {len(quizzes)} quizzes")

# Count by section
quiz_section_counts = {}
for q in quizzes:
    sid = q['section_id']
    quiz_section_counts[sid] = quiz_section_counts.get(sid, 0) + 1

print("Quizzes by section:")
for sid in sorted(quiz_section_counts.keys()):
    print(f"  Section {sid}: {quiz_section_counts[sid]} quizzes")

# Save
with open('all_quizzes.json', 'w') as f:
    json.dump(quizzes, f, indent=2)
print(f"Saved to all_quizzes.json")

# Write summary
with open('extraction_summary.txt', 'w') as f:
    f.write(f"EXTRACTION COMPLETE\n\n")
    f.write(f"Total exercises: {len(exercises)}\n")
    f.write(f"Total quizzes: {len(quizzes)}\n\n")
    f.write("Exercises by section:\n")
    for sid in sorted(section_counts.keys()):
        f.write(f"  Section {sid}: {section_counts[sid]}\n")
    f.write("\nQuizzes by section:\n")
    for sid in sorted(quiz_section_counts.keys()):
        f.write(f"  Section {sid}: {quiz_section_counts[sid]}\n")

print("\nSummary saved to extraction_summary.txt")
