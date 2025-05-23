pipeline {
    agent {
        label 'Built-In Node' // 🖥 Jenkins agent (adjust if needed)
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/FreshCola/CSY3056.git'
            }
        }

        stage('Build') {
            steps {
                bat '''
                echo "== Starting Build =="
                echo "Nothing to build for Python"
                echo "== Build Completed =="
                '''
            }
        }

        stage('Test') {
            steps {
                bat '''
                echo "== Running Tests =="
                python -m unittest discover
                echo "== Tests Completed =="
                '''
            }
        }

        stage('Deploy') {
            steps {
                bat '''
                echo "== Deploying Application =="
                echo "Deployment Successful (Simulated)"
                '''
            }
        }
    }
}