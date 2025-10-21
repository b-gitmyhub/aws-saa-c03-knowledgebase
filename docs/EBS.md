# EBS

> Auto-generated from raw notes.

## Contents


### EBS Multi-Attach - io1/io2 family

EBS Multi-Attach - io1/io2 family

### EBS Encryption

EBS Encryption
When you create an encrypted EBS volume you get the following
- Data at rest is encrypted
- Data in flight between instance and volume is encrypted
- Snapshots are encrypted (ALL)
- Volumes created from encrypted snapshots are encrypted
- Encryption/decryption are handled transparently
- Encryption has minimal impact on latency
- EBS Encryption leverages keys from KMS (AES-256)
- Copying an unencrypted volume allows encryption
- Snapshots of encrypted volumes are encrypted

### EBS → Elastic Block Store

EBS → Elastic Block Store

### Network drive → can have some latency due to network

Network drive → can have some latency due to network
- Allows instances to persist data even after their termination
- Some EBS can be multi-attach
- Bound to specific AZ → can be moved to other AZ using snapshots
- Free tier 30GB of EBS storage per month
- Need to specify capacity in advance (size in GB, and IOPS)
- Delete on termination attribute
  * root volume by default has the flag on (Delete on termination)
  * other volumes by default do not have the flag set

### EBS Snapshots

EBS Snapshots
The snapshot is a backup of your EBS volume. There is no need to detach the volume to take the snapshot but is recommended.

### Features:

Features:
- EBS snapshot archive → 75% cheaper, takes 24-72 hrs to restore
- Recycle Bin for EBS snapshots → used to retain deleted snapshots
- Specify retention (from 1 day to years)
- Fast snapshot restore → faster initialization of snapshot to have low latency on the first use. Has a big cost.
