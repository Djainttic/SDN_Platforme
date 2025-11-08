import json
import requests

# Load cleaned exercise data
with open('exercises_clean.json', 'r') as f:
    exercises = json.load(f)

# Load cleaned quiz data
with open('quizzes_clean.json', 'r') as f:
    quizzes = json.load(f)

print(f"\\nLoaded {len(exercises)} exercises")
print(f"Loaded {len(quizzes)} quiz questions\\n")

# Insert exercises
url = "https://zwtjirdodmupjsissjzr.supabase.co/functions/v1/bulk-content-manager"
headers = {
    "Content-Type": "application/json",
    "apikey": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inp3dGppcmRvZG11cGpzaXNzanpyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjIxMzg1OTcsImV4cCI6MjA3NzcxNDU5N30.1XSG3JSBCx9qPyfY8CNfHLBPc5BCweNA5neFfGUyZ34",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inp3dGppcmRvZG11cGpzaXNzanpyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjIxMzg1OTcsImV4cCI6MjA3NzcxNDU5N30.1XSG3JSBCx9qPyfY8CNfHLBPc5BCweNA5neFfGUyZ34"
}

print("=== Inserting Exercises ===")
response1 = requests.post(url, json={"action": "bulk_insert_exercises", "data": exercises}, headers=headers)
print(f"Status: {response1.status_code}")
result1 = response1.json()
print(f"Response: {json.dumps(result1, indent=2)}")

print("\\n=== Inserting Quiz Questions ===")
response2 = requests.post(url, json={"action": "bulk_insert_quizzes", "data": quizzes}, headers=headers)
print(f"Status: {response2.status_code}")
result2 = response2.json()
print(f"Response: {json.dumps(result2, indent=2)}")

print("\\n=== Verification ===")
response3 = requests.post(url, json={"action": "get_content_stats"}, headers=headers)
stats = response3.json()
print(f"Final Stats:\\n{json.dumps(stats, indent=2)}")

# Write results to file for verification
with open('/workspace/populate_results.txt', 'w') as f:
    f.write(f"Exercises loaded: {len(exercises)}\\n")
    f.write(f"Quizzes loaded: {len(quizzes)}\\n")
    f.write(f"Exercises inserted: {result1.get('inserted', 0)}\\n")
    f.write(f"Quizzes inserted: {result2.get('inserted', 0)}\\n")
    f.write(f"\\nFinal statistics:\\n{json.dumps(stats, indent=2)}\\n")

print("\\nResults saved to /workspace/populate_results.txt")
