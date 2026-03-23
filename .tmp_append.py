#!/usr/bin/env python3
fp = '/Users/austinsonger/code/grc-toolkit/Information Security Management System Program.markdown'
text = """
### **A.8.13 Information Backup**

**Control Objective.** Maintain and regularly test backup copies of information, software, and system configurations per an agreed backup policy.

**Implementation.** [Company] operates a comprehensive backup program protecting critical data, application configurations, and system images against loss from hardware failure, human error, malware, or disaster. The program is aligned with ICT continuity requirements (A.5.30) and defined RTOs/RPOs.

Backups cover production databases, file storage, system configurations, application state, and identity and access management data. The <Cloud Hosting Provider> native backup and replication services provide automated, encrypted backups with geographic redundancy. Retention periods are defined per data type and regulatory requirements (A.5.33).

Backup integrity is verified through automated validation. Restore testing is conducted at planned intervals to confirm data can be recovered within defined RTOs. Test results are documented and gaps remediated. Backup data is encrypted at rest and in transit and protected from unauthorized access and ransomware through immutable backup configurations where supported.

**Roles and Responsibilities.** The IT and Security team implements, monitors, and tests backups. The Cybersecurity Program Manager defines backup requirements and recovery objectives. System owners verify that their critical data is covered.

**Evidence and Documentation.**

- Backup policy with schedules, retention, and RPO/RTO requirements
- Backup job completion and validation records
- Restore test results and after-action reports
- Encryption and access control configurations for backup storage
- Backup coverage inventory

**Review and Continuous Improvement.** The backup program is reviewed annually. Restore test results, backup failure rates, and actual recovery experiences inform improvements. Gaps are addressed through the Corrective Action Plan process.

### **A.8.14 Redundancy of Information Processing Facilities**

**Control Objective.** Implement sufficient redundancy to meet availability requirements for information processing facilities.

**Implementation.** [Company] designs infrastructure with redundancy aligned to availability requirements derived from the business impact analysis. The cloud-native architecture on <Cloud Hosting Provider> enables multi-availability-zone deployment for critical services, providing resilience against facility-level failures.

Redundancy measures include load-balanced application tiers across availability zones, database replication with automatic failover, redundant network connectivity, and geographic distribution for disaster recovery. Failover mechanisms are tested periodically to verify they activate correctly and meet defined recovery objectives.

Non-critical services may use reduced redundancy where the business impact of downtime is acceptable. Redundancy decisions are documented and aligned with agreed service levels.

**Roles and Responsibilities.** The IT and Security team designs and implements redundant architectures. The Cybersecurity Program Manager ensures redundancy meets ISMS availability requirements. The ISMS Management Committee approves availability requirements and accepts residual risk.

**Evidence and Documentation.**

- Redundancy architecture documentation
- Availability zone deployment configurations
- Failover test results
- Service availability metrics
- Business impact analysis supporting redundancy decisions

**Review and Continuous Improvement.** Redundancy is reviewed annually and after significant infrastructure changes. Failover tests validate effectiveness. Availability metrics and actual outage experiences inform improvements through the Corrective Action Plan process.

### **A.8.15 Logging**

**Control Objective.** Produce, store, protect, and analyze logs recording activities, exceptions, faults, and security events.

**Implementation.** [Company] maintains comprehensive logging across systems, applications, network devices, and security platforms, centralized in the <SIEM Platform> for correlation, analysis, and retention.

Logged events include authentication successes and failures, access to sensitive data, administrative and privileged actions, system and application errors, security events and alerts, configuration changes, and network activity. Log entries contain sufficient detail for investigation: timestamp, source, user identity, event type, outcome, and affected resource.

Logs are protected against tampering through write-once storage, access restrictions, and integrity monitoring. Clock synchronization (A.8.17) ensures consistent timestamps. Retention periods meet legal, regulatory, and investigative requirements. Automated analysis in the <SIEM Platform> provides real-time alerting for security-relevant patterns.

**Roles and Responsibilities.** The IT and Security team manages log infrastructure, configures collection, and monitors alerts. The Cybersecurity Program Manager defines logging requirements and retention. System owners ensure their systems generate required logs.

**Evidence and Documentation.**

- Logging policy with requirements per system type
- Log source inventory and collection configurations
- <SIEM Platform> alert rules and correlation configurations
- Log retention configurations
- Log integrity protection configurations

**Review and Continuous Improvement.** Logging coverage and effectiveness are reviewed annually. Log source coverage, alert accuracy (false positives/negatives), and investigation utility are assessed. Gaps discovered during incident investigations drive improvements through the Corrective Action Plan process.

### **A.8.16 Monitoring Activities**

**Control Objective.** Monitor networks, systems, and applications for anomalous behavior and evaluate potential security incidents.

**Implementation.** [Company] operates continuous monitoring across infrastructure, applications, and user activity layers. The <SIEM Platform> aggregates and correlates events from multiple sources. The <Endpoint Detection and Response Platform> monitors endpoint behavior. Network monitoring tools track traffic patterns and detect anomalies.

Monitoring covers: network traffic for unusual patterns and known threats, system resource utilization for anomalies, application behavior for errors and security events, user activity for policy violations and insider threat indicators, and cloud service configurations for unauthorized changes. Baselines of normal activity are established, and deviations trigger investigation.

Alert triage follows the assessment process (A.5.25), with confirmed incidents escalated through the incident management process. Monitoring operates 24/7, with automated alerting for critical events and on-call response.

**Roles and Responsibilities.** The IT and Security team operates monitoring tools and performs alert triage. The Cybersecurity Program Manager defines monitoring requirements and reviews effectiveness. System owners provide context for alerts in their domains.

**Evidence and Documentation.**

- Monitoring architecture and tool configurations
- Alert rules and escalation procedures
- Triage and investigation records
- Monitoring coverage assessments
- Effectiveness metrics (detection rates, triage times)

**Review and Continuous Improvement.** Monitoring effectiveness is reviewed annually. Post-incident reviews identify detection gaps. Alert tuning reduces false positives. Coverage is expanded as new systems or threats are identified. Improvements are addressed through the Corrective Action Plan process.

### **A.8.17 Clock Synchronization**

**Control Objective.** Synchronize clocks across all information processing systems to a single, approved time source.

**Implementation.** [Company] synchronizes all system clocks to approved, authoritative time sources using NTP (Network Time Protocol). The <Cloud Hosting Provider> provides accurate time services synchronized to national standards.

On-premises and endpoint devices synchronize to organizational time servers or directly to the cloud provider\u2019s NTP service. Time zone and UTC usage conventions are documented. Clock accuracy is monitored, and synchronization failures trigger alerts.

Accurate and consistent timestamps are essential for log correlation (A.8.15), incident investigation (A.5.28), and forensic analysis. All log sources must produce timestamps traceable to the approved time reference.

**Roles and Responsibilities.** The IT and Security team configures and monitors time synchronization. The Cybersecurity Program Manager defines requirements. System owners verify their systems are synchronized.

**Evidence and Documentation.**

- NTP configuration records
- Time source documentation
- Synchronization monitoring and alert records
- Time accuracy verification records

**Review and Continuous Improvement.** Synchronization configurations are reviewed annually and when infrastructure changes. Accuracy is verified through monitoring. Drift issues are addressed promptly through the Corrective Action Plan process.

### **A.8.18 Use of Privileged Utility Programs**

**Control Objective.** Restrict and control the use of utility programs capable of overriding system and application controls.

**Implementation.** [Company] restricts access to system utilities that could bypass security controls \u2014 disk editors, registry editors, debug tools, network sniffers, password recovery tools, and similar programs. These utilities are removed from systems where not needed and, where required, restricted to authorized personnel only.

Use of privileged utilities requires authorization from the Cybersecurity Program Manager, is limited to specific tasks, and is logged comprehensively. Utilities are not available on standard user endpoints; they are accessible only on designated administrative workstations or through controlled provisioning.

The separation of privileged utility access from normal operational access reduces the risk of accidental misuse or exploitation by attackers who compromise a standard account.

**Roles and Responsibilities.** The IT and Security team controls utility availability and access. The Cybersecurity Program Manager authorizes use. System administrators use utilities only for approved purposes and document their actions.

**Evidence and Documentation.**

- Authorized utility inventory
- Access restriction configurations
- Usage authorization records
- Utility usage logs
- Administrative workstation configurations

**Review and Continuous Improvement.** Utility restrictions are reviewed annually. Unauthorized utility presence is detected through endpoint scanning. Usage logs are reviewed for anomalies. Findings are addressed through the Corrective Action Plan process.

### **A.8.19 Installation of Software on Operational Systems**

**Control Objective.** Control software installation on operational systems to maintain integrity and prevent introduction of vulnerabilities or malware.

**Implementation.** [Company] restricts software installation on operational systems through technical controls and policy. Standard users cannot install software on managed endpoints; installation requires administrative privileges controlled through the privileged access process (A.8.2).

Approved software is deployed through the organization\u2019s endpoint management platform, ensuring consistent configuration and licensing compliance. Requests for new software go through an approval process that includes security assessment, licensing verification, and compatibility testing.

On production servers and infrastructure, software changes follow the change management process with security impact assessment. Only authorized, tested versions are deployed. Unauthorized software discovered through endpoint scanning is flagged for investigation and removal.

**Roles and Responsibilities.** The IT and Security team manages the approved software catalog and deployment. The Cybersecurity Program Manager defines installation policies. System administrators install software through approved channels only.

**Evidence and Documentation.**

- Approved software catalog
- Software request and approval records
- Endpoint management deployment records
- Unauthorized software detection and removal records
- Change management records for server software

**Review and Continuous Improvement.** The approved catalog is reviewed annually. Unauthorized software detection rates are tracked. Installation controls are validated through endpoint compliance monitoring. Deficiencies are addressed through the Corrective Action Plan process.

### **A.8.20 Networks Security**

**Control Objective.** Secure and control networks to protect information in systems and applications.

**Implementation.** [Company] implements network security through a defense-in-depth approach covering the cloud infrastructure on <Cloud Hosting Provider>, corporate network (where applicable), and remote access.

Controls include network segmentation separating environments by sensitivity and function (production, staging, development, management), firewalls and security groups enforcing least-privilege network access rules, intrusion detection and prevention capabilities, encrypted communications for all sensitive traffic, and DNS security filtering.

The cloud network architecture uses virtual private clouds, subnet isolation, and security groups to enforce microsegmentation. Internet-facing services are protected by web application firewalls and DDoS protection. Administrative access to network infrastructure requires MFA and is logged.

**Roles and Responsibilities.** The IT and Security team designs, implements, and maintains network security. The Cybersecurity Program Manager defines requirements and reviews architecture. Network changes follow the change management process.

**Evidence and Documentation.**

- Network architecture diagrams and documentation
- Firewall and security group rule sets
- Network segmentation documentation
- IDS/IPS configurations and alert records
- Network change management records

**Review and Continuous Improvement.** Network security is reviewed annually and after significant infrastructure changes. Firewall rules are reviewed for necessity and least privilege. Penetration testing validates segmentation. Findings are addressed through the Corrective Action Plan process.

### **A.8.21 Security of Network Services**

**Control Objective.** Identify, implement, and monitor security mechanisms, service levels, and requirements for all network services.

**Implementation.** [Company] defines security requirements for all network services \u2014 whether provided internally, by <Cloud Hosting Provider>, or by third-party service providers. Requirements address authentication, encryption, access control, monitoring, availability, and incident response.

For internal services, the IT and Security team implements controls per the network security architecture. For provider services, requirements are incorporated into agreements (A.5.20) and validated through audit reports and monitoring (A.5.22). Service levels for availability, performance, and security response are defined and tracked.

Network service configurations are documented and managed under change control (A.8.9). Access to network management interfaces is restricted and logged.

**Roles and Responsibilities.** The IT and Security team manages internal network services and monitors provider services. The Cybersecurity Program Manager defines security requirements and reviews service agreements. Provider performance is tracked against agreed service levels.

**Evidence and Documentation.**

- Network service inventory with security requirements
- Service level agreements and monitoring records
- Provider audit reports and compliance evidence
- Network service configuration documentation
- Access logs for network management interfaces

**Review and Continuous Improvement.** Network service security is reviewed annually. Service level compliance is tracked. Provider reassessments inform requirement updates. Deficiencies are addressed through the Corrective Action Plan process.

### **A.8.22 Segregation of Networks**

**Control Objective.** Segregate groups of information services, users, and information systems based on trust levels and business requirements.

**Implementation.** [Company] segregates networks to limit the blast radius of security incidents and enforce access control at the network layer. Segregation is implemented through virtual private clouds, subnets, security groups, and network access control lists on <Cloud Hosting Provider>.

Key segregation boundaries include: production vs. non-production environments, internet-facing vs. internal services, management networks vs. data networks, and high-sensitivity zones vs. general-purpose zones. Traffic between segments is controlled by security groups and firewalls enforcing least-privilege rules.

The segregation design supports the principle of defense in depth \u2014 even if one segment is compromised, lateral movement to other segments is restricted. Network monitoring (A.8.16) detects unauthorized cross-segment traffic.

**Roles and Responsibilities.** The IT and Security team implements and maintains segregation. The Cybersecurity Program Manager defines segregation requirements. Network changes affecting segmentation go through change management with security review.

**Evidence and Documentation.**

- Network segregation architecture and diagrams
- Security group and ACL rule sets
- Cross-segment traffic policies
- Segregation validation test results
- Unauthorized cross-segment traffic alerts

**Review and Continuous Improvement.** Segregation is reviewed annually and after infrastructure changes. Penetration testing validates effectiveness. Rule sets are reviewed for necessity. Findings are addressed through the Corrective Action Plan process.

### **A.8.23 Web Filtering**

**Control Objective.** Manage access to external websites to reduce exposure to malicious content.

**Implementation.** [Company] implements web filtering to protect against drive-by downloads, phishing sites, malicious domains, and inappropriate content. DNS-based filtering blocks access to categories of known malicious, phishing, and prohibited sites.

The filtering configuration balances protection with business need. Blocked categories include known malware distribution, phishing, command and control, and other high-risk categories. Business-justified exceptions can be requested and are approved by the IT and Security team.

Filtering is applied to all organizational endpoints and network egress points. The filtering service integrates threat intelligence feeds for up-to-date protection. Filtering logs support investigation and compliance monitoring.

**Roles and Responsibilities.** The IT and Security team implements and maintains filtering. The Cybersecurity Program Manager defines filtering policy. Exception requests are evaluated by the IT and Security team.

**Evidence and Documentation.**

- Web filtering policy and category configurations
- Exception request and approval records
- Filtering logs and reports
- Threat intelligence feed configurations
- Blocked access reports and trends

**Review and Continuous Improvement.** Filtering effectiveness is reviewed annually. Blocked access trends, exception requests, and malware incident correlation inform policy adjustments. Improvements are addressed through the Corrective Action Plan process.
"""

with open(fp, 'a', encoding='utf-8') as f:
    f.write(text)
print("Done: A.8.13-A.8.23")
