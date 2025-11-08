# Manual Testing Guide for SDN Lab Platform - Phase 1

## Overview
This guide provides comprehensive testing instructions for all Phase 1 professor account features.

**Deployed Application**: https://tux051sfv9tp.space.minimax.io

**Test Account (Professor)**:
- Email: user123@gmail.com
- Role: Professor (configured in database)

## Testing Pathways

### 1. Authentication & Role-Based Routing

**Steps:**
1. Open https://tux051sfv9tp.space.minimax.io
2. Log in with test professor account
3. **Expected**: Redirect to `/professor` dashboard (not student dashboard)
4. **Expected**: See professor navigation sidebar with:
   - Dashboard
   - Students
   - Progress
   - Content
   - Lab Settings
   - Classes

**Success Criteria:**
- ✓ Login successful
- ✓ Redirected to professor interface
- ✓ All navigation items visible
- ✓ No access to student-only routes

---

### 2. Professor Dashboard

**Location**: `/professor` (default landing page)

**Elements to Verify:**
1. **Stats Cards** (top section):
   - Total Students count
   - Active Classes count
   - Average Completion percentage
   - (Values may be 0 initially - this is expected)

2. **Recent Activity Section**:
   - Shows recent student actions
   - May be empty initially

3. **Quick Actions**:
   - "Add Student" button
   - "Create Class" button
   - "View Progress" button
   - All buttons should be clickable

**Success Criteria:**
- ✓ Dashboard loads without errors
- ✓ All stat cards display
- ✓ Quick action buttons are functional

---

### 3. Student Management (CRITICAL PATHWAY)

**Location**: Navigate to "Students" from sidebar

**Test 3A: View Student List**
- **Expected**: Empty table initially with message "No students found"
- **Expected**: Search bar and "Add Student" button visible

**Test 3B: Add Student**
1. Click "Add Student" button
2. **Expected**: Modal dialog opens
3. Fill in form:
   - Name: "Test Student"
   - Email: "teststudent@example.com"
   - Class: (Select from dropdown if classes exist, or leave empty)
   - Enrollment Date: (Select date)
4. Click "Add Student"
5. **Expected**: Toast notification "Student added successfully"
6. **Expected**: Student appears in table

**Test 3C: Search Student**
1. Type "Test" in search bar
2. **Expected**: Table filters to show matching students

**Test 3D: Edit Student**
1. Click "Edit" button on a student row
2. **Expected**: Modal opens with pre-filled data
3. Change name to "Test Student Updated"
4. Click "Update Student"
5. **Expected**: Toast "Student updated successfully"
6. **Expected**: Name updated in table

**Test 3E: Delete Student**
1. Click "Delete" button on a student row
2. **Expected**: Confirmation dialog appears
3. Click "Delete"
4. **Expected**: Toast "Student deleted successfully"
5. **Expected**: Student removed from table

**Success Criteria:**
- ✓ All CRUD operations work
- ✓ Search/filter functional
- ✓ Toast notifications appear
- ✓ Table updates in real-time

---

### 4. Class Management

**Location**: Navigate to "Classes" from sidebar

**Test 4A: Create Class**
1. Click "Create Class" button
2. Fill in form:
   - Name: "Fall 2024 SDN Lab"
   - Code: "SDN-F24"
   - Semester: "Fall 2024"
   - Start Date: (Select date)
   - End Date: (Select date)
3. Click "Create Class"
4. **Expected**: Toast "Class created successfully"
5. **Expected**: Class appears in list

**Test 4B: Edit Class**
1. Click "Edit" on a class
2. Change name to "Fall 2024 SDN Lab - Section A"
3. Click "Update Class"
4. **Expected**: Toast "Class updated successfully"

**Test 4C: Delete Class**
1. Click "Delete" on a class
2. Confirm deletion
3. **Expected**: Toast "Class deleted successfully"

**Success Criteria:**
- ✓ Class creation works
- ✓ Edit functionality works
- ✓ Delete with confirmation works

---

### 5. Progress Tracking

**Location**: Navigate to "Progress" from sidebar

**Prerequisites**: Create at least one student and one class first

**Test 5A: Individual Progress View**
1. Click "Individual" tab (should be default)
2. Select a student from dropdown
3. **Expected**: Shows progress for all 9 lab sections (Section 0-8)
4. **Expected**: Displays:
   - Section name
   - Progress bar (percentage)
   - Score
   - Time spent
   - Commands executed count

**Test 5B: Class Overview**
1. Click "Class Overview" tab
2. Select a class from dropdown
3. **Expected**: Shows:
   - Overall class completion rate
   - Progress heatmap for all students
   - List of students
   - Completion percentages per section

**Note**: Progress data will be empty initially. To test with data:
1. Log out
2. Log in as a student (create a student account)
3. Complete some lab exercises
4. Log back in as professor
5. Check progress tracking

**Success Criteria:**
- ✓ Both tabs switch correctly
- ✓ Student/class dropdowns work
- ✓ Progress displays correctly when data exists
- ✓ Charts and visualizations render

---

### 6. Content Editor

**Location**: Navigate to "Content" from sidebar

**Test 6A: View Exercises**
1. Select a section from dropdown (Section 0-8)
2. Click "Exercises" tab
3. **Expected**: Shows list of exercises for that section
4. **Expected**: Each exercise shows:
   - Title
   - Instructions (truncated)
   - Edit button

**Test 6B: Add New Exercise**
1. Click "Add New Exercise" button
2. **Expected**: Modal opens
3. Fill in form:
   - Title: "Test Exercise"
   - Instructions: "This is a test exercise"
   - Expected Output: "output example"
   - Hints: "Hint 1"
   - Points: 10
4. Click "Create Exercise"
5. **Expected**: Toast "Exercise created successfully"
6. **Expected**: New exercise appears in list

**Test 6C: Edit Exercise**
1. Click "Edit" on an exercise
2. **Expected**: Modal opens with pre-filled data
3. Modify title
4. Click "Update Exercise"
5. **Expected**: Toast "Exercise updated successfully"

**Test 6D: View/Edit Quizzes**
1. Click "Quizzes" tab
2. Click "Add New Quiz Question"
3. Fill in form:
   - Question: "What is SDN?"
   - Options: "Option 1", "Option 2", "Option 3", "Option 4"
   - Correct Answer: 0 (first option)
   - Explanation: "Explanation text"
   - Points: 5
4. Click "Create Quiz Question"
5. **Expected**: Toast "Quiz question created successfully"
6. **Expected**: Question appears in list

**Success Criteria:**
- ✓ Section selector works
- ✓ Tabs switch between exercises/quizzes
- ✓ CRUD operations work for both types
- ✓ Forms validate properly

---

### 7. Lab Settings (CRITICAL FEATURE)

**Location**: Navigate to "Lab Settings" from sidebar

**Prerequisites**: Create at least one class first

**Test 7A: View Lab Settings**
1. Select a class from dropdown
2. **Expected**: Table shows all 9 sections (Section 0-8)
3. **Expected**: Each row has:
   - Section name
   - Available toggle
   - Unlock Date picker
   - Prerequisites multi-select
   - Passing Score input
   - Custom Message textarea
   - Save button

**Test 7B: Configure Basic Availability**
1. For Section 0:
   - Toggle "Available" to ON
   - Leave unlock date empty (available immediately)
   - No prerequisites (Section 0 is always first)
   - Set passing score: 70
2. Click "Save" for Section 0
3. **Expected**: Toast "Lab settings saved for Section 0"

**Test 7C: Configure Prerequisites (KEY FEATURE)**
1. For Section 1:
   - Toggle "Available" to ON
   - Set unlock date: (today's date or future)
   - Select prerequisite: "Section 0"
   - Set passing score: 75
   - Custom message: "Complete Section 0 with 75% before accessing"
2. Click "Save"
3. **Expected**: Toast "Lab settings saved for Section 1"

**Test 7D: Configure Multiple Prerequisites**
1. For Section 5:
   - Toggle "Available" to ON
   - Select prerequisites: "Section 3" and "Section 4"
   - Set passing score: 80
   - Custom message: "Complete Sections 3 and 4 first"
2. Click "Save"
3. **Expected**: Successfully saved

**Test 7E: Save All Settings**
1. Configure multiple sections
2. Click "Save All Settings" button at top
3. **Expected**: Toast showing all sections saved
4. Refresh page
5. Select same class
6. **Expected**: All settings persist (toggled, dates, prerequisites, scores)

**Test 7F: Disable Section**
1. For any section, toggle "Available" to OFF
2. Add custom message: "This lab is currently under maintenance"
3. Click "Save"
4. **Expected**: Section saved as unavailable

**Success Criteria:**
- ✓ All settings save correctly
- ✓ Prerequisites can be selected/multi-selected
- ✓ Unlock dates work
- ✓ Passing score validation works
- ✓ Settings persist after page refresh
- ✓ "Save All" works for bulk operations

---

### 8. Student Dashboard Lab Access Control (CRITICAL INTEGRATION)

**Prerequisites**: 
- Configure lab settings as professor (Step 7)
- Have a student account created

**Test 8A: Access Locked Section**
1. Log out from professor account
2. Create/log in as student account
3. Navigate to student dashboard
4. **Expected**: Sections with prerequisites show:
   - Lock icon 🔒
   - "Prerequisites required" message
   - Custom message if configured
   - Prerequisites list displayed
5. Try to click locked section
6. **Expected**: Toast notification explaining why locked

**Test 8B: Complete Prerequisites and Unlock**
1. As student, complete prerequisite section(s)
2. Achieve required passing score
3. Navigate back to dashboard
4. **Expected**: Previously locked section now unlocked
5. Click section
6. **Expected**: Can access section content

**Test 8C: Unlock Date Control**
1. As professor, set a section unlock date to tomorrow
2. As student, try to access that section
3. **Expected**: Section locked with message showing unlock date
4. As professor, change unlock date to today
5. As student, refresh dashboard
6. **Expected**: Section now accessible

**Success Criteria:**
- ✓ Lock icon displays for restricted sections
- ✓ Prerequisites are enforced
- ✓ Unlock dates are respected
- ✓ Custom messages display correctly
- ✓ Sections unlock when prerequisites met

---

### 9. Responsive Design

**Test on Multiple Devices:**
1. Desktop (1920x1080)
2. Tablet (768x1024)
3. Mobile (375x667)

**Check:**
- ✓ Navigation adapts (sidebar/hamburger menu)
- ✓ Tables are scrollable on mobile
- ✓ Forms are usable on small screens
- ✓ Buttons/inputs properly sized
- ✓ No horizontal scrolling issues

---

### 10. Navigation & Routing

**Test All Routes:**
- `/professor` → Dashboard
- `/professor/students` → Student Management
- `/professor/classes` → Class Management
- `/professor/progress` → Progress Tracking
- `/professor/content` → Content Editor
- `/professor/lab-settings` → Lab Settings

**Test:**
1. Click each sidebar link
2. **Expected**: URL changes
3. **Expected**: Correct page loads
4. **Expected**: Sidebar highlights active page
5. Use browser back/forward buttons
6. **Expected**: Navigation works correctly

**Success Criteria:**
- ✓ All routes accessible
- ✓ Active page highlighted
- ✓ Browser navigation works
- ✓ No broken links

---

## Error Scenarios to Test

### 1. Network Errors
- Disconnect internet during form submission
- **Expected**: Error toast with retry option

### 2. Invalid Data
- Try to create student with invalid email
- Try to set passing score > 100
- **Expected**: Form validation catches errors

### 3. Duplicate Data
- Try to create student with existing email
- **Expected**: Error message from backend

### 4. Empty States
- View progress with no students
- View content with no exercises
- **Expected**: Helpful empty state messages

---

## Integration Testing Checklist

- [ ] Professor can manage students and they appear in database
- [ ] Class assignments persist and filter correctly
- [ ] Progress tracking reflects actual student activity
- [ ] Content changes are visible to students immediately
- [ ] Lab settings control student access in real-time
- [ ] Role-based access prevents students from accessing professor routes
- [ ] All toast notifications appear and disappear correctly
- [ ] No console errors in browser developer tools

---

## Known Limitations & Future Enhancements

**Current Scope (Phase 1):**
- Basic CRUD operations functional
- Manual testing required (automated tests not yet implemented)
- Limited analytics (Phase 2)
- No grading automation yet (Phase 2)

**Phase 2 Features (Planned):**
- Advanced analytics dashboards
- Automated grading system
- Bulk operations (import/export)
- Email notifications
- Real-time collaboration tools

---

## Reporting Issues

If you encounter any issues during testing, please document:
1. **What you were trying to do** (steps to reproduce)
2. **What you expected to happen**
3. **What actually happened**
4. **Browser and device info**
5. **Screenshots if applicable**
6. **Console errors** (press F12 → Console tab)

---

## Quick Test Summary

For a rapid validation (5-10 minutes):
1. ✅ Log in as professor → Dashboard loads
2. ✅ Create one class
3. ✅ Add one student
4. ✅ Configure lab settings for Section 0 (make available)
5. ✅ Configure Section 1 with Section 0 as prerequisite
6. ✅ Add one exercise in Content Editor
7. ✅ Check progress tracking (will be empty initially)
8. ✅ Log out, log in as student → Verify Section 1 is locked

If all 8 quick tests pass, core functionality is working correctly.
