
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code checkout configured through Jenkins SCM.'
            }
        }

        stage('Verify Environment') {
            steps {
                echo 'SHMC CI pipeline started successfully.'
                bat 'python --version'
                bat 'git --version'
                bat 'docker --version'
            }
        }
    }
}
