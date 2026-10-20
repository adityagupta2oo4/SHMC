
pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Checking out SHMC from GitHub'
                checkout scm
            }
        }

        stage('Verify Environment') {
            steps {
                bat '"C:\\Users\\hp\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" --version'
                bat 'git --version'
                bat 'docker --version'
            }
        }

        stage('Verify Docker Engine') {
            steps {
                bat 'docker info'
                bat 'docker run --rm hello-world'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'if not exist .venv "C:\\Users\\hp\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" -m venv .venv'
                bat '".venv\\Scripts\\python.exe" -m pip install --upgrade pip'
                bat '".venv\\Scripts\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '".venv\\Scripts\\python.exe" -m pytest -v'
            }
        }
    }

    post {
        success {
            echo 'SHMC CI pipeline completed successfully.'
        }
        failure {
            echo 'SHMC CI pipeline failed. Check the console output.'
        }
    }
}
