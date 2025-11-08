# SDN Lab Platform - Professor User Guide

**Version**: 1.0  
**Last Updated**: 2025-11-05  
**Platform URL**: https://377u4geo9kkl.space.minimax.io

---

## Table of Contents

1. [Getting Started](#getting-started)
2. [Dashboard Overview](#dashboard-overview)
3. [Class Management](#class-management)
4. [Student Management](#student-management)
5. [Lab Content Management](#lab-content-management)
6. [Grading System](#grading-system)
7. [Analytics & Reports](#analytics--reports)
8. [Container Environment Management](#container-environment-management)
9. [Communication Tools](#communication-tools)
10. [Advanced Features](#advanced-features)
11. [Best Practices](#best-practices)
12. [Troubleshooting](#troubleshooting)

---

## Getting Started

### First Login

1. Navigate to: https://377u4geo9kkl.space.minimax.io
2. Click "Sign In"
3. Enter your professor credentials
4. You will be directed to the Professor Dashboard

### Dashboard Navigation

The professor interface is organized into the following sections:

- **Dashboard**: Overview of all classes and student progress
- **Classes**: Manage your classes and enrollments
- **Students**: View and manage student accounts
- **Labs**: Manage lab content, sections, and exercises
- **Grading**: Review submissions and assign grades
- **Analytics**: View detailed performance metrics
- **Environment**: Monitor and manage lab containers
- **Reports**: Generate and export data reports
- **Communications**: Announcements and messaging
- **Settings**: Configure lab parameters and preferences

---

## Dashboard Overview

### Key Metrics

The dashboard displays:

1. **Active Classes**: Number of classes currently running
2. **Total Students**: Enrolled students across all classes
3. **Active Lab Sessions**: Students currently working in labs
4. **Average Progress**: Overall completion percentage
5. **Recent Activity**: Timeline of student actions

### Quick Actions

- **Start New Class**: Create a new class for the semester
- **View All Students**: Access student management panel
- **Check Active Sessions**: Monitor real-time lab usage
- **Generate Report**: Create analytics reports

### Progress Visualization

- **Class Progress Chart**: Bar chart showing completion rates per class
- **Section Completion Heatmap**: Visual representation of student progress across 9 lab sections
- **Time Analytics**: Average time spent per section

---

## Class Management

### Creating a New Class

1. Navigate to **Classes** section
2. Click **Add Class** button
3. Fill in required information:
   - **Class Name**: e.g., "SDN Fundamentals Fall 2025"
   - **Class Code**: Unique identifier (e.g., "CS401-F25")
   - **Semester**: Current academic term
   - **Start Date**: First day of class
   - **End Date**: Last day of class
   - **Description**: Course overview (optional)
4. Click **Create Class**

### Managing Enrollments

#### Add Students to Class

1. Open the class details
2. Click **Enroll Students** tab
3. Choose enrollment method:
   - **Manual**: Enter student email addresses
   - **Bulk Upload**: Upload CSV file with student data
   - **Self-Enrollment**: Share class code with students

#### Remove Students

1. Go to class roster
2. Select student(s) to remove
3. Click **Remove from Class**
4. Confirm the action

### Class Settings

Configure class-specific parameters:

- **Prerequisites**: Required prior knowledge or completed sections
- **Grading Scheme**: Define grade calculation method
- **Deadlines**: Set due dates for lab sections
- **Access Control**: Enable/disable specific lab sections
- **Resource Limits**: Set container resource allocation per student

---

## Student Management

### Student Overview

The Student Management page displays:

- Student name and email
- Enrollment status
- Overall progress percentage
- Last activity timestamp
- Achievement badges earned

### Individual Student Details

Click on any student to view:

1. **Progress Report**: Completion status for all 9 sections
2. **Lab Sessions**: History of lab activity
3. **Assessment Scores**: Quiz and exercise results
4. **Time Tracking**: Hours spent on each section
5. **Container Usage**: Resource consumption metrics
6. **Command History**: Commands executed in terminals (for debugging)

### Student Actions

#### Reset Password

1. Select student from list
2. Click **Reset Password**
3. System generates temporary password
4. Student will be prompted to change on next login

#### Reset Progress

1. Open student details
2. Navigate to specific section
3. Click **Reset Section Progress**
4. Confirm to clear completion data

#### Extend Deadline

1. Go to student's progress page
2. Select section with deadline
3. Click **Extend Deadline**
4. Choose new due date

---

## Lab Content Management

### Lab Structure

The platform includes 9 comprehensive SDN lab sections:

0. **Introduction to SDN**: Basic concepts and architecture
1. **Mininet Basics**: Virtual network creation
2. **RYU Controller**: SDN controller programming
3. **Open vSwitch**: Switch configuration and management
4. **OpenFlow Protocol**: Protocol deep dive
5. **Traffic Analysis**: Network monitoring with Wireshark
6. **Custom Topologies**: Advanced network design
7. **Controller Applications**: Building SDN apps
8. **SDN Security**: Security best practices

### Viewing Lab Content

1. Navigate to **Labs** section
2. Select a section (0-8)
3. View components:
   - **Tutorial**: Step-by-step instructions
   - **Exercises**: Hands-on practice tasks
   - **Quiz Questions**: Assessment items
   - **Student Progress**: Completion statistics

### Editing Exercises

1. Go to **Content Editor** page
2. Select section to edit
3. Choose **Exercises** tab
4. Click **Edit** on existing exercise or **Add New**
5. Modify fields:
   - Exercise title
   - Description
   - Instructions
   - Expected output
   - Difficulty level
   - Points value
6. Click **Save Changes**

### Managing Quiz Questions

1. In Content Editor, select **Quiz Questions** tab
2. Add/edit questions:
   - Question text
   - Question type (multiple choice, true/false, short answer)
   - Answer options
   - Correct answer
   - Points
   - Explanation
3. Questions are automatically integrated into assessment system

### Tutorial Content

Tutorial content (learning objectives and step-by-step guides) is embedded in the frontend code. To modify:

- Contact system administrator for code updates
- File location: `src/components/LabTutorial.tsx`

---

## Grading System

### Automated Grading

The system automatically grades:

- **Quiz Submissions**: Multiple choice and true/false questions
- **Exercise Completion**: Based on predefined criteria
- **Command Accuracy**: Correct syntax and execution

### Manual Review

For subjective assessments:

1. Navigate to **Grading** section
2. View **Pending Reviews** queue
3. Select student submission
4. Review:
   - Student's code/commands
   - Terminal output
   - Network topology created
   - Flow table entries
5. Assign score and feedback
6. Click **Submit Grade**

### Grading Rules

Create automated grading rules:

1. Go to **Grading Rules** tab
2. Click **Add Rule**
3. Configure:
   - Section number
   - Criteria (completion percentage, quiz score, exercise count)
   - Point allocation
   - Weight in final grade
4. Save rule

### Grade Export

Export grades for external systems:

1. Select class
2. Click **Export Grades**
3. Choose format:
   - **CSV**: For spreadsheet software
   - **PDF**: For printing/archiving
4. Download file

### Grade Distribution

View statistical analysis:

- Bar chart showing grade distribution
- Average, median, and standard deviation
- Comparison across sections
- Trend analysis over time

---

## Analytics & Reports

### Advanced Analytics Dashboard

Access comprehensive metrics:

1. Navigate to **Analytics** section
2. View dashboards:
   - **Progress Heatmap**: Visual completion matrix
   - **Time Analysis**: Average time per section
   - **Error Patterns**: Common command mistakes
   - **Engagement Metrics**: Login frequency, session duration
   - **Success Prediction**: ML-based at-risk student identification

### ML-Powered Insights

The platform uses machine learning to provide:

- **Early Warning System**: Identifies students at risk of falling behind
- **Success Prediction**: Likelihood of course completion
- **Content Effectiveness**: Which sections students struggle with most
- **Personalized Recommendations**: Suggested interventions

### Custom Reports

Build custom reports:

1. Go to **Custom Report Builder**
2. Select report type:
   - Student progress report
   - Grade distribution report
   - Analytics summary
3. Choose filters:
   - Date range
   - Specific class
   - Section numbers
   - Student group
4. Select data fields to include
5. Generate report

### Scheduled Reports

Automate report generation:

1. Navigate to **Reports** > **Scheduled**
2. Click **Create Schedule**
3. Configure:
   - Report type
   - Frequency (daily, weekly, monthly)
   - Recipients (email list)
   - Format (CSV/PDF)
4. Save schedule

Reports are automatically generated and emailed according to schedule.

---

## Container Environment Management

### Overview

Each lab section runs in an isolated Docker container providing:

- **Mininet**: Network emulation
- **RYU Controller**: SDN controller
- **Open vSwitch**: Software-defined switch
- **Traffic Tools**: Wireshark, tcpdump, iperf
- **Security Tools**: For SDN security labs

### Monitoring Active Sessions

View real-time container usage:

1. Navigate to **Environment Management**
2. See active sessions:
   - Student name
   - Section number
   - Container status (running/stopped)
   - Resource usage (CPU, memory, network)
   - Duration
3. Sort by various metrics

### Managing Containers

#### Stop Individual Container

1. Find student's active session
2. Click **Stop Container**
3. Confirm action
4. Container is gracefully terminated

#### Bulk Actions

1. Select multiple sessions
2. Choose action:
   - **Stop Selected**: Terminate multiple containers
   - **Extend Time**: Add time before auto-cleanup
   - **View Logs**: Check container output

### Resource Monitoring

Track infrastructure usage:

- **CPU Utilization**: Total and per-container
- **Memory Usage**: Available vs. consumed
- **Network Traffic**: Bandwidth usage
- **Disk I/O**: Container storage metrics
- **Active Connections**: Network socket count

### Configuration

Adjust container parameters:

1. Go to **Environment Settings**
2. Modify:
   - **Resource Limits**: CPU, memory per container
   - **Session Timeout**: Auto-cleanup after inactivity
   - **Max Concurrent Sessions**: Per student limit
   - **Network Isolation**: Security settings
3. Apply changes

---

## Communication Tools

### Announcements

Broadcast messages to all students:

1. Navigate to **Communications**
2. Click **New Announcement**
3. Compose message:
   - Subject line
   - Message body (supports formatting)
   - Priority level (normal/urgent)
   - Target audience (all/specific class)
4. Choose delivery:
   - **Immediate**: Send now
   - **Scheduled**: Set future date/time
5. Click **Send**

### Direct Messaging

Send private messages:

1. Go to **Messages** tab
2. Click **New Message**
3. Select recipient(s)
4. Write message
5. Click **Send**

### Automated Reminders

Configure automatic notifications:

1. Navigate to **Reminder Settings**
2. Create reminder rules:
   - **Deadline Approaching**: 1-3 days before due date
   - **Incomplete Section**: After X days of inactivity
   - **Low Performance**: Quiz score below threshold
3. Customize message template
4. Enable reminder

### Message History

View communication log:

- All sent announcements
- Direct message threads
- Student responses
- Automated reminder records

---

## Advanced Features

### Teaching Assistant Management

Delegate responsibilities to TAs:

1. Navigate to **TA Management**
2. Click **Add TA**
3. Enter TA email
4. Assign permissions:
   - **Can Grade**: Review and grade submissions
   - **Can Edit Content**: Modify exercises/quizzes
   - **Can View Analytics**: Access reports
   - **Can Message Students**: Send communications
5. Save TA profile

### Peer Review System

Enable student peer reviews:

1. Go to **Peer Reviews** section
2. Configure peer review settings:
   - Number of reviews per student
   - Review deadline
   - Rubric criteria
   - Anonymous/Named reviews
3. Assign review pairs
4. Monitor review submissions
5. View review quality metrics

### LMS Integration

Connect to external Learning Management Systems:

1. Navigate to **LMS Integration**
2. Select LMS type:
   - Canvas
   - Blackboard
   - Moodle
3. Configure connection:
   - LMS URL
   - API credentials (OAuth)
   - Sync settings
4. Map course data
5. Enable automatic grade sync

### Custom Lab Settings

Create customized lab configurations:

1. Go to **Lab Settings**
2. For each section, configure:
   - **Prerequisites**: Required sections
   - **Difficulty Level**: Beginner to Advanced
   - **Time Estimates**: Expected completion time
   - **Container Type**: Mininet, RYU, OVS, etc.
   - **Available Commands**: Command whitelist
   - **Reference Materials**: Links to documentation

---

## Best Practices

### Class Setup

1. **Create class early**: Set up at least 1 week before semester starts
2. **Configure deadlines**: Align with academic calendar
3. **Test environment**: Run through labs yourself before student access
4. **Prepare materials**: Ensure all content is reviewed and accurate

### Student Onboarding

1. **Send welcome email**: Include login instructions and platform overview
2. **Host orientation**: Live demo of platform features
3. **Share resources**: Link to student user guide
4. **Set expectations**: Communicate grading criteria and deadlines

### Monitoring Progress

1. **Check weekly**: Review analytics dashboard regularly
2. **Identify struggling students**: Use ML early warning system
3. **Provide timely feedback**: Respond to questions within 24 hours
4. **Celebrate success**: Acknowledge achievements and badges

### Grading Strategy

1. **Establish clear rubrics**: Define grading criteria upfront
2. **Use automated grading**: Let system handle objective assessments
3. **Focus on quality**: Manual review for complex exercises
4. **Provide feedback**: Use comments to guide student improvement

### Resource Management

1. **Monitor usage**: Check environment dashboard daily
2. **Set limits**: Prevent resource exhaustion
3. **Schedule maintenance**: Plan downtime during low-usage periods
4. **Clean up**: Regularly remove old sessions and data

---

## Troubleshooting

### Common Issues

#### Students Cannot Access Labs

**Problem**: Student reports "Access Denied" error

**Solutions**:
1. Verify student is enrolled in class
2. Check if section is unlocked
3. Ensure student completed prerequisites
4. Verify account is active (not suspended)

#### Container Won't Start

**Problem**: Terminal shows "Failed to start container"

**Solutions**:
1. Check Docker host is configured (see Docker Setup Guide)
2. Verify resource limits aren't exceeded
3. Check for existing containers for that student
4. Review container logs in Environment Management

#### Quiz Scores Not Calculating

**Problem**: Grades show as 0 despite correct answers

**Solutions**:
1. Ensure grading rules are configured
2. Check quiz question answer keys are set
3. Verify student submitted (not just saved) quiz
4. Re-calculate grades using "Recalculate" button

#### Slow Performance

**Problem**: Platform is slow or unresponsive

**Solutions**:
1. Check number of active containers (reduce if high)
2. Review resource usage in Environment Management
3. Close inactive sessions
4. Clear browser cache
5. Contact system administrator if persistent

### Getting Help

#### Support Resources

1. **User Guide**: This document
2. **Student User Guide**: For student-facing issues
3. **Docker Setup Guide**: For container configuration
4. **Troubleshooting Guide**: Detailed problem resolution
5. **API Documentation**: For technical integrations

#### Contact Support

For issues not resolved through guides:

1. Document the problem:
   - What you were trying to do
   - Error messages received
   - Steps to reproduce
   - Browser and version
   - Screenshots if applicable
2. Check Supabase function logs (if technical)
3. Contact system administrator with documentation

---

## Appendix

### Keyboard Shortcuts

- **Dashboard**: Alt + D
- **Classes**: Alt + C
- **Students**: Alt + S
- **Labs**: Alt + L
- **Grading**: Alt + G
- **Analytics**: Alt + A

### System Requirements

**Supported Browsers**:
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

**Recommended**:
- Screen resolution: 1920x1080 or higher
- Stable internet connection (5 Mbps+)
- JavaScript enabled
- Cookies enabled

### Platform Updates

The platform is continuously improved. Major updates include:

- New lab sections and content
- Enhanced analytics features
- Performance optimizations
- Security enhancements
- UI improvements

Check the platform changelog for detailed update notes.

---

## Quick Reference

### Section Numbers and Topics

| Section | Topic |
|---------|-------|
| 0 | Introduction to SDN |
| 1 | Mininet Basics |
| 2 | RYU Controller |
| 3 | Open vSwitch |
| 4 | OpenFlow Protocol |
| 5 | Traffic Analysis |
| 6 | Custom Topologies |
| 7 | Controller Applications |
| 8 | SDN Security |

### Container Types

| Type | Description | Sections |
|------|-------------|----------|
| mininet | Network emulation | 0, 1, 4, 6 |
| ryu | RYU controller | 2, 7 |
| ovs | Open vSwitch | 3 |
| traffic-analyzer | Traffic tools | 5 |
| security-lab | Security tools | 8 |

### Grading Components

| Component | Weight | Auto-Graded |
|-----------|--------|-------------|
| Quiz Questions | 30% | Yes |
| Exercise Completion | 40% | Partial |
| Manual Review | 20% | No |
| Lab Reports | 10% | No |

---

**End of Professor User Guide**

For additional assistance, refer to the Student User Guide, Docker Setup Guide, and Troubleshooting Guide.

**Platform Version**: 1.0  
**Last Updated**: 2025-11-05  
**Document Version**: 1.0
