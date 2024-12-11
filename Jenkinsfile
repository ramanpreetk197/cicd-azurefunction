pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // Cloning the GitHub repository
                git branch: 'main',
                    url: 'https://github.com/ramanpreetk197/cicd-azurefunction.git',
                    credentialsId: 'rm2'
            }
        }

        stage('Build') {
            steps {
                script {
                    echo 'Installing dependencies...'
                    bat 'pip install -r app/requirements.txt'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    echo 'Running tests...'
                    bat 'pytest tests'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    echo 'Deploying to Azure...'
                    bat """
                        az login --service-principal -u %AZURE_CLIENT_ID% -p %AZURE_CLIENT_SECRET% --tenant %AZURE_TENANT_ID%
                        zip -r app.zip app
                        az functionapp deployment source config-zip --resource-group %RESOURCE_GROUP% --name %FUNCTION_APP_NAME% --src app.zip
                    """
                }
            }
        }
    }
}
