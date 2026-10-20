pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code checkout will be configured through Jenkins SCM.'
            }
        }

        stage('Verify Environment') {
            steps {
                echo 'SHMC CI pipeline started successfully.'
                bat 'python3 --version'
                bat 'git --version'
            }
        }
    }
}