# EFS

> Auto-generated from raw notes.

## Contents


### EFS - Performance & Storage Class

EFS - Performance & Storage Class

### - EFS Scale

- EFS Scale
  * 1000s of concurrent NFS clients, 10 GB/s+ throughput
  * Grows to Petabyte-scale network file system, automatically

### - Performance Mode (set at EFS creation time)

- Performance Mode (set at EFS creation time)
  * General Purpose (default) → latency-sensitive use cases (web server, CMS, etc.)
  * MAX IO → Higher latency / throughput, highly parallel (big data, media processing)

### - Throughput Mode

- Throughput Mode
  * Bursting — 1TB = 50MiB/s + burst up to 100MiB/s
  * Provisioned — set your throughput regardless of storage size
  * Elastic — automatically scales throughput up or down based on your workload
      - Up to 3 GiB/s for reads and 1 GiB/s writes
      - Used for unpredictable workloads

### EFS - Storage Classes

EFS - Storage Classes
- Storage Tiers (lifecycle management feature) → Move a file after N days
  * Standard — for frequent accessed files
  * Infrequent access (EFS-IA) — cost to retrieve files, lower price to store
  * Archive — rarely accessed objs (few times each year), 80% less cheaper
  * Implement lifecycle policies to move file between storage tiers

### Availability and durability

Availability and durability
- Standard: Multi-AZ, great for prod
- One Zone: One AZ, great for dev, backup enabled by default, compatible with IA (EFS One Zone - IA)
