# ALX Postmortem
**_By:_**
# ArtaxJay Oluwajuwon

## Issue Summary:
- Duration: The outage occurred on March 5, 2024, from 10:04 AM to 12:37 PM (GMT+1).
- Impact: The primary service affected was the user authentication system, resulting in users experiencing login failures and inability to access their accounts. Approximately 30% of users were affected during the peak of the outage.

## Root Cause:
The root cause of the outage was identified as a misconfiguration in the database replication setup. Due to a recent update in the database schema, the replication process was not properly synchronized across all nodes, leading to inconsistencies and intermittent failures in user authentication requests.

## Timeline:
- 10:04 AM: Issue detected as monitoring alerts indicated a spike in failed login attempts.
- 10:10 AM: Engineering team, me, notified after multiple customer complaints regarding login failures.
- 10:21 AM: Initial investigation focused on network connectivity and server load.
- 10:45 AM: Misleading assumption made that the issue was related to a recent software deployment.
- 11:09 AM: Issue escalated to database administrators for further investigation.
- 11:33 AM: Database replication misconfiguration identified as the root cause.
- 12:03 PM: Configuration changes applied to correct the replication setup.
- 12:37 PM: Service fully restored, and user authentication system back to normal operation.

## Root Cause and Resolution:
The misconfiguration in the database replication setup caused inconsistencies in user authentication data across nodes, leading to login failures. To resolve the issue, database administrators reconfigured the replication process to ensure proper synchronization among all nodes. Additionally, automated checks were implemented to detect and prevent similar misconfigurations in the future.

## Corrective and Preventative Measures:
- Improve documentation and training for database administrators on database replication setup and configuration.
- Implement automated monitoring and alerting for database replication status and consistency.
- Conduct regular audits of database configurations to identify and address potential misconfigurations.
- Task: Update database replication setup documentation with detailed steps and best practices.
- Task: Schedule regular training sessions for database administrators on database configuration management.
- Task: Implement automated tests to validate database replication consistency after schema updates.
