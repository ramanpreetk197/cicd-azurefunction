pipeline {
    agent any

    environment {
        PYTHON_HOME = 'C:\\Path\\To\\Python' // Update this path to your Python installation
        PATH = "${PYTHON_HOME}\\Scripts;${PYTHON_HOME};${env.PATH}" // Ensure pip and Python are in the PATH
    }

    stages {
        stage('Clone Repository') {
            steps {
                // Cloning the GitHub repository
                git branch: 'main',
                    url: 'https://github.com/ramanpreetk197/cicd-azurefunction.git',
                    credentialsId: 'rm1'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                script {
                    echo 'Installing dependencies...'
                    // Use the absolute path to python if needed
                    bat '"${PYTHON_HOME}\\python.exe" -m pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    try {
                        echo 'Running tests...'
                        bat '"${PYTHON_HOME}\\Scripts\\pytest.exe" --junitxml=test_results.xml'
                    } catch (Exception e) {
                        echo 'Tests failed. Check test results for details.'
                        currentBuild.result = 'UNSTABLE'
                    }
                }
            }
            post {
                always {
                    // Archive test results
                    junit 'test_results.xml'
                }
            }
        }

        stage('Deploy to Azure') {
            steps {
                script {
                    echo 'Deploying to Azure...'
                    bat """
                        REM Login to Azure using Service Principal
                        az login --service-principal ^
                            -u %AZURE_CLIENT_ID% ^
                            -p %AZURE_CLIENT_SECRET% ^
                            --tenant %AZURE_TENANT_ID%

                        REM Package and deploy the function
                        zip -r function.zip *
                        az functionapp deployment source config-zip ^
                            --resource-group %RESOURCE_GROUP% ^
                            --name %FUNCTION_APP_NAME% ^
                            --src function.zip
                    """
                }
            }
            post {
                cleanup {
                    echo 'Cleaning up workspace...'
                    bat 'del /f /q function.zip'
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed.'
        }
        success {
            echo 'Deployment succeeded!'
        }
        failure {
            echo 'Pipeline failed. Check logs for details.'
        }
    }
}
