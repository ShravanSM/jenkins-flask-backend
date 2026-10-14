pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/ShravanSM/jenkins-flask-backend.git',
                    branch: 'main'
            }
        }

        stage('Install dependencies') {
            steps {
                bat '"C:\\Users\\shrav\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Verify application') {
            steps {
                bat '"C:\\Users\\shrav\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" -m py_compile app.py'
            }
        }

        stage('Deploy to EC2') {
            steps {
                sshagent(credentials: ['ec2-ssh-key']) {
                    bat 'ssh -o StrictHostKeyChecking=no ubuntu@15.206.209.74 "cd ~/apps/flask-app && git pull origin main && source venv/bin/activate && pip install -r requirements.txt && pm2 restart flask-backend"'
                }
            }
        }
    }
}
