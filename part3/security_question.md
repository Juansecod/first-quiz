# Security Question

Suppose you are the head of Engineering for an exciting new tech startup that installs solar panels via an app. It's Uber for Solar Panels! You are doing a security audit of your app's infrastructure. You are using the OWASP Top 10 for 2021 as a guide for what security issues might be a problem for you.

Your infrastructure is deployed in Kubernetes containers on Amazon Web Services. It has these components:

- A mobile app for Android and iOS.
- A web frontend that the customer can use instead of the mobile app. This is written in Javascript with Next.js.
- A MySQL database that stores customer information, including passwords, home addresses, telephone numbers, etc. It
also contains customer order information.
- A Python backend implemented in FastAPI. This talks to the database and serves data to both the web frontend and the
mobile apps.

You have 12 software engineer employees who have full access to the system, 3 customer support employees who can view customer information and make changes to orders and accounts, and one sales employee.

Using the OWASP Top 10, what would you look for to make your system secure?

## OWASP Top 10:2021

- ***A01:*** 2021-Broken Access Control

- ***A02:*** 2021-Cryptographic Failures

- ***A03:*** 2021-Injection

- ***A04:*** 2021-Insecure Design

- ***A05:*** 2021-Security Misconfiguration

- ***A06:*** 2021-Vulnerable and Outdated Components

- ***A07:*** 2021-Identification and Authentication Failures

- ***A08:*** 2021-Software and Data Integrity Failures

- ***A09:*** 2021-Security Logging and Monitoring Failures

- ***A10:*** 2021-Server-Side Request Forgery

## How to make a system secure

1. ***Mobile App (Android and iOS):***
    - They should implement appropriate access controls to ensure that users can only access functionalities and data for which they have permission.

    - Use secure authentication, preferably with multi-factor authentication (MFA), to protect user accounts in the mobile application.

    - Conduct security testing on the mobile application to identify injection vulnerabilities, such as code injection, and authentication vulnerabilities (A07).

2. ***Web Frontend (Next.js):***
    - Apply a strict access control strategy in the web application to ensure that users cannot access unauthorized resources (A01).

    - Use strong encryption and SSL/TLS certificates to protect communication between the client and the server, preventing cryptographic vulnerabilities (A02).

    - Avoid injection vulnerabilities, such as cross-site scripting (XSS), and ensure that output is properly filtered (A03).

3. ***MySQL Database:***
    - Configure a role-based access control policy to ensure that users and applications can only access authorized data (A01).

    - Ensure that sensitive data is stored encrypted in the database (A08).

    - Conduct audits and activity tracking to identify unauthorized access and data modifications (A09).

4. ***Python Backend (FastAPI):***
    - Implement proper identification and authentication management to ensure that only authenticated users have access to functionalities (A07).

    - Avoid injection vulnerabilities (A03) by using parameterized queries or an ORM to access the database.

    - Use access controls to ensure that users can only perform authorized actions (A01).

5. ***Component Security (A06):***
    - Conduct a third-party component analysis in your application to identify and update vulnerable and obsolete components using vulnerability scanning tools.

6. ***Secure Configuration (A05):***
    - Perform regular security audits to ensure that your AWS and Kubernetes configurations are secure and follow best practices.

7. ***Server-Side Request Forgery (A10):***
    - Validate and filter all input requests, especially those that can trigger server requests from the client.

8. ***Data Integrity (A08):***
    - Implement measures to ensure data integrity, such as the use of digital signatures and proper access controls to prevent unauthorized data modifications.

9. ***Logging and Monitoring (A09):***
    - Establish a logging and monitoring system that alerts about suspicious or anomalous activities in real-time and retains records for later review.
