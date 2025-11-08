# SDN Lab Platform - Comprehensive Manual Testing Guide

## Testing Overview

**Platform URL**: https://tus9vo7shfes.space.minimax.io  
**Testing Date**: 2025-11-04
**Platform Status**: FULLY DEPLOYED - ALL CONTENT POPULATED

### Test Credentials

**Professor Account**:
- Email: `jgyzqdwm@minimax.com`
- Password: `29AttRMrtU`

**Student Accounts** (all use password `Student123!`):
- alice.chen@students.edu (3/9 sections completed)
- bob.martinez@students.edu (5/9 sections completed)
- carol.johnson@students.edu (1/9 completed)
- david.kim@students.edu (4/9 completed)
- emma.wilson@students.edu (1/9 completed)

## Critical Test Priority

### MUST TEST (High Priority)
1. **Content Editor** - Verify 63 exercises and 62 quizzes are visible
2. **Lab Management** - All 9 sections display correctly
3. **Student Lab Interface** - All 5 tabs work (Tutorial, Terminal, Topology, Flow Tables, Assessment)
4. **Authentication** - Both professor and student login
5. **Database Content** - Bonus content is accessible

### SHOULD TEST (Medium Priority)
6. Student/Class Management
7. Analytics and Grading
8. Progress Tracking
9. Report Generation

### NICE TO TEST (Low Priority)
10. Advanced features (TA Management, Peer Reviews, LMS Integration)

---

## PART 1: PROFESSOR TESTING

### Test 1.1: Professor Login ✓ HIGH PRIORITY
**Objective**: Verify professor authentication

**Steps**:
1. Go to https://tus9vo7shfes.space.minimax.io
2. Click "Sign In"
3. Enter: `jgyzqdwm@minimax.com`
4. Enter: `29AttRMrtU`
5. Click "Sign In"

**Expected**: 
- Login succeeds
- Redirect to professor dashboard
- Professor navigation menu visible

**Report Issues**: If login fails, cannot proceed with testing

---

### Test 1.2: Content Editor ✓ CRITICAL - HIGHEST PRIORITY
**Objective**: VERIFY BONUS CONTENT IS DEPLOYED (63 exercises, 62 quizzes)

**Steps**:
1. After login, click "Content Editor" in navigation
2. Look for "Exercises" tab/section
3. **COUNT EXERCISES**:
   - Should show **63 total exercises**
   - Section 0: 7 exercises
   - Section 1: 7 exercises
   - Section 2: 7 exercises
   - Section 3: 7 exercises
   - Section 4: 7 exercises
   - Section 5: 7 exercises
   - Section 6: 7 exercises
   - Section 7: 7 exercises
   - Section 8: 7 exercises

4. Switch to "Quizzes" tab/section
5. **COUNT QUIZZES**:
   - Should show **62 total quizzes**
   - Sections 0-2: 0 quizzes (these are hardcoded in frontend)
   - Section 3: 12 quizzes
   - Section 4: 10 quizzes
   - Section 5: 10 quizzes
   - Section 6: 10 quizzes
   - Section 7: 10 quizzes
   - Section 8: 10 quizzes

6. Try clicking "Edit" on one exercise
7. Verify edit form opens with exercise details

**Expected**:
- Content Editor loads successfully
- **63 exercises visible** (NOT 0, NOT 22)
- **62 quizzes visible** (NOT 0, NOT 1)
- Distribution matches above
- Edit functionality works

**THIS IS THE MOST CRITICAL TEST**
**If counts are wrong (e.g., showing 0, 22, or 1), report immediately**

---

### Test 1.3: Lab Management ✓ HIGH PRIORITY
**Objective**: Verify all 9 lab sections are accessible

**Steps**:
1. Click "Labs" in navigation
2. Verify ALL 9 sections visible (Section 0 through Section 8)
3. Check each section shows:
   - Section title (e.g., "Section 0: SDN Environment Setup")
   - Exercise count: 7
   - Quiz count: 0 (sections 0-2) or 10+ (sections 3-8)
   - Preview/View button

4. Click "Preview" on Section 0
5. Verify lab content displays:
   - Learning objectives
   - Step-by-step instructions
   - SDN commands (RYU, Mininet, OVS, etc.)

**Expected**:
- All 9 sections visible
- Correct counts per section
- Preview functionality works
- Content displays correctly

---

### Test 1.4: Student Management
**Objective**: Test student creation

**Steps**:
1. Click "Students" in navigation
2. Verify 5 existing students listed
3. Click "Add Student"
4. Fill form:
   - Email: test.new@test.edu
   - First Name: Test
   - Last Name: New
   - Password: TestPass123!
5. Submit

**Expected**:
- Student list displays
- Add form works
- New student created
- Success message appears

---

### Test 1.5: Class Management
**Objective**: Test class creation

**Steps**:
1. Click "Classes" in navigation
2. Click "Add Class"
3. Fill form:
   - Name: Test Class 2025
   - Code: SDN101
   - Semester: Spring 2025
   - Start/End dates
4. Submit

**Expected**:
- Class list displays
- Add form works
- Class created
- Success message

---

### Test 1.6: Analytics Dashboard
**Objective**: Verify analytics displays

**Steps**:
1. Click "Advanced Analytics" (or "Analytics")
2. Look for charts/visualizations
3. Check for data display

**Expected**:
- Page loads
- Charts render
- Data shows (even if minimal)

---

### Test 1.7: Reports
**Objective**: Test report generation

**Steps**:
1. Click "Reports"
2. Select report type (Progress/Grades)
3. Click "Generate CSV" or "Generate PDF"

**Expected**:
- Reports page loads
- Export buttons work
- File downloads

---

## PART 2: STUDENT TESTING

### Test 2.1: Student Login ✓ HIGH PRIORITY
**Objective**: Verify student authentication

**Steps**:
1. Logout from professor (or use incognito/private window)
2. Go to https://tus9vo7shfes.space.minimax.io
3. Click "Sign In"
4. Enter: `alice.chen@students.edu`
5. Enter: `Student123!`
6. Click "Sign In"

**Expected**:
- Login succeeds
- Redirect to student dashboard
- Shows progress (3/9 completed for alice)
- Student navigation visible

---

### Test 2.2: Student Dashboard
**Objective**: Verify progress displays

**Steps**:
1. After login, examine dashboard
2. Check for:
   - Progress tracker showing 3/9 completed
   - Statistics
   - Lab access button

**Expected**:
- Dashboard loads
- Progress shows correctly
- Can navigate to labs

---

### Test 2.3: Lab Interface - All 5 Tabs ✓ CRITICAL
**Objective**: Verify complete lab functionality

**Steps**:
1. Click "Labs" or "Start Lab"
2. Select "Section 0"
3. **Test each tab**:

**TUTORIAL TAB**:
4. Click "Tutorial"
5. Verify content shows:
   - Learning objectives
   - Step-by-step instructions
   - SDN commands

**TERMINAL TAB**:
6. Click "Terminal"
7. Verify interactive terminal displays
8. Try typing a command (optional)

**TOPOLOGY TAB**:
9. Click "Topology"
10. Verify network diagram displays
11. Look for switches, hosts, controller nodes

**FLOW TABLES TAB**:
12. Click "Flow Tables"
13. Verify flow table interface displays

**ASSESSMENT TAB**:
14. Click "Assessment"
15. Verify quiz questions display
16. Try answering one question
17. Submit answer
18. Check for feedback

**Expected**:
- All 5 tabs accessible
- Tutorial content loads (NOT empty)
- Terminal interface visible
- Topology visualization displays
- Flow tables interface displays
- Quiz loads and works

**THIS IS CRITICAL FOR STUDENT EXPERIENCE**

---

### Test 2.4: Lab Section Content
**Objective**: Verify all sections have content

**Steps**:
1. Test Section 0 (Setup)
2. Test Section 4 (OpenFlow)
3. Test Section 8 (Security)
4. For each, verify Tutorial and Assessment tabs have content

**Expected**:
- All sections accessible
- All have tutorial content
- All have quiz questions

---

### Test 2.5: Quiz Functionality
**Objective**: Test assessment system

**Steps**:
1. In any lab section, go to Assessment tab
2. Read question
3. Select answer
4. Click "Submit"
5. Verify feedback (correct/incorrect)
6. Complete entire quiz
7. Check for score

**Expected**:
- Questions display clearly
- Can select answers
- Submit works
- Feedback provided
- Score calculated

---

### Test 2.6: Progress Tracking
**Objective**: Verify progress updates

**Steps**:
1. After completing quiz, go back to dashboard
2. Check if progress updated
3. Look for completion markers

**Expected**:
- Progress updates
- Dashboard reflects changes
- Section marked complete

---

## QUICK TEST CHECKLIST

Use this for rapid verification:

### CRITICAL TESTS (Must Pass)
- [ ] Professor login works
- [ ] Content Editor shows **63 exercises**
- [ ] Content Editor shows **62 quizzes**
- [ ] Student login works
- [ ] Lab interface - Tutorial tab has content
- [ ] Lab interface - Assessment tab has quizzes

### IMPORTANT TESTS
- [ ] All 9 lab sections visible
- [ ] Lab preview works
- [ ] Student dashboard shows progress
- [ ] All 5 lab tabs load

### NICE TO HAVE
- [ ] Student/Class creation works
- [ ] Analytics displays
- [ ] Reports export works

---

## EXPECTED TEST RESULTS

### What Should Work
Based on previous testing and deployment:
- All authentication
- Navigation and routing
- Content display
- Database operations
- Edge function calls
- Chart rendering
- Form submissions

### What Might Have Issues
- Complex interactions
- Real-time features
- File exports (browser-dependent)
- Network topology animations

---

## REPORTING RESULTS

### If Everything Works
Report: "All tests passed. Platform is production-ready."

### If Issues Found
For each issue, provide:

**Issue Template**:
```
Test: [Test number, e.g., Test 1.2]
Problem: [What went wrong]
Expected: [What should happen]
Actual: [What happened]
Account: [Which account]
Browser: [Chrome/Firefox/etc.]
```

**Example**:
```
Test: Test 1.2 Content Editor
Problem: Only showing 22 exercises instead of 63
Expected: Should show 63 exercises total
Actual: Shows 22 exercises
Account: jgyzqdwm@minimax.com
Browser: Chrome
```

---

## TROUBLESHOOTING

### Common Issues

**Login fails**:
- Double-check credentials (case-sensitive)
- Clear browser cache
- Try different browser

**Content not loading**:
- Check console (F12) for errors
- Refresh page
- Check internet connection

**Counts are wrong in Content Editor**:
- This is a critical issue
- Take screenshot
- Report immediately with exact counts shown

---

## TIME ESTIMATE
- **Quick Test** (critical only): 15 minutes
- **Thorough Test** (all high/medium priority): 45 minutes
- **Complete Test** (everything): 90 minutes

**Recommended**: Start with Quick Test to catch critical issues

---

## FINAL CHECKLIST

Before reporting completion:
- [ ] Tested as Professor
- [ ] Tested as Student
- [ ] Verified bonus content (63 exercises, 62 quizzes)
- [ ] Tested lab interface (all 5 tabs)
- [ ] Documented any issues found
- [ ] Screenshots of critical issues (if any)

---

## POST-TESTING

After completing tests:
1. Document results in test-progress-final.md
2. Report total tests passed/failed
3. Provide issue details (if any)
4. Give overall assessment: "Production Ready" or "Needs Fixes"

**Thank you for testing!**
