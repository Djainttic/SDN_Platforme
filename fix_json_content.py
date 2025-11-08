import json

# Read the entire file
with open('sample_lab_content.json', 'r') as f:
    content = f.read()

# Try to find all exercise objects
# Split by '}  ,' pattern and reconstruct
parts = content.split('}  ,')
exercises_list = []

for i, part in enumerate(parts):
    part = part.strip()
    if i < len(parts) - 1:
        part = part + '}'
    
    try:
        data = json.loads(part)
        if 'exercises' in data:
            exercises_list.extend(data['exercises'])
        elif isinstance(data, dict) and 'section_id' in data:
            exercises_list.append(data)
    except Exception as e:
        print(f"Skipping part {i}: {str(e)[:50]}")

print(f"Extracted {len(exercises_list)} exercises")

# Save as proper array
with open('sample_lab_content_fixed.json', 'w') as f:
    json.dump(exercises_list, f, indent=2)
print("Saved to sample_lab_content_fixed.json")

# Do the same for quiz questions
with open('sample_quiz_questions_1.json', 'r') as f:
    content = f.read()

parts = content.split('}  ,')
quizzes_list = []

for i, part in enumerate(parts):
    part = part.strip()
    if i < len(parts) - 1:
        part = part + '}'
    
    try:
        data = json.loads(part)
        if 'quiz_questions' in data:
            quizzes_list.extend(data['quiz_questions'])
        elif isinstance(data, dict) and 'section_id' in data:
            quizzes_list.append(data)
    except Exception as e:
        print(f"Skipping quiz part {i}: {str(e)[:50]}")

print(f"Extracted {len(quizzes_list)} quiz questions")

# Save as proper array
with open('sample_quiz_questions_fixed.json', 'w') as f:
    json.dump(quizzes_list, f, indent=2)
print("Saved to sample_quiz_questions_fixed.json")
