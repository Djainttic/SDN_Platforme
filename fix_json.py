#!/usr/bin/env python3
"""
Fix and merge the lab content JSON files
"""
import json
import re

# Read the malformed file
with open('sample_lab_content.json', 'r') as f:
    content = f.read()

# Find the position where the first JSON structure ends
# It should be "]}\n" then we have extra content
first_end = content.find(']\n}')
if first_end > 0:
    # Get the first part (valid JSON)
    first_part = content[:first_end + 3]  # Include ]\n}
    first_data = json.loads(first_part)
    
    # Get the rest (malformed part starting with comma)
    rest_content = content[first_end + 3:].strip()
    
    # Remove leading comma and whitespace
    if rest_content.startswith(','):
        rest_content = rest_content[1:].strip()
    
    # Wrap it in an array if needed
    if rest_content.startswith('{'):
        rest_content = '[' + rest_content + ']'
    
    # Try to parse the rest
    try:
        rest_data = json.loads(rest_content)
        # Merge the exercises
        all_exercises = first_data['exercises'] + rest_data
        
        # Create final structure
        final_data = {
            "exercises": all_exercises
        }
        
        # Save corrected file
        with open('sample_lab_content_fixed.json', 'w') as f:
            json.dump(final_data, f, indent=2)
        
        print(f"✓ Fixed! Total exercises: {len(all_exercises)}")
        print(f"✓ Saved to sample_lab_content_fixed.json")
        
    except Exception as e:
        print(f"Error parsing rest: {e}")
        print(f"Rest content preview: {rest_content[:200]}")
else:
    print("Could not find the split point in the JSON")
