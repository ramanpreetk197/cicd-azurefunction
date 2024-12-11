pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // Cloning the GitHub repository
                git branch: 'main', 
                    url: 'https://github.com/ramanpreetk197/cicd-azurefunction.git', 
                    credentialsId: 'rm'
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    echo 'Installing dependencies...'
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    try {
                        echo 'Running tests...'
                        sh 'pytest --junitxml=test_results.xml'
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
                    sh """
                        # Login to Azure using Service Principal
                        az login --service-principal \
                            -u $AZURE_CLIENT_ID \
                            -p $AZURE_CLIENT_SECRET \
                            --tenant $AZURE_TENANT_ID

                        # Package and deploy the function
                        zip -r function.zip *
                        az functionapp deployment source config-zip \
                            --resource-group $RESOURCE_GROUP \
                            --name $FUNCTION_APP_NAME \
                            --src function.zip
                    """
                }
            }
            post {
                cleanup {
                    echo 'Cleaning up workspace...'
                    sh 'rm -f function.zip'
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
