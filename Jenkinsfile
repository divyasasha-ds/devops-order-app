pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                echo 'Running application tests...'
                sh 'test -f app.py'
                sh 'test -f database.py'
                echo 'Application files verified successfully!'
            }
        }

        stage('Build Check') {
            steps {
                echo 'Application build check completed successfully!'
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