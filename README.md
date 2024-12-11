# cicd-azurefunction

Jenkins CI/CD Pipeline to Deploy Azure Functions
This project sets up a CI/CD pipeline using Jenkins to deploy a Python-based Azure Function. The pipeline integrates with GitHub for source control and uses Azure CLI for deployment.

Project Overview
Azure Function: A simple HTTP-triggered "Hello, World!" function in Python.

Pipeline Stages:
Build: Install dependencies.
Test: Run automated test cases.
Deploy: Deploy to Azure using Azure CLI.

Setup Steps
Azure Function: Create and deploy an HTTP-triggered function in Python.
GitHub: Push code (app.py, requirements.txt, test_function.py, Jenkinsfile) to a new repository.

Jenkins:
Install required plugins (GitHub, Azure CLI, Pipeline).
Add Azure Service Principal credentials.
Create a pipeline linked to the GitHub repository.

Run Pipeline:
Push changes to trigger the Build, Test, and Deploy stages.
Test Cases
Verify HTTP status code 200.
Check the response body contains "Hello, World!".


Run tests with:

bash
Copy code
pytest


Verification
Test the function via the Azure Function URL.
Ensure all pipeline stages succeed in Jenkins.