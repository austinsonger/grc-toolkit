# Evidence Fetchers Catalog
[![Fetcher Count](https://img.shields.io/badge/Active_Fetchers-42_Scripts-blue)]() [![Compliance Status](https://img.shields.io/badge/Coverage-84%25_Automated-green)]()

Welcome to the **Evidence Fetchers Catalog**.

This repository contains the automated scripts ("fetchers") used to validate your security posture against **FedRAMP 20x Key Security Indicators (KSIs)** and more. This dashboard maps each 20x KSI to the evidence fetchers used to provide evidence for the KSI.

### 📊 Compliance Summary

| Status | Count | Percentage | Definition |
| :--- | :--- | :--- | :--- |
|  **Automated** | **42** | **84%** | Validated by a script in this repo. |
|  **Manual** | **8** | **16%** | Validated by a pass or fail questionnaire.|

---

## CED Family (Cybersecurity Education)

| KSI ID (20x) | Former KSI ID name | Evidence Title | Fetcher Script | Source System | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`KSI-CED-RGT`** | **`CED-01`** | Security Awareness Training | [security_awareness_training.sh](knowbe4/security_awareness_training.sh) | KnowBe4 | Automated |
| **`KSI-CED-RST`** | **`CED-02`** | Role Specific Training (High Risk) | [high_risk_training.sh](knowbe4/high_risk_training.sh) | KnowBe4 | Automated |
| **`KSI-CED-DET`** | **`CED-03`** | Development and Engineering Training | [developer_specific_training.sh](knowbe4/developer_specific_training.sh) | KnowBe4 | Automated |
| **`KSI-CED-RRT`** | **`CED-04`** | Response and Recovery Training | - | - | Manual |

---

## CMT Family (Change Management)

| KSI ID (20x) | Former KSI ID name | Evidence Title | Fetcher Script | Source System | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`KSI-CMT-LMC`** | **`CMT-01`** | GitLab Merge Request Summary | [gitlab_merge_request_summary.py](gitlab/gitlab_merge_request_summary.py) | GitLab | Automated |
|  |  | GitLab CI/CD Pipeline Configuration | [gitlab_ci_cd_pipeline_config.py](gitlab/gitlab_ci_cd_pipeline_config.py) | GitLab | Automated |
| **`KSI-CMT-RMV`** | **`CMT-02`** | Checkov Terraform Security | [checkov_terraform.sh](checkov/checkov_terraform.sh) | Checkov (IaC Scanner) | Automated |
|  |  | Checkov Kubernetes Security | [checkov_kubernetes.sh](checkov/checkov_kubernetes.sh) | Checkov (IaC Scanner) | Automated |
|  |  | GitLab Merge Request Summary | [gitlab_merge_request_summary.py](gitlab/gitlab_merge_request_summary.py) | GitLab | Automated |
|  |  | GitLab Project Summary | [gitlab_project_summary.py](gitlab/gitlab_project_summary.py) | GitLab | Automated |
| **`KSI-CMT-VTD`** | **`CMT-03`** | GitLab CI/CD Pipeline Configuration | [gitlab_ci_cd_pipeline_config.py](gitlab/gitlab_ci_cd_pipeline_config.py) | GitLab | Automated |
| **`KSI-CMT-RVP`** | **`CMT-04`** | Reviewing Change Procedures | - | - | Manual |

---

## CNA Family (Cloud-Native Architecture)

| KSI ID (20x) | Former KSI ID name | Evidence Title | Fetcher Script | Source System | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`KSI-CNA-RNT`** | **`CNA-01`** | Security Groups | [security_groups.sh](aws/security_groups.sh) | AWS | Automated |
|  |  | WAF All Rules | [waf_all_rules.sh](aws/waf_all_rules.sh) | AWS WAF | Automated |
|  |  | WAF DoS Rules | [waf_DoS_rules.sh](aws/waf_DoS_rules.sh) | AWS WAF | Automated |
| **`KSI-CNA-MAT`** | **`CNA-02`** | Load Balancer Encryption Status | [load_balancer_encryption_status.sh](aws/load_balancer_encryption_status.sh) | AWS ELB | Automated |
|  |  | AWS Component SSL Enforcement | [aws_component_ssl_enforcement_status.sh](aws/aws_component_ssl_enforcement_status.sh) | AWS | Automated |
|  |  | Security Groups | [security_groups.sh](aws/security_groups.sh) | AWS | Automated |
| **`KSI-CNA-ULN`** | **`CNA-03`** | WAF All Rules | [waf_all_rules.sh](aws/waf_all_rules.sh) | AWS WAF | Automated |
|  |  | AWS Component SSL Enforcement | [aws_component_ssl_enforcement_status.sh](aws/aws_component_ssl_enforcement_status.sh) | AWS | Automated |
| **`KSI-CNA-DFP`** | **`CNA-04`** | Checkov Terraform Security | [checkov_terraform.sh](checkov/checkov_terraform.sh) | Checkov (IaC Scanner) | Automated |
|  |  | Checkov Kubernetes Security | [checkov_kubernetes.sh](checkov/checkov_kubernetes.sh) | Checkov (IaC Scanner) | Automated |
| **`KSI-CNA-RVP`** | **`CNA-05`** | WAF All Rules | [waf_all_rules.sh](aws/waf_all_rules.sh) | AWS WAF | Automated |
|  |  | WAF DoS Rules | [waf_DoS_rules.sh](aws/waf_DoS_rules.sh) | AWS WAF | Automated |
| **`KSI-CNA-OFA`** | **`CNA-06`** | Auto Scaling High Availability | [auto_scaling_high_availability.sh](aws/auto_scaling_high_availability.sh) | AWS Auto Scaling | Automated |
|  |  | Database High Availability | [database_high_availability.sh](aws/database_high_availability.sh) | AWS RDS | Automated |
|  |  | EKS High Availability | [eks_high_availability.sh](aws/eks_high_availability.sh) | AWS EKS | Automated |
|  |  | EFS High Availability | [efs_high_availability.sh](aws/efs_high_availability.sh) | AWS EFS | Automated |
|  |  | Load Balancer High Availability | [load_balancer_high_availability.sh](aws/load_balancer_high_availability.sh) | AWS ELB | Automated |
|  |  | Network Resilience High Availability | [network_resilience_high_availability.sh](aws/network_resilience_high_availability.sh) | AWS Networking | Automated |
|  |  | Route 53 High Availability | [route53_high_availability.sh](aws/route53_high_availability.sh) | AWS Route 53 | Automated |
| **`KSI-CNA-IBP`** | **`CNA-07`** | WAF All Rules | [waf_all_rules.sh](aws/waf_all_rules.sh) | AWS WAF | Automated |
|  |  | Checkov Terraform Security | [checkov_terraform.sh](checkov/checkov_terraform.sh) | Checkov (IaC Scanner) | Automated |
| **`KSI-CNA-EIS`** | **`CNA-08`** | Enforcing Intended State | [aws_config_conformance_packs.sh](aws/aws_config_conformance_packs.sh) | AWS Config | Automated |

---

## IAM Family (Identity and Access Management)

| KSI ID (20x) | Former KSI ID name | Evidence Title | Fetcher Script | Source System | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`KSI-IAM-MFA`** | **`IAM-01`** | Okta Phishing Resistant MFA | [okta_phishing_resistant_mfa.py](okta/okta_phishing_resistant_mfa.py) | Okta | Automated |
|  |  | IAM Identity Center | [iam_identity_center.sh](aws/iam_identity_center.sh) | AWS IAM Identity Center | Automated |
|  |  | IAM Roles | [iam_roles.sh](aws/iam_roles.sh) | AWS IAM | Automated |
|  |  | IAM Users and Groups | [iam_users_groups.sh](aws/iam_users_groups.sh) | AWS IAM | Automated |
| **`KSI-IAM-APM`** | **`IAM-02`** | Adopting Passwordless Methods | [okta_passwordless_authentication.py](okta/okta_passwordless_authentication.py) | Okta | Automated |
| **`KSI-IAM-SNU`** | **`IAM-03`** | Okta Non-User Accounts | [okta_non_user_accounts_authentication.py](okta/okta_non_user_accounts_authentication.py) | Okta | Automated |
|  |  | IAM Identity Center | [iam_identity_center.sh](aws/iam_identity_center.sh) | AWS IAM Identity Center | Automated |
|  |  | IAM Roles | [iam_roles.sh](aws/iam_roles.sh) | AWS IAM | Automated |
| **`KSI-IAM-JIT`** | **`IAM-04`** | Okta Just-in-Time Authorization | [okta_just_in_time_authorization.py](okta/okta_just_in_time_authorization.py) | Okta | Automated |
|  |  | IAM Identity Center | [iam_identity_center.sh](aws/iam_identity_center.sh) | AWS IAM Identity Center | Automated |
|  |  | IAM Roles | [iam_roles.sh](aws/iam_roles.sh) | AWS IAM | Automated |
| **`KSI-IAM-ELP`** | **`IAM-05`** | Okta Least Privilege | [okta_least_privilege.py](okta/okta_least_privilege.py) | Okta | Automated |
|  |  | IAM Identity Center | [iam_identity_center.sh](aws/iam_identity_center.sh) | AWS IAM Identity Center | Automated |
|  |  | EKS Least Privilege | [eks_least_privilege.sh](aws/eks_least_privilege.sh) | AWS EKS | Automated |
|  |  | IAM Users and Groups | [iam_users_groups.sh](aws/iam_users_groups.sh) | AWS IAM | Automated |
| **`KSI-IAM-SUS`** | **`IAM-06`** | Okta Suspicious Activity | [okta_suspicious_activity_management.py](okta/okta_suspicious_activity_management.py) | Okta | Automated |
|  |  | CloudTrail Configuration | [cloudtrail_configuration.sh](aws/cloudtrail_configuration.sh) | AWS CloudTrail | Automated |
|  |  | SentinelOne Cloud Detection Rules | [sentinelone_cloud_detection_rules.py](sentinelone/sentinelone_cloud_detection_rules.py) | SentinelOne | Automated |
| **`KSI-IAM-AAM`** | **`IAM-07`** | Automated Account Management | [okta_automated_account_management.py](okta/okta_automated_account_management.py) | Okta | Automated |

---

## INR Family (Incident Response)

| KSI ID (20x) | Former KSI ID name | Evidence Title | Fetcher Script | Source System | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`KSI-INR-RIR`** | **`INR-01`** | Reviewing Incident Response Procedures | - | - | Manual |
| **`KSI-INR-RPI`** | **`INR-02`** | Reviewing Past Incidents | [sentinelone_activities.py](sentinelone/sentinelone_activities.py) | SentinelOne | Automated |
| **`KSI-INR-AAR`** | **`INR-03`** | Generating After Action Reports | - | - | Manual |

---

## MLA Family (Monitoring, Logging and Auditing)

| KSI ID (20x) | Former KSI ID name | Evidence Title | Fetcher Script | Source System | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`KSI-MLA-OSM`** | **`MLA-01`** | Operating SIEM Capability | [sentinelone_cloud_detection_rules.py](sentinelone/sentinelone_cloud_detection_rules.py) | SentinelOne | Automated |
|  |  | CloudTrail Configuration | [cloudtrail_configuration.sh](aws/cloudtrail_configuration.sh) | AWS CloudTrail | Automated |
| **`KSI-MLA-RVL`** | **`MLA-02`** | Reviewing Logs | [sentinelone_activities.py](sentinelone/sentinelone_activities.py) | SentinelOne | Automated |
|  |  | CloudTrail Configuration | [cloudtrail_configuration.sh](aws/cloudtrail_configuration.sh) | AWS CloudTrail | Automated |
| **`KSI-MLA-EVC`** | **`MLA-05`** | Evaluating Configurations | [sentinelone_xdr_assets.py](sentinelone/sentinelone_xdr_assets.py) | SentinelOne | Automated |
|  |  | SentinelOne Agents | [sentinelone_agents.py](sentinelone/sentinelone_agents.py) | SentinelOne | Automated |
|  |  | GitLab Project Summary | [gitlab_project_summary.py](gitlab/gitlab_project_summary.py) | GitLab | Automated |
|  |  | Checkov Terraform Security | [checkov_terraform.sh](checkov/checkov_terraform.sh) | Checkov (IaC Scanner) | Automated |
| **`KSI-MLA-LET`** | **`MLA-07`** | Logging Event Types | [cloudwatch_high_availability.sh](aws/cloudwatch_high_availability.sh) | AWS CloudWatch | Automated |
|  |  | CloudTrail Configuration | [cloudtrail_configuration.sh](aws/cloudtrail_configuration.sh) | AWS CloudTrail | Automated |
| **`KSI-MLA-ALA`** | **`MLA-08`** | Authorizing Log Access | [iam_policies.sh](aws/iam_policies.sh) | AWS IAM | Automated |

---

## PIY Family (Policy and inventory)

| KSI ID (20x) | Former KSI ID name | Evidence Title | Fetcher Script | Source System | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`KSI-PIY-GIV`** | **`PIY-01`** | Generating Inventories | [detect_new_aws_resource.sh](aws/detect_new_aws_resource.sh) | AWS | Automated |
|  |  | EKS Pod Inventory | [eks_pod_inventory.sh](k8s/eks_pod_inventory.sh) | Kubernetes (EKS) | Automated |
|  |  | GitLab Project Summary | [gitlab_project_summary.py](gitlab/gitlab_project_summary.py) | GitLab | Automated |
|  |  | Rippling Current Employees | [rippling_current_employees.py](rippling/rippling_current_employees.py) | Rippling | Automated |
|  |  | Rippling All Employees | [rippling_all_employees.py](rippling/rippling_all_employees.py) | Rippling | Automated |
| **`KSI-PIY-RVD`** | **`PIY-03`** | Reviewing Vulnerability Disclosures | - | - | Manual |
| **`KSI-PIY-RSD`** | **`PIY-04`** | GitLab CI/CD Pipeline Config | [gitlab_ci_cd_pipeline_config.py](gitlab/gitlab_ci_cd_pipeline_config.py) | GitLab | Automated |
| **`KSI-PIY-RIS`** | **`PIY-06`** | Reviewing Investments in Security | - | - | Manual |
| **`KSI-PIY-RES`** | **`PIY-08`** | Reviewing Executive Support | - | - | Manual |

---

## RPL Family (Recovery Planning)

| KSI ID (20x) | Former KSI ID name | Evidence Title | Fetcher Script | Source System | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`KSI-RPL-RRO`** | **`RPL-01`** | Reviewing Recovery Objectives | [backup_validation.sh](aws/backup_validation.sh) | AWS Backup | Automated |
| **`KSI-RPL-ARP`** | **`RPL-02`** | Aligning Recovery Plan | [backup_recovery_high_availability.sh](aws/backup_recovery_high_availability.sh) | AWS Backup | Automated |
| **`KSI-RPL-ABO`** | **`RPL-03`** | RDS Database High Availability | [database_high_availability.sh](aws/database_high_availability.sh) | AWS RDS | Automated |
|  |  | Backup Recovery High Availability | [backup_recovery_high_availability.sh](aws/backup_recovery_high_availability.sh) | AWS Backup | Automated |
|  |  | EFS High Availability | [efs_high_availability.sh](aws/efs_high_availability.sh) | AWS EFS | Automated |
|  |  | EKS High Availability | [eks_high_availability.sh](aws/eks_high_availability.sh) | AWS EKS | Automated |
|  |  | Load Balancer High Availability | [load_balancer_high_availability.sh](aws/load_balancer_high_availability.sh) | AWS ELB | Automated |
|  |  | Network Resilience High Availability | [network_resilience_high_availability.sh](aws/network_resilience_high_availability.sh) | AWS Networking | Automated |
|  |  | Route 53 High Availability | [route53_high_availability.sh](aws/route53_high_availability.sh) | AWS Route 53 | Automated |
|  |  | CloudWatch High Availability | [cloudwatch_high_availability.sh](aws/cloudwatch_high_availability.sh) | AWS CloudWatch | Automated |
| **`KSI-RPL-TRC`** | **`RPL-04`** | Testing Recovery Capabilities | [backup_validation.sh](aws/backup_validation.sh) | AWS Backup | Automated |

---

## SCR Family (Supply Chain Risk)

| KSI ID (20x) | Former KSI ID name | Evidence Title | Fetcher Script | Source System | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`KSI-SCR-MIT`** |  | Mitigating Supply Chain Risk | [checkov_terraform.sh](checkov/checkov_terraform.sh) | Checkov (IaC Scanner) | Automated |
| **`KSI-SCR-MON`** |  | Monitoring Supply Chain Risk | [guard_duty.sh](aws/guard_duty.sh) | AWS GuardDuty | Automated |

---

## SVC Family (Service Configuration)

| KSI ID (20x) | Former KSI ID name | Evidence Title | Fetcher Script | Source System | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`KSI-SVC-EIS`** | **`SVC-01`** | GitLab Merge Request Summary | [gitlab_merge_request_summary.py](gitlab/gitlab_merge_request_summary.py) | GitLab | Automated |
|  |  | GitLab Project Summary | [gitlab_project_summary.py](gitlab/gitlab_project_summary.py) | GitLab | Automated |
|  |  | Checkov Terraform Security | [checkov_terraform.sh](checkov/checkov_terraform.sh) | Checkov (IaC Scanner) | Automated |
|  |  | Checkov Kubernetes Security | [checkov_kubernetes.sh](checkov/checkov_kubernetes.sh) | Checkov (IaC Scanner) | Automated |
| **`KSI-SVC-SNT`** | **`SVC-02`** | Block Storage Encryption Status | [block_storage_encryption_status.sh](aws/block_storage_encryption_status.sh) | AWS EBS | Automated |
|  |  | Load Balancer Encryption Status | [load_balancer_encryption_status.sh](aws/load_balancer_encryption_status.sh) | AWS ELB | Automated |
|  |  | RDS Encryption | [rds_encryption_status.sh](aws/rds_encryption_status.sh) | AWS RDS | Automated |
|  |  | S3 Encryption | [s3_encryption_status.sh](aws/s3_encryption_status.sh) | AWS S3 | Automated |
| **`KSI-SVC-ACM`** | **`SVC-04`** | AWS Config Monitoring | [aws_config_monitoring.sh](aws/aws_config_monitoring.sh) | AWS Config | Automated |
|  |  | AWS Config Conformance Packs | [aws_config_conformance_packs.sh](aws/aws_config_conformance_packs.sh) | AWS Config | Automated |
|  |  | IAM Policies | [iam_policies.sh](aws/iam_policies.sh) | AWS IAM | Automated |
|  |  | Checkov Terraform Security | [checkov_terraform.sh](checkov/checkov_terraform.sh) | Checkov (IaC Scanner) | Automated |
| **`KSI-SVC-VRI`** | **`SVC-05`** | Authorized Cryptographic Modules | [block_storage_encryption_status.sh](aws/block_storage_encryption_status.sh) | AWS EBS | Automated |
|  |  | RDS Encryption | [rds_encryption_status.sh](aws/rds_encryption_status.sh) | AWS RDS | Automated |
|  |  | S3 Encryption | [s3_encryption_status.sh](aws/s3_encryption_status.sh) | AWS S3 | Automated |
| **`KSI-SVC-ASM`** | **`SVC-06`** | KMS Key Rotation | [kms_key_rotation.sh](aws/kms_key_rotation.sh) | AWS KMS | Automated |
| **`KSI-SVC-PRR`** | **`SVC-08`** | Preventing Residual Risk | [s3_encryption_status.sh](aws/s3_encryption_status.sh) | AWS S3 | Automated |
| **`KSI-SVC-VCM`** | **`SVC-09`** | Load Balancer Encryption Status | [load_balancer_encryption_status.sh](aws/load_balancer_encryption_status.sh) | AWS ELB | Automated |
| **`KSI-SVC-RUD`** | **`SVC-10`** | Removing Unwanted Data | - | - | Manual |
