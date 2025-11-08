# Lab Management - Quick Reference Guide

## Access Lab Management
**URL**: https://tus9vo7shfes.space.minimax.io
**Login**: jgyzqdwm@minimax.com / 29AttRMrtU
**Navigation**: Professor Sidebar → "Labs" (flask icon)

## Main Features

### 1. Overview Dashboard
**What You See**:
- All 9 lab sections in grid layout
- Statistics for each lab (exercises, quizzes, completion rate)
- Overall platform statistics at top
- Progress bars showing student completion

**Actions Available**:
- Preview Lab - View content as students see it
- Edit Content - Modify exercises and quizzes

### 2. Preview Mode
**How to Access**: Click "Preview Lab" on any section card

**What You Can See**:
- Complete tutorial content
- Learning objectives (e.g., "Understand RYU controller architecture")
- Step-by-step instructions
- Command examples (e.g., `sudo mn --version`)
- All content exactly as students see it

**Actions**:
- Click "Edit Content" to modify exercises/quizzes
- Click "Back to Labs" to return to overview

### 3. Edit Content
**How to Access**: Click "Edit Content" on any section card

**What You Can Edit**:
- **Exercises**: Title, description, instructions, difficulty
- **Quiz Questions**: Question text, options, correct answer, points

**How to Edit**:
1. Click "Edit Content" for a section
2. Opens ContentEditor with that section selected
3. Switch between "Exercises" and "Quizzes" tabs
4. Click "Add Exercise" or "Add Question"
5. Fill in the form and click "Save"

### 4. Student Progress
**Where to See It**: On each lab card in overview

**Information Shown**:
- Total students
- Completed count
- In-progress count
- Completion percentage
- Visual progress bar

## Lab Sections Overview

| Section | Title | Topics |
|---------|-------|--------|
| 0 | Environment Setup | Install tools, configure VMs |
| 1 | Introduction to SDN Tools | Mininet CLI, network exploration |
| 2 | Controller & Data Plane | RYU controller, OpenFlow |
| 3 | Flow Table Management | OVS flow rules, priorities |
| 4 | OpenFlow Messages | Packet processing, flow installation |
| 5 | Traffic Analysis | Wireshark, OpenFlow traffic |
| 6 | Custom Topology Design | Build custom networks |
| 7 | Advanced Programming | Custom RYU applications |
| 8 | Security & QoS | Firewall, DDoS mitigation |

## What Can Be Edited

### YES - Through UI
- Exercise content (title, description, instructions)
- Quiz questions (text, options, answers)
- Difficulty levels
- Point values
- Hints and expected outputs

### NO - Requires Code Changes
- Tutorial objectives (e.g., "Understand SDN tools")
- Step-by-step instructions (e.g., "Verify Tool Installation")
- Command examples (e.g., `ryu-manager --version`)
- Section titles and descriptions

## Common Tasks

### Review Lab Content
1. Click "Labs" in sidebar
2. Scan the overview for statistics
3. Click "Preview Lab" on any section
4. Review objectives and steps
5. Return to overview with "Back to Labs"

### Add New Exercise
1. Click "Edit Content" on target section
2. Select "Exercises" tab
3. Click "Add Exercise"
4. Fill in: Exercise ID, Title, Description, Instructions
5. Set difficulty level
6. Click "Save"

### Add New Quiz Question
1. Click "Edit Content" on target section
2. Select "Quizzes" tab
3. Click "Add Question"
4. Enter question text
5. Fill in 4 options
6. Select correct answer
7. Set points value
8. Click "Save"

### Check Student Progress
1. View overview dashboard
2. Look at progress bars on each lab card
3. Check completion percentages
4. Note "completed" vs "in progress" counts

### Modify Existing Content
1. Click "Edit Content" on section
2. Find the exercise or quiz to modify
3. Click edit icon (pencil)
4. Make changes
5. Click "Save"

### Delete Content
1. Click "Edit Content" on section
2. Find the exercise or quiz to delete
3. Click delete icon (trash)
4. Confirm deletion

## Tips

1. **Use Preview First**: Before editing, preview to see current state
2. **Check Progress Data**: Use completion rates to identify sections needing improvement
3. **Be Consistent**: Match difficulty levels across similar exercises
4. **Test Changes**: Preview after editing to verify content appears correctly
5. **Student View**: Preview mode shows exactly what students see

## Navigation Flow

```
Labs Overview → Preview Lab → View Content → Back to Overview
                    ↓
              Edit Content → Content Editor → Save → Reload
```

## Statistics Explained

**Total Labs**: 9 (Sections 0-8)
**Total Exercises**: Sum of all exercise counts
**Total Quizzes**: Sum of all quiz questions
**Active Students**: Unique students with progress records
**Completion Rate**: (Completed / Total Students) × 100%

## Important Notes

1. **Tutorial Content**: Objectives and steps are VIEW-ONLY through UI
2. **Save Required**: Changes to exercises/quizzes must be explicitly saved
3. **Refresh Data**: Statistics update on page load
4. **Section Order**: Labs are sequential (0→8)
5. **Prerequisites**: Earlier sections may be required for later ones

## Troubleshooting

**Can't see Labs menu item**:
- Verify you're logged in as professor
- Check sidebar navigation (look for flask icon)
- Refresh page if needed

**Preview not working**:
- Ensure lab section number is valid (0-8)
- Try "Back to Labs" and preview again
- Check browser console for errors

**Edit not saving**:
- Verify all required fields filled
- Check for error messages
- Ensure you clicked "Save" button
- Check internet connection

**Statistics showing zero**:
- May indicate no student data yet
- Check that students have been added
- Verify students have accessed labs

## Quick Access URLs

- **Overview**: /professor/labs
- **Edit Content**: /professor/content or /professor/content-editor
- **Student Management**: /professor/students
- **Progress Tracking**: /professor/progress

## Support

For issues with:
- **Viewing/Previewing**: Check browser compatibility, clear cache
- **Editing**: Verify form fields, check error messages
- **Tutorial Content Changes**: Contact development team
- **Database Issues**: Check Supabase connection

---
**Last Updated**: 2025-11-04
**Platform Version**: v1.0 (Lab Management)
**Status**: Production
