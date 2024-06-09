## Issue Summary
On the 8th of June, 2024, from 3:13 PM to 3:50 PM, existing web app users saw missing images, broken layouts, and non-functional interactive elements. The Ubuntu server’s Nginx installation wasn’t listening on port 80, so the CDN couldn’t deliver cached files. However, users could still access the web app. At its peak, the issue resulted in a 502 Bad Gateway error. The root cause was an invalid configuration change on the UFW firewall that disabled connections on port 80.

## Timeline (all times West African)
- 3:12 PM: Firewall configuration edit was done
- 3:23 PM: Firewall configuration push was done
- 3:25 PM: 502 Bad Gateway error begins
- 3:25 PM: Pagers alerted teams
- 3:36 PM: Failed server restart fix
- 3:45 PM: Server log inspection
- 3:50 PM: Successful Firewall configuration rollback
- 3:51 PM: Firewall restart begins
- 3:52 PM: 502 Bad Gateway error fixed

## Root Cause
At 3:12 PM WAT, a configuration change was made in the UFW Firewall configuration to disallow HTTP connections, and it took effect when the firewall was restarted. The change meant that the CDN could not establish a connection on port 80 to deliver static assets like images, stylesheets, and JavaScript files for existing web app users. As the cache couldn’t be delivered, existing users experienced missing images, broken layouts, and non-functional interactive elements.

## Resolution and Recovery
At 3:25 PM WAT, the engineer on call was tipped off by the monitoring systems and began investigating the source of the problem. By 3:36 PM, the engineer attempted a server restart to fix the issue but the issue persisted. Hence, the engineer escalated it to other senior engineers on the team.

By 3:45 PM, upon inspecting the server logs, the engineers identified the root cause of the issue. By 3:50 PM, the Firewall was reconfigured to allow connections on port 80. A minute later, the firewall was restarted,

At 3:52 PM, the issue was fixed and all web app elements loaded properly.

## Corrective and Preventative Measures
After analyzing this incident, we’re taking the following actions to prevent such an occurrence from happening in the future.
Update documentation and give engineers training on the impact of firewall configuration changes.
Put stricter change management protocols in place to review firewall changes.
Enhance our monitoring tools to detect specific port connectivity issues more quickly and alert the engineers.
Integrate automated testing for changes to the firewall configuration to catch issues before deployment.
