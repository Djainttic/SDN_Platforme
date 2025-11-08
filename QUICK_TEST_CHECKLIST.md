# Quick Test Checklist - Phase 1 Features

## 🎯 Essential Tests (15 minutes)

### Test 1: Professor Dashboard Access
- [ ] Log in to https://tux051sfv9tp.space.minimax.io
- [ ] Use professor account: user123@gmail.com
- [ ] Verify redirect to `/professor` dashboard
- [ ] Confirm sidebar shows: Dashboard, Students, Progress, Content, Lab Settings, Classes
- [ ] Check stats cards display (may show zeros initially)

### Test 2: Class Management
- [ ] Navigate to "Classes"
- [ ] Click "Create Class"
- [ ] Enter details:
  - Name: "SDN Lab Fall 2024"
  - Code: "SDN-F24"
  - Semester: "Fall 2024"
  - Start Date: (today)
  - End Date: (3 months from now)
- [ ] Verify toast: "Class created successfully"
- [ ] Confirm class appears in list
- [ ] Click "Edit" and change name
- [ ] Verify update works

### Test 3: Student Management
- [ ] Navigate to "Students"
- [ ] Click "Add Student"
- [ ] Enter details:
  - Name: "John Doe"
  - Email: "john.doe@example.com"
  - Class: (select your created class)
  - Enrollment Date: (today)
- [ ] Verify toast: "Student added successfully"
- [ ] Confirm student appears in table
- [ ] Test search: Type "John" in search bar
- [ ] Verify filtering works
- [ ] Click "Edit" on student
- [ ] Change name to "John Smith"
- [ ] Verify update works

### Test 4: Lab Settings Configuration (CRITICAL) ⭐
- [ ] Navigate to "Lab Settings"
- [ ] Select your class from dropdown
- [ ] Verify table shows Sections 0-8

**Configure Section 0 (Foundation):**
- [ ] Toggle "Available" to ON
- [ ] Leave unlock date empty (available immediately)
- [ ] No prerequisites needed
- [ ] Set Passing Score: 70
- [ ] Click "Save"
- [ ] Verify toast: "Lab settings saved for Section 0"

**Configure Section 1 (With Prerequisites):**
- [ ] Toggle "Available" to ON
- [ ] In Prerequisites dropdown, select "Section 0"
- [ ] Set Passing Score: 75
- [ ] Custom Message: "You must complete Section 0 with 75% score before accessing this lab"
- [ ] Click "Save"
- [ ] Verify toast: "Lab settings saved for Section 1"

**Configure Section 2 (Multiple Prerequisites):**
- [ ] Toggle "Available" to ON
- [ ] In Prerequisites dropdown, select both "Section 0" AND "Section 1"
- [ ] Set Passing Score: 80
- [ ] Custom Message: "Complete Sections 0 and 1 first"
- [ ] Click "Save"
- [ ] Verify toast: "Lab settings saved for Section 2"

**Test Unlock Date:**
- [ ] For Section 3, set unlock date to tomorrow
- [ ] Save settings
- [ ] This will be locked until tomorrow

**Verify Persistence:**
- [ ] Refresh the page (F5)
- [ ] Select same class again
- [ ] Confirm all settings are still there (toggled states, prerequisites, scores)

### Test 5: Content Editor
- [ ] Navigate to "Content"
- [ ] Select "Section 0" from dropdown
- [ ] Click "Exercises" tab

**Add Exercise:**
- [ ] Click "Add New Exercise"
- [ ] Fill in:
  - Title: "Introduction to Mininet"
  - Instructions: "Learn the basics of Mininet network emulation"
  - Expected Output: "Network topology created successfully"
  - Hints: "Use mn command"
  - Points: 10
- [ ] Click "Create Exercise"
- [ ] Verify toast and exercise appears in list

**Add Quiz Question:**
- [ ] Click "Quizzes" tab
- [ ] Click "Add New Quiz Question"
- [ ] Fill in:
  - Question: "What does SDN stand for?"
  - Options: "Software Defined Networking", "System Data Network", "Secure Data Node", "None"
  - Correct Answer: 0 (first option)
  - Explanation: "SDN stands for Software Defined Networking"
  - Points: 5
- [ ] Click "Create Quiz Question"
- [ ] Verify toast and question appears

### Test 6: Progress Tracking
- [ ] Navigate to "Progress"
- [ ] Click "Individual" tab
- [ ] Select student from dropdown
- [ ] Verify display shows:
  - Section 0-8 listed
  - Progress bars (0% initially)
  - Score, time spent, commands executed
- [ ] Click "Class Overview" tab
- [ ] Select class from dropdown
- [ ] Verify shows class-wide statistics

### Test 7: Student Access Control (CRITICAL INTEGRATION) ⭐
- [ ] Log out from professor account
- [ ] Create a student account OR use test student credentials
- [ ] Log in as student
- [ ] Navigate to dashboard

**Verify Locked Sections:**
- [ ] Section 0 should be UNLOCKED (available)
- [ ] Section 1 should show LOCK ICON 🔒
- [ ] Hover/click Section 1
- [ ] Verify custom message displays: "You must complete Section 0 with 75%..."
- [ ] Section 2 should also be locked
- [ ] Section 3 should be locked with "Available from: [tomorrow's date]"

**Verify Unlocked Section:**
- [ ] Click Section 0
- [ ] Should access without issues
- [ ] Can view exercises and start lab

### Test 8: Class Selector
- [ ] Log back in as professor
- [ ] Navigate to "Lab Settings"
- [ ] If you created multiple classes, switch between them in dropdown
- [ ] Verify settings are different for each class
- [ ] Confirm class-specific configuration works

---

## ✅ Success Criteria

All tests above should pass with:
- ✓ No console errors (F12 → Console)
- ✓ Toast notifications appear for all actions
- ✓ Data persists after page refresh
- ✓ Lab access control enforces prerequisites
- ✓ Student dashboard respects lab settings
- ✓ All CRUD operations work

---

## 🐛 Common Issues & Solutions

**Issue**: Settings don't save
- **Solution**: Check browser console for errors (F12), verify Supabase connection

**Issue**: Student can access locked sections
- **Solution**: Verify lab_settings were saved, check if class_id matches student's class

**Issue**: Prerequisites not working
- **Solution**: Ensure student has completed prerequisite section and achieved passing score

**Issue**: Toast notifications don't appear
- **Solution**: Check if toast component is rendering, verify edge function responses

---

## 📊 What to Report

After testing, please provide:
1. ✅ Which tests passed
2. ❌ Which tests failed (if any)
3. 🐛 Any bugs or unexpected behavior
4. 💡 Suggestions for improvements
5. 📸 Screenshots of any issues

---

## Next Steps After Testing

Once Phase 1 testing is complete:
- **Option A**: Request modifications/fixes for any issues
- **Option B**: Proceed to Phase 2 (Advanced Analytics, Grading, Environment Management)
- **Option C**: Start using the platform with real students and classes
