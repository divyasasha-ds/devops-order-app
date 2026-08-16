pipeline {
    agent any

    stages {

        stage('Test') {
            steps {
                echo 'Running application tests...'

                sh 'test -f app.py'
                sh 'test -f database.py'
                sh 'test -f Dockerfile'
                sh 'test -f requirements.txt'

                echo 'Application files verified successfully!'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'

                sh 'docker build -t devops-order-app:1.0 .'

                echo 'Docker image built successfully!'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'

                sh 'docker rm -f devops-order-app || true'

                sh 'docker run -d --name devops-order-app -p 5000:5000 devops-order-app:1.0'

                echo 'Application deployed successfully!'
            }
        }

        stage('Verify Deployment') {
            steps {
                echo 'Checking deployed container...'

                sh 'docker ps --filter name=devops-order-app'

                echo 'Deployment verification completed!'
            }
        }
    }

    post {
        success {
            echo 'CI/CD Pipeline completed successfully!'
        }

        failure {
            echo 'CI/CD Pipeline failed!'
        }
    }
}
