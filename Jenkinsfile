pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                echo 'Running application tests...'
                bat 'python -m py_compile app.py database.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t devops-order-app:1.0 .'
            }
        }
    }

    post {
        success {
            echo 'CI Pipeline completed successfully!'
        }
        failure {
            echo 'CI Pipeline failed!'
        }
    }
}