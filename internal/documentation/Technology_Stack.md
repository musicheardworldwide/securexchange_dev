This document contains the selected technology stack for the SecureXchange project following project preferences and security requirements.

# Technology Stack Selection

- Backend Framework: **Django**
   - Reason: Strong data validation, superior error handling, and built-in encryption tools to ensure secure file handling.
 - Frontend Framework: **React**
   - Reason: Modular and component-based structure for user interaction with a responsive, scalable UI. 
- Database: **PostgreSQL**
    - Reason: Relational database model with encrypted data storage for secure files and user metadata.
- Security Tools: **OpenSSL, JWT**
    - Reason: Used for transmission encryption and user authentication without application sessions stored on the client.
- DfPops Tools: **GitHub Actions**
    - Reason: For continuous inner circle development through all project stages.

Next step: Begin work on the docker containers with setup scripts and configuration files.
