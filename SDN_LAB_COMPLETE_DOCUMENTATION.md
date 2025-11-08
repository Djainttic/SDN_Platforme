# SDN Interactive Learning Platform: Complete Documentation

## Executive Summary

This document provides comprehensive documentation for the Software-Defined Networking (SDN) Interactive Learning Platform, a complete educational ecosystem for students, instructors, and administrators. The platform delivers a hands-on, end-to-end curriculum covering foundational SDN concepts to advanced security applications. It integrates a real-time command execution engine, interactive web-based tutorials, automated assessments, and a complete suite of SDN tools, including Mininet, Ryu, and Open vSwitch.

This manual covers the platform’s architecture, installation and setup procedures, a complete lab manual for all nine curriculum sections, user guides for both students and instructors, a detailed technical reference, and advanced topics for further research. It is designed to be the single source of truth for all aspects of the platform, ensuring a consistent, high-quality learning experience.

---

## 1. Platform Overview & Architecture

The SDN Interactive Learning Platform is a fully integrated, web-based educational tool designed to provide a hands-on, immersive learning experience in Software-Defined Networking. It combines a comprehensive curriculum with a real-time, interactive lab environment, allowing students to bridge the gap between theory and practice.

### 1.1. System Architecture and Components

The platform is built on a modern, decoupled architecture consisting of a frontend web application and a backend powered by serverless functions. This design ensures scalability, security, and a seamless user experience.

-   **Frontend Web Platform**: A responsive React-based application that serves as the main user interface. It provides students with access to the curriculum, interactive terminal, network visualizations, and assessment system.
-   **Backend Services**: A set of Supabase Edge Functions that provide the core logic for command execution, controller management, assessments, and progress tracking. This serverless architecture allows for a secure and scalable execution environment.
-   **SDN Lab Environment**: A containerized environment running the necessary SDN tools, including Mininet for network emulation, Open vSwitch (OVS) for virtual switching, and the Ryu controller for network control. This environment is managed by the backend and provides the real-time, hands-on experience for students.

### 1.2. Technology Stack

The platform utilizes a modern, robust technology stack:

-   **Frontend**:
    -   React 18 + TypeScript
    -   Vite for building and development
    -   TailwindCSS for styling
    -   Chart.js for data visualization
    -   Xterm.js for the interactive terminal
-   **Backend**:
    -   Supabase for database and authentication
    -   Supabase Edge Functions (Deno) for serverless logic
-   **SDN Environment**:
    -   Docker and Docker Compose for containerization
    -   Mininet for network emulation
    -   Open vSwitch for virtual switching
    -   Ryu SDN Controller

### 1.3. User Roles and Access Levels

The platform is designed with two primary user roles in mind:

-   **Student**: The primary user of the platform. Students have access to the dashboard, all nine curriculum sections, the interactive lab environment, and the assessment system. They can track their progress, complete labs, and take quizzes.
-   **Instructor/Administrator**: Has access to all student features, plus additional administrative capabilities. Instructors can monitor student progress, manage lab environments, customize curriculum content, and view assessment results.

---

## 2. Installation & Setup Guide

This section provides a comprehensive guide for setting up the SDN Lab Platform. The platform is designed to be deployed in a containerized environment using Docker, ensuring a consistent and reproducible setup.

### 2.1. Prerequisites and System Requirements

-   **Docker and Docker Compose**: Ensure that Docker and Docker Compose are installed on the host machine.
-   **Operating System**: A modern Linux distribution is recommended (e.g., Ubuntu 20.04 or later).
-   **Hardware**:
    -   Minimum 8GB RAM
    -   Minimum 4 CPU cores
    -   Minimum 20GB of free disk space

### 2.2. Docker Environment Setup

The entire SDN Lab Platform is orchestrated using Docker Compose. The `docker-compose.yml` file, located in the root of the `sdn_lab` directory, defines all the services required for the platform to run, including the Mininet container, the Ryu controller, and any other necessary components.

To start the environment, navigate to the `sdn_lab` directory and run:
```bash
docker-compose up -d
```

### 2.3. SDN Lab Container Deployment

The `docker-compose.yml` file defines the services for the key SDN components:

-   **Mininet**: The primary container for network emulation. It includes all the necessary scripts and tools for the lab exercises.
-   **Ryu Controller**: A dedicated container for the Ryu SDN controller.
-   **Open vSwitch**: Integrated within the Mininet container to provide virtual switching capabilities.

### 2.4. Configuration for Single VM and Dual VM Setups

The platform supports both single and dual virtual machine (VM) setups, providing flexibility for different deployment scenarios. Configuration files for each setup are located in the `sdn_lab/config/` directory.

-   **Single VM Setup**: In this configuration, the controller and Mininet run on the same VM. This is the default and simplest setup, ideal for individual learning and development. The `single-vm.conf` file contains the necessary settings.
-   **Dual VM Setup**: This setup mirrors a more realistic production environment, with the controller running on a separate VM from the Mininet topology. The `dual-vm.conf` file provides the configuration for this scenario, requiring proper networking between the two VMs.

### 2.5. Troubleshooting Common Setup Issues

| Symptom | Likely Cause | Diagnostic Steps | Fix |
|---|---|---|---|
| Docker container fails to start | Port conflict or insufficient resources | `docker logs <container_name>` | Free up the conflicting port or allocate more system resources. |
| Mininet cannot connect to controller | Incorrect IP address or port; controller not running | Check controller logs; verify IP and port in config file. | Ensure the controller is running and the correct IP/port is configured. |
| Commands fail in terminal | Permission issues or incorrect environment | `ls -l` to check permissions; `env` to check variables. | Adjust file permissions; ensure environment variables are set correctly. |


---

## 3. Complete Lab Manual (Sections 0-8)

This section provides a detailed, step-by-step manual for all nine sections of the SDN curriculum. Each section includes learning objectives, hands-on exercises with verification steps, and troubleshooting guidance.

### Section 0: Environment Setup

**Learning Objectives:**
- Understand the role of the loopback interface and process management.
- Apply static IP addressing to connect two virtual machines.
- Analyze logs to confirm operational status and diagnose connection failures.
- Evaluate the impact of timing and port numbers on controller-switch connectivity.

**Lab Steps:**
1.  **Tool Verification**: Verify the installation of Mininet, Ryu, and Open vSwitch.
2.  **Single-VM Controller Setup**: Start the Ryu controller in a single-VM setup.
3.  **Remote Controller Connection**: Launch Mininet and connect to the local Ryu controller.
4.  **Dual-VM Configuration**: Configure a dual-VM setup with a remote controller.
5.  **Connection Validation**: Test connectivity between Mininet and the remote controller.
6.  **Flow Inspection**: Use `ovs-ofctl` to inspect the flow tables.
7.  **Troubleshooting**: Practice common troubleshooting procedures, such as resolving port conflicts.

### Section 1: Introduction to SDN Tools

**Learning Objectives:**
- Understand the difference between emulation and simulation.
- Apply Mininet CLI commands to explore topology and test connectivity.
- Analyze command outputs to confirm state and diagnose errors.
- Create a personalized command cheatsheet.

**Lab Steps:**
1.  **Mininet CLI Exploration**: Use commands like `nodes`, `net`, and `dump`.
2.  **Connectivity Testing**: Run `pingall` to test reachability.
3.  **Performance Testing**: Use `iperf` to measure bandwidth between hosts.
4.  **Link Failure Simulation**: Practice bringing links up and down.
5.  **Network Diagnostics**: Use Mininet CLI to diagnose connectivity issues.
6.  **Topology Cleanup**: Learn to use `mn -c` to clean up network states.

### Section 2: Controller & Data Plane Connection

**Learning Objectives:**
- Understand Ryu's component-based architecture.
- Apply the `simple_switch_13` app to a minimal topology.
- Analyze controller logs and flow tables to understand reactive forwarding.

**Lab Steps:**
1.  **Controller Startup**: Start the Ryu controller with the `simple_switch_13` application.
2.  **Mininet-Controller Connection**: Connect a Mininet topology to the Ryu controller.
3.  **OpenFlow Handshake Verification**: Observe the OpenFlow handshake in the controller logs.
4.  **Reactive Flow Observation**: Watch as flows are reactively installed after a `pingall`.
5.  **Flow Table Inspection**: Use `ovs-ofctl dump-flows` to see the installed flows.

### Section 3: Deep Dive into Open vSwitch

**Learning Objectives:**
- Understand the roles of `ovs-vsctl`, `ovs-ofctl`, and `ovs-dpctl`.
- Manually install flow rules for L2, L3, and L4 matching.
- Analyze the impact of ARP handling on L3 reachability.

**Lab Steps:**
1.  **Switch Capabilities Inspection**: Use `ovs-ofctl show` to see switch features.
2.  **Manual Flow Installation**: Use `ovs-ofctl add-flow` to manually insert flows.
3.  **L2 MAC-based Forwarding**: Create flows for MAC-based forwarding.
4.  **ARP Handling**: Implement flows to handle ARP requests.
5.  **L3 IP-based Routing**: Create flows for IP-based routing.
6.  **L4 TCP/UDP Port Filtering**: Implement a simple firewall using TCP/UDP port matching.
7.  **Priority-based Flow Matching**: Experiment with flow priorities.

### Section 4: OpenFlow Fundamentals

**Learning Objectives:**
- Analyze flow table outputs to identify default entries.
- Compare reactive and proactive flow installation.
- Evaluate the trade-offs between reactive and proactive modes.

**Lab Steps:**
1.  **Flow Table Analysis**: Examine the default flow table entries.
2.  **Reactive vs. Proactive Comparison**: Run the network in both reactive and proactive modes.
3.  **Packet-In Event Observation**: Observe packet-in events in the controller logs.
4.  **Proactive Flow Installation**: Manually install flows before traffic starts.

### Section 5: Traffic Analysis and Visualization

**Learning Objectives:**
- Apply Wireshark filters to identify OpenFlow messages.
- Use a Ryu GUI to observe topology discovery.
- Analyze counters to validate traffic generation.

**Lab Steps:**
1.  **Wireshark Packet Capture**: Capture and analyze OpenFlow traffic.
2.  **OpenFlow Handshake Identification**: Identify the HELLO, FEATURES_REQUEST, and FEATURES_REPLY messages.
3.  **RYU GUI Topology Discovery**: Use the Ryu GUI to visualize the network topology.
4.  **Statistics Collection**: Collect flow and port statistics using `ovs-ofctl`.

### Section 6: Custom Topologies

**Learning Objectives:**
- Apply MiniEdit to construct topologies graphically.
- Implement custom topologies using the Mininet Python API.
- Analyze the trade-offs between GUI and API approaches.

**Lab Steps:**
1.  **MiniEdit Graphical Design**: Create a custom topology using the MiniEdit GUI.
2.  **Python API Programming**: Write a Python script to create a custom topology.
3.  **Topology Validation**: Test the custom topology to ensure it functions as expected.

### Section 7: Controller Application Development

**Learning Objectives:**
- Understand the packet-in -> decision -> flow mod cycle.
- Create working controller applications, including a hub, L2 switch, and simple firewall.

**Lab Steps:**
1.  **Hub Application**: Implement a simple hub that floods all packets.
2.  **L2 Learning Switch**: Create a learning switch that learns MAC addresses.
3.  **L3 Router**: Implement a basic L3 router.
4.  **L4 Firewall**: Create a firewall that filters traffic based on TCP/UDP ports.

### Section 8: Advanced Applications and Security

**Learning Objectives:**
- Implement a load balancer.
- Design and implement an advanced firewall, an IDS, and DDoS mitigation.
- Analyze network telemetry to distinguish normal from anomalous behavior.

**Lab Steps:**
1.  **Load Balancer**: Design and implement a simple load balancer.
2.  **Advanced Firewall**: Create a multi-field firewall.
3.  **Network Monitoring**: Use telemetry to monitor network performance.
4.  **Intrusion Detection System (IDS)**: Simulate an IDS to detect suspicious traffic.
5.  **DDoS Mitigation**: Implement a basic DDoS mitigation strategy.

---

## 4. Web Platform User Guide

This guide provides instructions for students on how to use the SDN Lab Platform's web interface.

### 4.1. Student Dashboard Navigation

The main dashboard provides an overview of all nine curriculum sections, your progress in each, and any achievements you have earned. You can click on any section to enter the lab environment.

### 4.2. Interactive Tutorial System Usage

Each lab section includes a detailed, step-by-step tutorial. Follow the instructions, and use the interactive terminal to execute the commands. The tutorial will guide you through the learning objectives for that section.

### 4.3. Command Execution Environment

The interactive terminal provides a real-time, sandboxed environment for executing SDN commands. It is connected to a backend that runs the commands in a secure container. The terminal supports command history and provides real-time feedback.

### 4.4. Assessment and Quiz System

At the end of each section, there is a quiz to assess your understanding of the material. The quizzes are auto-graded, and you will receive immediate feedback. A score of 70% or higher is required to pass. You can retry quizzes as many times as you need to.

### 4.5. Progress Tracking and Achievements

Your progress is tracked automatically as you complete tutorials and assessments. You can view your completion status and time spent per section on the main dashboard. You will also earn achievement badges for completing sections and mastering concepts.

---

## 5. Instructor Guide

This guide is for instructors and administrators who are managing the SDN Lab Platform.

### 5.1. Lab Management and Administration

Instructors have the ability to manage the lab environment, including starting and stopping controller instances and customizing lab content. The curriculum content can be modified by editing the `LabTutorial.tsx` and `AssessmentQuiz.tsx` files in the frontend codebase.

### 5.2. Student Progress Monitoring

Instructors can monitor the progress of all students through an administrative dashboard (to be configured). This includes viewing section completion rates, assessment scores, and time spent on each section.

### 5.3. Assessment Grading and Feedback

The quizzes are auto-graded by the `assessment-manager` edge function. Instructors can view the results and provide additional feedback to students if needed. The passing threshold for quizzes is configurable in the `assessment-manager` function.

### 5.4. Custom Curriculum Modifications

The platform is designed to be extensible. Instructors can modify the existing curriculum or add new sections by following the structure of the existing `LabTutorial.tsx` and `AssessmentQuiz.tsx` components. New backend functionality can be added by creating new edge functions.

---

## 6. Technical Reference

This section provides a detailed technical reference for the core SDN technologies used in the platform.

### 6.1. SDN Technologies Reference Guide

-   **RYU Controller**: A component-based SDN framework written in Python. It supports OpenFlow versions 1.0-1.5 and is used for creating control-plane logic.
-   **Open vSwitch (OVS)**: A multilayer virtual switch that enables network automation. It is managed via `ovs-vsctl` for configuration and `ovs-ofctl` for OpenFlow control.
-   **OpenFlow**: The standard protocol for communication between SDN controllers and switches. It allows for the programmatic management of flow tables.
-   **Mininet**: A network emulator that creates a realistic virtual network on a single machine. It is used for prototyping and testing SDN applications.

### 6.2. Command Reference

| Tool | Command | Purpose |
|---|---|---|
| Ryu | `ryu-manager <app>` | Start the Ryu controller with a specific application. |
| Mininet | `mn --controller=remote,ip=...` | Create a topology and connect to a remote controller. |
| Mininet | `pingall` | Test all-pairs connectivity. |
| Mininet | `iperf h1 h2` | Measure throughput between two hosts. |
| OVS | `ovs-vsctl show` | Display bridge and controller information. |
| OVS | `ovs-ofctl dump-flows s1` | List the flow table entries for a switch. |
| OVS | `ovs-ofctl add-flow s1 "..."` | Add a flow rule to a switch. |

### 6.3. API Documentation

The platform utilizes several backend APIs, implemented as Supabase Edge Functions:

-   `command-executor`: Executes SDN commands in a secure, sandboxed environment.
-   `controller-manager`: Manages the lifecycle of Ryu controller instances.
-   `assessment-manager`: Handles the grading of quizzes and assessments.
-   `progress-tracker`: Tracks student progress through the curriculum.

### 6.4. Database Schema

The Supabase database includes the following key tables:

-   `profiles`: Stores user profile information.
-   `lab_progress`: Tracks the completion status of each lab section for each user.
-   `assessment_responses`: Stores user responses to quizzes and assessments.
-   `achievements`: Tracks the badges and achievements earned by users.

---

## 7. Advanced Topics & Research

This section outlines advanced topics and potential research directions for extending the platform and curriculum.

### 7.1. Research Lab Extensions

The curriculum includes a research track with pathways for exploring advanced topics:

-   **Network Function Virtualization (NFV)**: Investigate the performance of virtualized network functions.
-   **P4 Programming**: Explore the P4 language for programmable data planes.
-   **Intent-Based Networking (IBN)**: Translate high-level intents into concrete network policies.
-   **Machine Learning for Traffic Classification**: Build and evaluate ML models for traffic analysis.
-   **SD-WAN**: Implement application-aware routing over emulated WAN links.
-   **Time-Sensitive Networking (TSN)**: Model and schedule time-constrained traffic.

### 7.2. Custom Application Development

The platform can be extended by developing custom controller applications. The modular nature of Ryu makes it easy to create new applications for tasks like advanced routing, security, or quality of service.

### 7.3. Performance Optimization

For complex topologies, performance can be optimized by adjusting the resources allocated to the Docker containers, optimizing flow rules, and using more efficient controller logic.

### 7.4. Security Considerations

The platform includes a command whitelist and input sanitization to prevent malicious use. For production deployments, further security measures, such as network isolation and more granular access control, should be considered.

---

## 8. Appendices

### 8.1. Quick Reference Cards

**Mininet CLI Cheatsheet**
- `nodes`: List all nodes.
- `net`: Display network connections.
- `dump`: Show information about all nodes.
- `hX ifconfig`: Show the configuration of a host's interface.
- `pingall`: Test connectivity between all hosts.

**Open vSwitch Cheatsheet**
- `ovs-vsctl show`: Show all bridges and their configurations.
- `ovs-ofctl show <bridge>`: Show the ports and features of a bridge.
- `ovs-ofctl dump-flows <bridge>`: Dump all flow entries in a bridge.

### 8.2. Common Troubleshooting Scenarios

Refer to the troubleshooting tables in the Installation & Setup Guide and the Lab Manual for detailed guidance on resolving common issues.

### 8.3. FAQ and Support Resources

**Q: Why can't my Mininet instance connect to the Ryu controller?**
A: This is often due to an incorrect IP address or port, or the controller not being started first. Check your configuration and ensure the controller is running before starting Mininet.

**Q: Why are my flow rules not working as expected?**
A: This could be due to incorrect flow priorities, match fields, or actions. Use `ovs-ofctl dump-flows` to carefully inspect your flow table.

---

## 9. Sources

This documentation was compiled using information from the following sources:

- [1] Python Subprocess Documentation (https://docs.python.org/3/library/subprocess.html) - Publisher: Python Software Foundation - High Reliability - Official language documentation.
- [2] Python Official Tutorial (https://docs.python.org/3/tutorial/) - Publisher: Python Software Foundation - High Reliability - Official language tutorial.
- [3] pytest - mature full-featured Python testing tool (https://pytest.org/en/stable/) - Publisher: pytest development team - High Reliability - Official documentation for a widely used testing framework.
- [4] Ryu SDN Framework Documentation (https://ryu.readthedocs.io/_/downloads/en/latest/pdf/) - Publisher: Ryu Development Team - High Reliability - Official project documentation.
- [5] Ryu SDN Framework Overview (https://ryu-sdn.org/) - Publisher: Ryu Project - High Reliability - Official project website.
- [6] Open vSwitch Cheat Sheet (https://randomsecurity.dev/posts/openvswitch-cheat-sheet/) - Publisher: Random Security - Medium Reliability - Community-provided cheat sheet, useful but not official.
- [7] Mininet Sample Workflow (http://mininet.org/sample-workflow/) - Publisher: Mininet Project - High Reliability - Official project documentation.
- [8] SDN Real-World Use Cases 2025 (https://www.linkedin.com/pulse/software-defined-networking-sdn-real-world-5-uses-youll-ejlbc) - Publisher: LinkedIn - Medium Reliability - Industry article, provides context but may have biases.
- [9] Open vSwitch Official Documentation (https://docs.openvswitch.org/) - Publisher: Open vSwitch Project - High Reliability - Official project documentation.
- [10] Software-Defined Networking Explained (https://www.strongdm.com/blog/software-defined-networking) - Publisher: StrongDM - Medium Reliability - Vendor blog, provides useful explanations but may be biased.
- [11] OpenFlow Technical Papers and Tutorials (https://www.clear.rice.edu/comp529/www/papers/tutorial_4.pdf) - Publisher: Stanford University & Rice University - High Reliability - Academic paper from reputable institutions.
- [12] OpenFlow Tutorial - Complete Implementation Guide (https://homepages.dcc.ufmg.br/~mmvieira/cc/OpenFlow%20Tutorial%20-%20OpenFlow%20Wiki.htm) - Publisher: UFMG University - High Reliability - University-provided tutorial.
