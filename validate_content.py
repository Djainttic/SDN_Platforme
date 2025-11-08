#!/usr/bin/env python3
"""
Script to validate and count lab content for database insertion
"""
import json

def validate_and_count():
    # Load exercises
    with open('sample_lab_content.json', 'r') as f:
        exercises_data = json.load(f)
    
    exercises = exercises_data['exercises']
    print(f"✓ Total exercises: {len(exercises)}")
    
    # Count exercises by section
    ex_by_section = {}
    for ex in exercises:
        section = ex['section_id']
        ex_by_section[section] = ex_by_section.get(section, 0) + 1
    
    print("\nExercises by section:")
    for section in sorted(ex_by_section.keys()):
        print(f"  Section {section}: {ex_by_section[section]} exercises")
    
    # Load quizzes
    with open('sample_quiz_questions_1.json', 'r') as f:
        quizzes_data = json.load(f)
    
    quizzes = quizzes_data['quiz_questions']
    print(f"\n✓ Total quiz questions: {len(quizzes)}")
    
    # Count quizzes by section
    qz_by_section = {}
    for qz in quizzes:
        section = qz['section_id']
        qz_by_section[section] = qz_by_section.get(section, 0) + 1
    
    print("\nQuiz questions by section:")
    for section in sorted(qz_by_section.keys()):
        print(f"  Section {section}: {qz_by_section[section]} questions")
    
    # Check coverage
    print("\n=== Coverage Summary ===")
    for section in range(9):
        ex_count = ex_by_section.get(section, 0)
        qz_count = qz_by_section.get(section, 0)
        status = "✓" if (ex_count > 0 and qz_count > 0) else "✗"
        print(f"{status} Section {section}: {ex_count} exercises, {qz_count} quizzes")
    
    # Validate required fields
    print("\n=== Validating Exercise Fields ===")
    required_ex_fields = ['section_id', 'exercise_id', 'title', 'description', 'instructions', 'difficulty']
    for i, ex in enumerate(exercises[:3]):  # Check first 3
        missing = [f for f in required_ex_fields if f not in ex]
        if missing:
            print(f"✗ Exercise {i}: Missing fields {missing}")
        else:
            print(f"✓ Exercise {i}: All required fields present")
    
    print("\n=== Validating Quiz Fields ===")
    required_qz_fields = ['section_id', 'question', 'options', 'correct_answer', 'difficulty', 'points']
    for i, qz in enumerate(quizzes[:3]):  # Check first 3
        missing = [f for f in required_qz_fields if f not in qz]
        if missing:
            print(f"✗ Quiz {i}: Missing fields {missing}")
        else:
            print(f"✓ Quiz {i}: All required fields present")
    
    print("\n=== Ready for Database Insertion ===")
    print(f"Total items to insert: {len(exercises) + len(quizzes)}")

if __name__ == '__main__':
    validate_and_count()
