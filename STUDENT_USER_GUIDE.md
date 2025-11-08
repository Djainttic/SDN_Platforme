# SDN Lab Platform - Student User Guide

**Version**: 1.0  
**Last Updated**: 2025-11-05  
**Platform URL**: https://377u4geo9kkl.space.minimax.io

---

## Table of Contents

1. [Getting Started](#getting-started)
2. [Dashboard Overview](#dashboard-overview)
3. [Lab Interface](#lab-interface)
4. [Working with Containers](#working-with-containers)
5. [Terminal Commands](#terminal-commands)
6. [Network Topology](#network-topology)
7. [Completing Assessments](#completing-assessments)
8. [Tracking Progress](#tracking-progress)
9. [Tips for Success](#tips-for-success)
10. [Troubleshooting](#troubleshooting)

---

## Getting Started

### First Login

1. Navigate to: https://377u4geo9kkl.space.minimax.io
2. Click "Sign In"
3. Enter your student email and password
4. You will be directed to your Student Dashboard

### Password Setup

On first login, you may be asked to change your temporary password:

1. Enter current (temporary) password
2. Create new secure password (minimum 8 characters)
3. Confirm new password
4. Click "Update Password"

**Password Requirements**:
- At least 8 characters
- Include uppercase and lowercase letters
- Include at least one number
- Include at least one special character

### Navigating the Platform

The student interface has the following sections:

- **Dashboard**: Your progress overview and quick access
- **Labs**: Access all 9 lab sections
- **Settings**: Update profile and preferences

---

## Dashboard Overview

### Your Progress

The dashboard displays:

1. **Overall Progress**: Percentage of labs completed
2. **Current Section**: Lab you're currently working on
3. **Achievements**: Badges earned for milestones
4. **Recent Activity**: Your recent lab sessions
5. **Time Spent**: Total hours in lab environment

### Lab Sections

You'll see all 9 SDN lab sections:

| Section | Topic | Status |
|---------|-------|--------|
| 0 | Introduction to SDN | Available |
| 1 | Mininet Basics | Locked (until Section 0 complete) |
| 2 | RYU Controller | Locked |
| 3 | Open vSwitch | Locked |
| 4 | OpenFlow Protocol | Locked |
| 5 | Traffic Analysis | Locked |
| 6 | Custom Topologies | Locked |
| 7 | Controller Applications | Locked |
| 8 | SDN Security | Locked |

Sections unlock sequentially as you complete prerequisites.

### Quick Actions

- **Continue Current Lab**: Resume where you left off
- **View Achievements**: See all earned badges
- **Check Grades**: View assessment scores

---

## Lab Interface

### Opening a Lab Section

1. From Dashboard, click on any unlocked section
2. Lab interface opens with 5 tabs:
   - **Tutorial**: Step-by-step instructions
   - **Network Topology**: Visual network diagram
   - **Terminal**: Interactive command-line interface
   - **Flow Tables**: OpenFlow flow entries
   - **Assessment**: Quiz questions

### Starting a Lab Session

1. Click **Start Lab** button (top right)
2. Wait for container to initialize (5-10 seconds)
3. Session status changes to "Active"
4. Timer begins tracking your session time

### Lab Controls

- **Start Lab**: Begin new session
- **Stop Lab**: End current session (saves progress)
- **Export**: Download lab data and results
- **Fullscreen**: Expand terminal to full screen

---

## Working with Containers

### What are Containers?

Each lab runs in an isolated Docker container that provides:

- **Mininet**: Virtual network environment
- **RYU Controller**: SDN controller software
- **Open vSwitch**: Software-defined switches
- **Network Tools**: ping, tcpdump, iperf, Wireshark

This gives you a complete SDN environment without needing to install anything locally.

### Container Lifecycle

#### Starting a Container

1. Open any lab section
2. Go to **Terminal** tab
3. Click **Start Container**
4. Wait for "Container Running" status
5. Terminal prompt appears when ready

#### Using the Container

Once started, you can:

- Execute SDN commands
- Create network topologies
- Configure switches and controllers
- Analyze traffic
- Test network behaviors

#### Stopping a Container

When finished:

1. Click **Stop Container** button
2. Your work is automatically saved
3. Container resources are freed

**Important**: Containers auto-stop after 60 minutes of inactivity to conserve resources.

---

## Terminal Commands

### Understanding the Terminal

The web-based terminal provides full access to Linux command-line tools and SDN utilities.

### Basic Navigation

```bash
# View current directory
pwd

# List files
ls
ls -la

# Change directory
cd /home/sdn

# View file contents
cat filename.txt

# Clear screen
clear
```

### Mininet Commands

#### Creating Networks

```bash
# Simple 2-host network with 1 switch
sudo mn --topo single,2

# Linear topology with 3 switches
sudo mn --topo linear,3

# Tree topology (depth 2, fanout 2)
sudo mn --topo tree,2,2

# Custom controller (RYU)
sudo mn --controller remote,ip=127.0.0.1,port=6633
```

#### Inside Mininet CLI

```bash
# View network nodes
nodes

# View network links
links

# View network information
net

# Dump node information
dump

# Ping between hosts
h1 ping h2

# Run command on host
h1 ifconfig

# Exit Mininet
exit
```

### RYU Controller Commands

```bash
# Start RYU with simple switch app
ryu-manager ryu.app.simple_switch_13

# Start with GUI
ryu-manager --observe-links ryu.app.simple_switch_13 ryu.app.gui_topology.gui_topology

# Start with OpenFlow 1.3 support
ryu-manager ryu.app.ofctl_rest ryu.app.simple_switch_13

# View RYU applications
ryu-manager --list-apps
```

### Open vSwitch Commands

```bash
# View switch configuration
sudo ovs-vsctl show

# List all switches
sudo ovs-vsctl list-br

# Add a bridge (switch)
sudo ovs-vsctl add-br s1

# Add port to bridge
sudo ovs-vsctl add-port s1 eth0

# View flow tables
sudo ovs-ofctl dump-flows s1

# Add flow entry
sudo ovs-ofctl add-flow s1 in_port=1,actions=output:2

# Delete all flows
sudo ovs-ofctl del-flows s1
```

### Network Analysis Commands

```bash
# Ping test
ping 10.0.0.1
ping -c 5 10.0.0.2

# Bandwidth test with iperf
# On host 1 (server)
iperf -s

# On host 2 (client)
iperf -c 10.0.0.1 -t 10

# Packet capture
sudo tcpdump -i eth0
sudo tcpdump -i any -n host 10.0.0.1

# View network interfaces
ip addr
ifconfig
```

### File Operations

```bash
# Create file
touch myfile.txt

# Edit file (nano editor)
nano myfile.txt

# Save in nano: Ctrl+O, then Enter
# Exit nano: Ctrl+X

# Copy file
cp source.txt destination.txt

# Move/rename file
mv oldname.txt newname.txt

# Delete file
rm filename.txt
```

### Getting Help

```bash
# Command help
man <command>
<command> --help

# Examples:
man ping
sudo mn --help
ryu-manager --help
```

---

## Network Topology

### Viewing the Topology

1. Go to **Network Topology** tab
2. Visual diagram shows:
   - **Controller**: SDN controller (blue circle)
   - **Switches**: OpenFlow switches (squares)
   - **Hosts**: End devices (circles)
   - **Links**: Connections between nodes

### Understanding the Diagram

**Node Types**:
- **Controller**: Central control plane
- **Switch (s1, s2, s3)**: Forwarding devices
- **Host (h1, h2, etc.)**: End devices with IP addresses

**Link Types**:
- **Control Links**: Controller to switches (dashed blue)
- **Data Links**: Between switches and hosts (solid gray)

### Topology Information

Hover over nodes to see:
- Node name and type
- IP address (for hosts)
- DPID (for switches)
- Port numbers
- Status (active/inactive)

### Saving Topology

1. After creating custom topology in Terminal
2. Click **Save Topology** button
3. Snapshot is stored in your session history
4. Can be viewed later from Dashboard

---

## Completing Assessments

### Assessment Overview

Each lab section includes:
- **Quiz Questions**: Multiple choice and true/false
- **Exercise Tasks**: Hands-on practice
- **Lab Reports**: Written analysis (some sections)

### Taking a Quiz

1. Go to **Assessment** tab
2. Read each question carefully
3. Select your answer
4. Click **Next Question**
5. Review answers before submission
6. Click **Submit Assessment**

### Quiz Question Types

**Multiple Choice**:
- Choose one correct answer from options
- Click radio button to select

**True/False**:
- Determine if statement is correct
- Select True or False

**Short Answer** (some sections):
- Type your response in text box
- Be concise and specific

### Viewing Results

After submission:

1. **Score**: Displayed immediately for auto-graded questions
2. **Feedback**: Explanation for each question
3. **Correct Answers**: Shown after submission
4. **Grade**: Added to your overall grade

### Retaking Assessments

- Quizzes can typically be retaken once
- Highest score is recorded
- Check with professor for specific policy

---

## Tracking Progress

### Progress Indicators

Track your advancement through:

1. **Completion Percentage**: Per section and overall
2. **Badges**: Achievement icons for milestones
3. **Time Tracking**: Hours spent per section
4. **Grade**: Current score out of 100%

### Achievement Badges

Earn badges for:

- **First Steps**: Complete Section 0
- **Network Builder**: Create first custom topology
- **Command Master**: Execute 50+ commands
- **Flow Expert**: Configure 10+ flow entries
- **Quiz Champion**: Score 100% on any quiz
- **Lab Completer**: Finish all 9 sections
- **Speed Demon**: Complete section in under 2 hours
- **Perfect Score**: Get 100% overall grade

### Viewing Detailed Progress

1. Go to Dashboard
2. Click **Progress Details**
3. See breakdown:
   - Section completion status
   - Quiz scores
   - Exercise completion
   - Time spent
   - Commands executed
   - Achievements earned

### Progress Requirements

To complete a section:

1. **Read tutorial**: Understand concepts
2. **Complete exercises**: Practice hands-on tasks
3. **Pass assessment**: Score minimum 70% on quiz
4. **Meet time requirement**: Minimum engagement time

---

## Tips for Success

### Before Starting

1. **Read the tutorial thoroughly**: Don't skip ahead
2. **Watch demo videos**: If provided by professor
3. **Set aside enough time**: Each section takes 2-4 hours
4. **Prepare note-taking tools**: Document important commands

### During Labs

1. **Follow instructions step-by-step**: Don't skip steps
2. **Copy commands carefully**: Syntax matters
3. **Read error messages**: They provide clues
4. **Save frequently**: Use Export button
5. **Test your work**: Verify results before proceeding
6. **Ask questions**: Use communication tools if stuck

### Command-Line Best Practices

1. **Use Tab completion**: Type first letters, press Tab
2. **Use Up arrow**: Recall previous commands
3. **Check syntax**: Use --help flag
4. **Start simple**: Test basic commands before complex ones
5. **Read output**: Don't ignore terminal messages

### Time Management

1. **Plan sessions**: Allocate 2-4 hours per section
2. **Take breaks**: Every 45-60 minutes
3. **Don't rush**: Quality over speed
4. **Save progress**: Stop session before deadline
5. **Review before quiz**: Go through tutorial again

### Getting Unstuck

If you encounter problems:

1. **Re-read instructions**: Missed step?
2. **Check command syntax**: Typo?
3. **Restart container**: Technical issue?
4. **Review error message**: What does it say?
5. **Consult reference materials**: Documentation links
6. **Ask professor/TA**: Through messaging system

---

## Troubleshooting

### Common Issues and Solutions

#### Cannot Start Container

**Symptoms**: "Failed to start container" error

**Solutions**:
1. Wait 30 seconds and try again
2. Stop any existing active sessions
3. Refresh the page
4. Clear browser cache
5. Try different browser

#### Terminal Not Responding

**Symptoms**: Commands don't execute, no output

**Solutions**:
1. Wait 10 seconds (might be loading)
2. Click in terminal area to focus
3. Press Enter to get new prompt
4. Restart container if frozen
5. Check internet connection

#### Commands Not Working

**Symptoms**: "Command not found" or permission errors

**Solutions**:
1. Check spelling and syntax
2. Use `sudo` for system commands
3. Ensure you're in correct directory
4. Verify command is available: `which <command>`
5. Read command help: `<command> --help`

#### Quiz Won't Submit

**Symptoms**: Submit button grayed out or unresponsive

**Solutions**:
1. Answer all required questions
2. Check internet connection
3. Refresh page (answers are saved)
4. Try different browser
5. Contact professor if persistent

#### Progress Not Saving

**Symptoms**: Work lost after closing browser

**Solutions**:
1. Click "Stop Lab" before closing
2. Use Export button to save locally
3. Check session timeout (60 min)
4. Verify internet connection during session
5. Don't use incognito/private mode

#### Slow Performance

**Symptoms**: Platform laggy or unresponsive

**Solutions**:
1. Close other browser tabs
2. Check internet speed (need 5+ Mbps)
3. Disable browser extensions
4. Use recommended browsers
5. Restart browser

### Error Messages

#### "Session Expired"

**Meaning**: Container stopped due to inactivity

**Action**: Start new session, previous work is saved

#### "Resource Limit Exceeded"

**Meaning**: Too many containers running

**Action**: Stop containers from other sections first

#### "Authentication Failed"

**Meaning**: Login session ended

**Action**: Sign in again, work is saved

#### "Network Error"

**Meaning**: Lost connection to server

**Action**: Check internet, refresh page

### Getting Help

#### Self-Service Resources

1. Read this guide thoroughly
2. Check professor's announcements
3. Review tutorial instructions
4. Consult SDN documentation links

#### Asking for Help

When contacting professor/TA:

1. **Describe the problem**: What happened?
2. **Include error messages**: Copy exact text
3. **State what you tried**: Troubleshooting steps
4. **Provide context**: Which section? Which step?
5. **Include screenshot**: If visual issue

#### Emergency Contact

For critical platform issues:

1. Document the problem
2. Note date/time it occurred
3. List your actions before issue
4. Contact system administrator
5. Use backup resources if needed

---

## Appendix

### Keyboard Shortcuts

**Terminal**:
- **Ctrl + C**: Cancel current command
- **Ctrl + D**: Exit/logout
- **Ctrl + L**: Clear screen
- **Up Arrow**: Previous command
- **Tab**: Auto-complete

**Platform**:
- **Alt + D**: Go to Dashboard
- **Alt + L**: Go to Labs
- **F11**: Fullscreen terminal

### Command Reference Card

**Mininet**:
```bash
sudo mn --topo single,2        # Simple topology
nodes                          # Show nodes
links                          # Show links
h1 ping h2                     # Ping test
exit                           # Exit Mininet
```

**Open vSwitch**:
```bash
sudo ovs-vsctl show            # Show config
sudo ovs-ofctl dump-flows s1   # Show flows
sudo ovs-ofctl add-flow s1 ... # Add flow
```

**RYU**:
```bash
ryu-manager app.py             # Start controller
ryu-manager --list-apps        # List apps
```

**Network Tools**:
```bash
ping <ip>                      # Connectivity test
ifconfig                       # Network interfaces
ip addr                        # IP addresses
tcpdump -i eth0               # Packet capture
```

### System Requirements

**Browser**:
- Chrome 90+ (recommended)
- Firefox 88+
- Safari 14+
- Edge 90+

**Internet**:
- Minimum: 5 Mbps
- Recommended: 10+ Mbps
- Stable connection required

**Display**:
- Minimum: 1280x720
- Recommended: 1920x1080 or higher

### Lab Section Summary

| Section | Time | Difficulty | Prerequisites |
|---------|------|------------|---------------|
| 0 | 2-3h | Beginner | None |
| 1 | 2-4h | Beginner | Section 0 |
| 2 | 3-4h | Intermediate | Section 1 |
| 3 | 3-4h | Intermediate | Section 2 |
| 4 | 3-5h | Intermediate | Section 3 |
| 5 | 2-3h | Intermediate | Section 4 |
| 6 | 4-5h | Advanced | Section 5 |
| 7 | 4-6h | Advanced | Section 6 |
| 8 | 3-5h | Advanced | Section 7 |

**Total Estimated Time**: 25-35 hours for complete course

### Assessment Grading

**Grade Components**:
- Tutorial Completion: 20%
- Exercise Tasks: 30%
- Quiz Scores: 40%
- Lab Reports: 10%

**Grading Scale**:
- A: 90-100%
- B: 80-89%
- C: 70-79%
- D: 60-69%
- F: Below 60%

### Frequently Asked Questions

**Q: Can I skip sections?**  
A: No, sections must be completed sequentially due to prerequisites.

**Q: How many times can I retake a quiz?**  
A: Typically once. Check with your professor for specific policy.

**Q: What if my container crashes?**  
A: Start a new session. Your progress is saved automatically.

**Q: Can I work on multiple sections at once?**  
A: Yes, but only one container can run at a time per student.

**Q: How long do I have to complete the course?**  
A: Check with your professor for deadlines. Typically one semester.

**Q: Are there practice exercises?**  
A: Yes, each section includes multiple practice exercises before assessment.

**Q: Can I collaborate with classmates?**  
A: Check your professor's collaboration policy. Generally, discussions are OK but submit your own work.

**Q: What if I lose internet connection during a lab?**  
A: Your session will be saved. Reconnect and continue where you left off.

---

**End of Student User Guide**

For additional assistance, refer to the Professor User Guide, Docker Setup Guide, and Troubleshooting Guide.

**Platform Version**: 1.0  
**Last Updated**: 2025-11-05  
**Document Version**: 1.0

---

**Good luck with your SDN learning journey!**
