pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'REPLACE_WITH_FLASK_GITHUB_REPOSITORY_URL'
            }
        }
        stage('Install dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }
        stage('Verify application') {
            steps {
                bat 'python -m py_compile app.py'
            }
        }
        stage('Deploy to EC2') {
            steps {
                echo 'Deployment stage placeholder: configure EC2 deployment credentials and commands before enabling this stage.'
            }
        }
    }
}
