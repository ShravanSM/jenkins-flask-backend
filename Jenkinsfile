pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/ShravanSM/jenkins-flask-backend.git', branch: 'main'
            }
        }
        stage('Install dependencies') {
            steps {
                bat '"C:\\Users\\shrav\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" -m pip install -r requirements.txt'
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
