import json
import re

def merge_json_objects(filename):
    """Read a file with multiple JSON objects and merge them"""
    with open(filename, 'r') as f:
        content = f.read()
    
    # Find all JSON objects by splitting on "}\n  ," or similar patterns
    # Use regex to find closing braces followed by comma
    objects = []
    current_depth = 0
    current_obj = ""
    
    for char in content:
        current_obj += char
        if char == '{':
            current_depth += 1
        elif char == '}':
            current_depth -= 1
            if current_depth == 0 and current_obj.strip():
                try:
                    obj = json.loads(current_obj.strip().rstrip(','))
                    objects.append(obj)
                    current_obj = ""
                except json.JSONDecodeError:
                    pass  # Continue building
    
    # If there's remaining content
    if current_obj.strip():
        try:
            obj = json.loads(current_obj.strip().rstrip(','))
            objects.append(obj)
        except:
            pass
    
    return objects

# Process exercises
print("Processing exercises...")
exercise_objects = merge_json_objects('sample_lab_content.json')
all_exercises = []
for obj in exercise_objects:
    if 'exercises' in obj:
        all_exercises.extend(obj['exercises'])
    elif isinstance(obj, list):
        all_exercises.extend(obj)
    elif 'section_id' in obj:
        all_exercises.append(obj)

print(f"Found {len(all_exercises)} exercises")

# Save fixed exercises
with open('exercises_fixed.json', 'w') as f:
    json.dump(all_exercises, f, indent=2)
print("Saved to exercises_fixed.json")

# Process quizzes
print("\nProcessing quizzes...")
quiz_objects = merge_json_objects('sample_quiz_questions_1.json')
all_quizzes = []
for obj in quiz_objects:
    if 'quiz_questions' in obj:
        all_quizzes.extend(obj['quiz_questions'])
    elif isinstance(obj, list):
        all_quizzes.extend(obj)
    elif 'section_id' in obj:
        all_quizzes.append(obj)

print(f"Found {len(all_quizzes)} quiz questions")

# Save fixed quizzes
with open('quizzes_fixed.json', 'w') as f:
    json.dump(all_quizzes, f, indent=2)
print("Saved to quizzes_fixed.json")
