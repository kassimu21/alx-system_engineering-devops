Background Context

Any software system will eventually fail, and that failure can come stem from a wide range of possible factors: bugs, traffic spikes, security issues, hardware failures, natural disasters, human error… Failing is normal and failing is actually a great opportunity to learn and improve. Any great Software Engineer must learn from his/her mistakes to make sure that they won’t happen again. Failing is fine, but failing twice because of the same issue is not.

A postmortem is a tool widely used in the tech industry. After any outage, the team(s) in charge of the system will write a summary that has 2 main goals:

To provide the rest of the company’s employees easy access to information detailing the cause of the outage. Often outages can have a huge impact on a company, so managers and executives have to understand what happened and how it will impact their work.
And to ensure that the root cause(s) of the outage has been discovered and that measures are taken to make sure it will be fixed.
Resources
Read or watch:

Incident Report, also referred to as a Postmortem
The importance of an incident postmortem process
What is an Incident Postmortem?

My first postmortem

ISSUE SUMMARY

From 7:00 AM to 10:30 AM GMT, urgent requests for Full Throttle RC APIs resulted in 500 and 504 error response messages.  My company's mobile applications that rely on the aforementioned APIs also returned similar errors. At its peak, the issue affected 80% of traffic to this API infrastructure. Users could continue to access specific APIs that run on separate infrastructures. The root cause of this outage was a syntax error in the SQL queries and wrong file imports. 

TIMELINE

11:19 AM:  Deployment push begins
11:26 AM: Outage begins
11:26 AM: Pagers alerted teams
11:54 AM: Failed configuration change rollback
12:15 PM: Successful configuration change rollback
12:19 PM: Server restarts begin
12:58 PM: 100% of traffic back online

ROOT CAUSE

At 11:19 AM PT, a deployment has the newly configured code released into production. The new code pushed has SQL syntax errors, and some files were wrongly imported.  Since the errors were not correctly handled in the system, this led to a system-wide breakdown of the entire system.   c
Resolution and recovery

CORRECTIVE AND PREVENTATIVE MEASURES

The errors were fixed by uploading new code to the server with errors fixed. 
To avoid getting into a similar situation next time: 
Test code before uploading
Use canary deployment
Build CI/CD pipelines

