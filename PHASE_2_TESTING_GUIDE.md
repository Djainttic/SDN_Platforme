# Phase 2 Testing Quick Reference

## Access Information
- **URL**: https://pwzmsj4en5im.space.minimax.io
- **Professor Account**: jgyzqdwm@minimax.com / 29AttRMrtU

## Phase 2 Features Testing Checklist

### 1. Advanced Analytics Dashboard
**URL**: `/professor/analytics`

**Test Steps**:
1. Login with professor account
2. Navigate to Analytics from sidebar
3. Select a class from dropdown
4. Verify these sections load:
   - Section Completion Rates (with progress bars)
   - Time-to-Complete Analysis (table)
   - Class Progress Heatmap (color-coded grid)
   - Command Error Patterns (with section selector)
   - Engagement Metrics (3 stat cards)

**Expected Results**:
- Page loads without errors
- All sections display data or "No data" messages
- Heatmap shows color coding (green/yellow/red/gray)
- Error patterns change when selecting different sections

### 2. Grading System
**URL**: `/professor/grading`

**Test Steps**:
1. Navigate to Grading from sidebar
2. Select a class from dropdown
3. Verify these elements:
   - "Add Grading Rule" button
   - "Export CSV" button
   - Grading Rules section
   - Gradebook table with students
4. Click "Add Grading Rule" button
5. Verify dialog opens with form fields:
   - Rule Name
   - Rule Type (dropdown)
   - Section (dropdown)
   - Points Allocated
6. Click "Export CSV" button
7. Verify CSV download starts

**Expected Results**:
- Page loads with all UI elements
- Dialogs open and close properly
- CSV export triggers download

### 3. Environment Management
**URL**: `/professor/environment`

**Test Steps**:
1. Navigate to Environment from sidebar
2. Select a class from dropdown
3. Verify these sections:
   - Active Sessions section (may be empty)
   - Refresh button
   - View History button
4. Click "View History" button
5. Verify session history table appears

**Expected Results**:
- Page loads without errors
- Active sessions display or show "No active sessions"
- History table loads when button clicked
- Reset/Terminate buttons visible on session cards

### 4. Reporting System
**URL**: `/professor/reports`

**Test Steps**:
1. Navigate to Reports from sidebar
2. Verify three tabs are visible:
   - Generate Reports
   - Report History
   - Scheduled Reports
3. On "Generate Reports" tab, verify 3 report cards:
   - Progress Report (blue button)
   - Grade Report (green button)
   - Analytics Report (purple button)
4. Click "Progress Report" Generate button
5. Verify CSV download starts
6. Switch to "Report History" tab
7. Verify table loads with report metadata
8. Switch to "Scheduled Reports" tab
9. Click "Create Schedule" button
10. Verify dialog opens with form

**Expected Results**:
- All tabs switch correctly
- Report generation triggers CSV download
- History table displays past reports
- Schedule dialog opens with form fields

## Navigation Testing

**Test Steps**:
1. Login as professor
2. Verify sidebar shows these menu items:
   - Dashboard
   - Students
   - Classes
   - Progress
   - Content Editor
   - Lab Settings
   - Analytics (NEW)
   - Grading (NEW)
   - Environment (NEW)
   - Reports (NEW)
3. Click each Phase 2 menu item
4. Verify correct page loads

**Expected Results**:
- All 4 new menu items visible
- Icons display correctly (TrendingUp, Award, Server, FileText)
- Pages load without errors
- Active menu item highlights

## Browser Console Testing

**Test Steps**:
1. Open browser DevTools (F12)
2. Go to Console tab
3. Visit each Phase 2 page
4. Check for JavaScript errors

**Expected Results**:
- No red error messages
- Only normal API calls logged
- No 404 or 500 HTTP errors

## Responsive Design Testing

**Test Steps**:
1. On each Phase 2 page, resize browser window
2. Test desktop (1920px), tablet (768px), mobile (375px)

**Expected Results**:
- Layouts adapt to screen size
- No horizontal scroll
- Buttons and text remain readable
- Tables scroll horizontally if needed

## Data Flow Testing

**Test Steps**:
1. On Analytics page, change class selector
2. Verify data updates for new class
3. On Grading page, change class selector
4. Verify gradebook updates

**Expected Results**:
- Loading indicators show during data fetch
- Data updates reflect selected class
- No stale data displayed

## API Integration Testing

**Test Steps**:
1. Open browser DevTools Network tab
2. Visit Analytics page
3. Verify API calls to:
   - /functions/v1/analytics-dashboard
4. Visit Grading page
5. Verify API calls to:
   - /functions/v1/grading-system
6. Visit Environment page
7. Verify API calls to:
   - /functions/v1/environment-management
8. Visit Reports page and generate report
9. Verify API calls to:
   - /functions/v1/report-generator

**Expected Results**:
- All API calls return 200 status (or 401 if not logged in)
- Response contains expected data structure
- Authentication headers sent correctly

## Edge Cases Testing

**Test Scenarios**:
1. **Empty State**: Select a class with no students
   - Verify appropriate "No data" messages
2. **Large Dataset**: Select a class with many students
   - Verify pagination or scrolling works
3. **Quick Navigation**: Rapidly click between pages
   - Verify no race conditions or errors
4. **Session Timeout**: Wait 30+ minutes, then interact
   - Verify redirect to login or token refresh

## Manual Verification Checklist

- [ ] All 4 Phase 2 pages accessible
- [ ] Navigation menu shows 4 new items
- [ ] Analytics displays multiple data sections
- [ ] Grading shows gradebook and rules
- [ ] Environment shows sessions
- [ ] Reports has 3 tabs
- [ ] CSV export works on Reports
- [ ] CSV export works on Grading
- [ ] Dialogs open and close properly
- [ ] No JavaScript console errors
- [ ] API calls successful
- [ ] Responsive design works
- [ ] Class selector updates data
- [ ] Empty states display properly
- [ ] Loading indicators show
- [ ] Logout works from all pages

## Known Testing Limitations

1. **Automated Browser Testing**: Browser testing tools currently unavailable
2. **Live Data**: Testing depends on existing data in database
3. **Scheduled Reports**: Cron execution not yet implemented
4. **Resource Metrics**: Real-time monitoring requires active sessions

## Manual Testing Recommendation

Due to browser testing tool limitations, manual testing is recommended:

1. Open https://pwzmsj4en5im.space.minimax.io in Chrome/Firefox
2. Login with test account
3. Follow checklist above
4. Take screenshots of each Phase 2 page
5. Document any issues found

## Success Criteria

Phase 2 testing is considered successful if:
- All 4 pages load without errors
- Navigation works correctly
- UI elements display properly
- API calls return data
- CSV exports download
- No critical JavaScript errors
- Responsive design functional

---

**Testing Date**: 2025-11-03
**Deployment URL**: https://pwzmsj4en5im.space.minimax.io
**Test Account**: jgyzqdwm@minimax.com / 29AttRMrtU
