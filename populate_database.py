import json
import requests

# Load exercise data
with open('sample_lab_content.json', 'r') as f:
    data = json.load(f)
    exercises = data.get('exercises', data) if isinstance(data, dict) else data

# Load quiz data
with open('sample_quiz_questions_1.json', 'r') as f:
    data = json.load(f)
    quizzes = data.get('quiz_questions', data) if isinstance(data, dict) else data

print(f"Loaded {len(exercises)} exercises")
print(f"Loaded {len(quizzes)} quiz questions")

# Insert exercises
url = "https://zwtjirdodmupjsissjzr.supabase.co/functions/v1/bulk-content-manager"
headers = {
    "Content-Type": "application/json",
    "apikey": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inp3dGppcmRvZG11cGpzaXNzanpyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjIxMzg1OTcsImV4cCI6MjA3NzcxNDU5N30.1XSG3JSBCx9qPyfY8CNfHLBPc5BCweNA5neFfGUyZ34",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inp3dGppcmRvZG11cGpzaXNzanpyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjIxMzg1OTcsImV4cCI6MjA3NzcxNDU5N30.1XSG3JSBCx9qPyfY8CNfHLBPc5BCweNA5neFfGUyZ34"
}

print("\n=== Inserting Exercises ===")
response1 = requests.post(url, json={"action": "bulk_insert_exercises", "data": exercises}, headers=headers)
print(f"Status: {response1.status_code}")
print(f"Response: {response1.json()}")

print("\n=== Inserting Quiz Questions ===")
response2 = requests.post(url, json={"action": "bulk_insert_quizzes", "data": quizzes}, headers=headers)
print(f"Status: {response2.status_code}")
print(f"Response: {response2.json()}")

print("\n=== Verification ===")
response3 = requests.post(url, json={"action": "get_content_stats"}, headers=headers)
print(f"Final Stats: {json.dumps(response3.json(), indent=2)}")
