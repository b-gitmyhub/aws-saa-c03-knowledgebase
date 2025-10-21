# IAM

> Auto-generated from raw notes.

## Contents


### - Attach the same volume to multiple EC2 instances in the same AZ

- Attach the same volume to multiple EC2 instances in the same AZ
- Each instance has full read-write permissions to the high performance volume
- Use case:
    - achieve higher app availability in clustered linux applications
    - apps must manage concurrent write ops.
    [diagram: AZ1 with EC2 instances and io2 volume]

### IAM - Password Policy

IAM - Password Policy

### Strong passwords → higher security for the account

Strong passwords → higher security for the account

### Enforce password policies by:

Enforce password policies by:
- setting minimum password length
- require specific characters
    - uppercase letters
    - lowercase letters
    - numbers
    - non-alphanumeric chars
- allow all IAM users to change their own passwords
- set password expiration
- prevent password reuse

### Enforce multi factor authentication: MFA = password + security device (you know)

Enforce multi factor authentication: MFA = password + security device (you know) (you own)

### AWS accepted MFA types:

AWS accepted MFA types:
- Virtual MFA device → Google Authenticator, Authy
- U2F security key (Universal Two Factor) Example: Yubikey (3P)
- Hardware Key Fob MFA Device Example: Gemalto (3P)
- AWS GovCloud (US) Example: SurePassID (3P)
- Hardware time-based One Time Password (TOTP)

### AWS Access

AWS Access
- AWS Management Console (password + MFA)
- AWS Command Line Interface (CLI) (access keys)
- AWS Software Development Kit (SDK) (access keys)
- Access Key ID = username
  Secret Access Key = password
- AWS CloudShell → Terminal (Web) in the AWS cloud

### IAM Roles for services

IAM Roles for services
An IAM role is a virtual identity within your AWS account that is not associated with a specific user. Instead, it has a set of permissions attached to it.
Purpose: Roles are designed to allow AWS services to perform actions on your behalf.
Example: EC2, Lambda…

### IAM Security Tools

IAM Security Tools
- IAM credential report (account-level) → reports all your accounts, users, and cred. status (password, access key, last access)
- IAM Access Advisor (user-level) → shows service permissions granted to user and when service was last used. This data can be used to revise policies.

### - Over 80% in cost savings if managed correctly

- Over 80% in cost savings if managed correctly

### IAM Guideline & Best Practices

IAM Guideline & Best Practices

### - Don’t use root account except for account setup

- Don’t use root account except for account setup
- Each physical user should have its own AWS user
- Assign users to groups and assign permissions to groups
- Create a strong password policy
- Use and enforce MFA
- Create and use Roles for AWS services
- Use access keys for programmatic access (CLI/SDK)
- Audit permissions using IAM Credential Report and Access Advisor
- Never share IAM user’s access keys

### Bootstrapping: launching commands when machine starts

Bootstrapping: launching commands when machine starts
- Script only runs once at the instance first start
- Runs as root user
- Data is used to automate tasks: installing updates, software, downloading files from internet, whatever

### IAM - Identity and Access Management

IAM - Identity and Access Management
It’s a global service

### - Root account created by default

- Root account created by default
- Users = people within the org
- Groups → only contain users, not other groups
  * user can belong to more groups

### IAM Permissions

IAM Permissions
Users and groups can be assigned policies (JSON document)
Policies define user permissions → least privilege principle (don’t give more permissions than a user needs)

### IAM policies inheritance

IAM policies inheritance
- inline policy → attached directly to user
- users inherit the permissions from the groups they belong to, so one user belonging to two groups will inherit more policies.

### IAM policies structure

IAM policies structure
{
  "Version": "2022-10-17",
  "Id": "S3-Account-Permissions",
  "Statement": [
    {
      "Sid": "1",
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam::123456789012:root" },
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": "arn:aws:s3:::mybucket/*"
    }
  ]
}

### ARN → Amazon Resource Name

ARN → Amazon Resource Name
