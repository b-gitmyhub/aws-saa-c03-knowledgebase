# EC2

> Auto-generated from raw notes.

## Contents


### - Up to MAX 16 EC2 instances at a time

- Up to MAX 16 EC2 instances at a time
- Must use filesystem that is cluster-aware

### Amazon EFS — Elastic File System

Amazon EFS — Elastic File System
- Managed NFS (Network File System) that can be mounted on many EC2
- EFS works with EC2 instances in many AZ
- Highly available, scalable, expensive (3x gp2), pay per use
- Use case:
    - content management
    - web serving
    - data sharing
    - Wordpress
- Uses NFSv4.1 protocol
- Uses security group to control access to EFS
- Compatible with Linux-based AMI (not with Windows one)
- POSIX file system (on Linux) that has a standard file API
- File system scales automatically, pay per use, no capacity planning

### Amazon EC2

Amazon EC2

### EC2 → Elastic Compute Cloud → infrastructure as a service

EC2 → Elastic Compute Cloud → infrastructure as a service
- renting virtual machines (EC2)
- storing data on virtual drives (EBS)
- distributing load across machines (ELB)
- scaling services using Auto Scaling Group (ASG)

### Sizing and Configuration Options

Sizing and Configuration Options
- OS: Linux, Windows, Mac
- Compute power (CPU)
- RAM
- Storage → EBS, EFS, EC2 Instance Store
- Network Card
- Firewall rules → Security Groups
- Bootstrap script (EC2 User Data)

### AMI → Amazon Machine Image

AMI → Amazon Machine Image
It’s a customization of an EC2 instance.
- You can add your own software, configuration, OS, monitoring
- Faster boot / config time
- Are built for a specific region
- Can be launched from:
  * A public AMI → AWS provided
  * Your own AMI → you build and maintain yourself
  * An AWS Marketplace AMI → an AMI someone else made (and possibly sells)

### AMI process (from an EC2 instance)

AMI process (from an EC2 instance)
- Start an instance and customize it
- Stop the instance (to ensure data integrity)
- Build an AMI → this will create EBS snapshots
- Launch instance from other AMI
