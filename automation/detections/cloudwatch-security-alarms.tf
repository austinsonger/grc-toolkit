# CloudWatch Security Alarms for Compliance Monitoring
# GRC-Toolkit: Detection Rules mapped to Security Controls
# Maps to: NIST AU-6, SI-4 | SOC 2 CC7.2, CC7.3 | CIS 4.1-4.15
# Version: 1.0.0

variable "alarm_actions" {
  description = "List of ARNs to notify when alarm triggers (SNS topics)"
  type        = list(string)
  default     = []
}

variable "cloudtrail_log_group_name" {
  description = "Name of the CloudTrail CloudWatch Log Group"
  type        = string
  default     = "/aws/cloudtrail/production"
}

resource "aws_cloudwatch_log_metric_filter" "unauthorized_api_calls" {
  name           = "UnauthorizedAPICalls"
  pattern        = "{ ($.errorCode = \"*UnauthorizedAccess*\") || ($.errorCode = \"AccessDenied*\") }"
  log_group_name = var.cloudtrail_log_group_name
  metric_transformation {
    name          = "UnauthorizedAPICalls"
    namespace     = "CISBenchmark"
    value         = "1"
    default_value = "0"
  }
}

resource "aws_cloudwatch_metric_alarm" "unauthorized_api_calls" {
  alarm_name          = "CIS-4.1-UnauthorizedAPICalls"
  alarm_description   = "Triggers on unauthorized API calls. Maps to: NIST SI-4, AU-6 | SOC2 CC7.2 | CIS 4.1"
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = "1"
  metric_name         = "UnauthorizedAPICalls"
  namespace           = "CISBenchmark"
  period              = "300"
  statistic           = "Sum"
  threshold           = "1"
  treat_missing_data  = "notBreaching"
  alarm_actions       = var.alarm_actions
  ok_actions          = var.alarm_actions
}

resource "aws_cloudwatch_log_metric_filter" "console_signin_without_mfa" {
  name           = "ConsoleSignInWithoutMFA"
  pattern        = "{ ($.eventName = \"ConsoleLogin\") && ($.additionalEventData.MFAUsed != \"Yes\") && ($.userIdentity.type = \"IAMUser\") && ($.responseElements.ConsoleLogin = \"Success\") }"
  log_group_name = var.cloudtrail_log_group_name
  metric_transformation {
    name          = "ConsoleSignInWithoutMFA"
    namespace     = "CISBenchmark"
    value         = "1"
    default_value = "0"
  }
}

resource "aws_cloudwatch_metric_alarm" "console_signin_without_mfa" {
  alarm_name          = "CIS-4.2-ConsoleSignInWithoutMFA"
  alarm_description   = "Console login without MFA detected. Maps to: NIST IA-2(1) | SOC2 CC6.1 | CIS 4.2"
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = "1"
  metric_name         = "ConsoleSignInWithoutMFA"
  namespace           = "CISBenchmark"
  period              = "300"
  statistic           = "Sum"
  threshold           = "1"
  treat_missing_data  = "notBreaching"
  alarm_actions       = var.alarm_actions
}

resource "aws_cloudwatch_log_metric_filter" "root_account_usage" {
  name           = "RootAccountUsage"
  pattern        = "{ $.userIdentity.type = \"Root\" && $.userIdentity.invokedBy NOT EXISTS && $.eventType != \"AwsServiceEvent\" }"
  log_group_name = var.cloudtrail_log_group_name
  metric_transformation {
    name          = "RootAccountUsage"
    namespace     = "CISBenchmark"
    value         = "1"
    default_value = "0"
  }
}

resource "aws_cloudwatch_metric_alarm" "root_account_usage" {
  alarm_name          = "CIS-4.3-RootAccountUsage"
  alarm_description   = "Root account activity detected. Maps to: NIST AC-6(5) | SOC2 CC6.1 | CIS 4.3"
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = "1"
  metric_name         = "RootAccountUsage"
  namespace           = "CISBenchmark"
  period              = "300"
  statistic           = "Sum"
  threshold           = "1"
  treat_missing_data  = "notBreaching"
  alarm_actions       = var.alarm_actions
}

resource "aws_cloudwatch_log_metric_filter" "iam_policy_changes" {
  name           = "IAMPolicyChanges"
  pattern        = "{($.eventName=DeleteGroupPolicy)||($.eventName=DeleteRolePolicy)||($.eventName=DeleteUserPolicy)||($.eventName=PutGroupPolicy)||($.eventName=PutRolePolicy)||($.eventName=PutUserPolicy)||($.eventName=CreatePolicy)||($.eventName=DeletePolicy)||($.eventName=CreatePolicyVersion)||($.eventName=DeletePolicyVersion)||($.eventName=SetDefaultPolicyVersion)||($.eventName=AttachRolePolicy)||($.eventName=DetachRolePolicy)||($.eventName=AttachUserPolicy)||($.eventName=DetachUserPolicy)||($.eventName=AttachGroupPolicy)||($.eventName=DetachGroupPolicy)}"
  log_group_name = var.cloudtrail_log_group_name
  metric_transformation {
    name          = "IAMPolicyChanges"
    namespace     = "CISBenchmark"
    value         = "1"
    default_value = "0"
  }
}

resource "aws_cloudwatch_metric_alarm" "iam_policy_changes" {
  alarm_name          = "CIS-4.4-IAMPolicyChanges"
  alarm_description   = "IAM policy changes detected. Maps to: NIST AC-2, CM-3 | SOC2 CC8.1 | CIS 4.4"
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = "1"
  metric_name         = "IAMPolicyChanges"
  namespace           = "CISBenchmark"
  period              = "300"
  statistic           = "Sum"
  threshold           = "1"
  treat_missing_data  = "notBreaching"
  alarm_actions       = var.alarm_actions
}

resource "aws_cloudwatch_log_metric_filter" "cloudtrail_changes" {
  name           = "CloudTrailChanges"
  pattern        = "{ ($.eventName = CreateTrail) || ($.eventName = UpdateTrail) || ($.eventName = DeleteTrail) || ($.eventName = StartLogging) || ($.eventName = StopLogging) }"
  log_group_name = var.cloudtrail_log_group_name
  metric_transformation {
    name          = "CloudTrailChanges"
    namespace     = "CISBenchmark"
    value         = "1"
    default_value = "0"
  }
}

resource "aws_cloudwatch_metric_alarm" "cloudtrail_changes" {
  alarm_name          = "CIS-4.5-CloudTrailChanges"
  alarm_description   = "CloudTrail configuration change detected. Maps to: NIST AU-9, CM-3 | SOC2 CC7.1 | CIS 4.5"
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = "1"
  metric_name         = "CloudTrailChanges"
  namespace           = "CISBenchmark"
  period              = "300"
  statistic           = "Sum"
  threshold           = "1"
  treat_missing_data  = "notBreaching"
  alarm_actions       = var.alarm_actions
}

resource "aws_cloudwatch_log_metric_filter" "security_group_changes" {
  name           = "SecurityGroupChanges"
  pattern        = "{ ($.eventName = AuthorizeSecurityGroupIngress) || ($.eventName = AuthorizeSecurityGroupEgress) || ($.eventName = RevokeSecurityGroupIngress) || ($.eventName = RevokeSecurityGroupEgress) || ($.eventName = CreateSecurityGroup) || ($.eventName = DeleteSecurityGroup)}"
  log_group_name = var.cloudtrail_log_group_name
  metric_transformation {
    name          = "SecurityGroupChanges"
    namespace     = "CISBenchmark"
    value         = "1"
    default_value = "0"
  }
}

resource "aws_cloudwatch_metric_alarm" "security_group_changes" {
  alarm_name          = "CIS-4.15-SecurityGroupChanges"
  alarm_description   = "Security group changes detected. Maps to: NIST CM-3, SC-7 | SOC2 CC8.1 | CIS 4.15"
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = "1"
  metric_name         = "SecurityGroupChanges"
  namespace           = "CISBenchmark"
  period              = "300"
  statistic           = "Sum"
  threshold           = "1"
  treat_missing_data  = "notBreaching"
  alarm_actions       = var.alarm_actions
}
