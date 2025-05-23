pipeline {
    agent {
        label 'Built-In Node' // 🖥 Your Jenkins agent's label (Windows node)
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
                cd "%WORKSPACE%"
                mkdir build
                npm install
                echo "== Build Completed! =="
                '''
            }
        }

        stage('Test') {
            steps {
                bat '''
                echo "== Running Tests =="
                cd "%WORKSPACE%"
                npm test
                echo "== Tests Completed! =="
                '''
            }
        }

        stage('Deploy') {
            steps {
                bat '''
                echo "== Deploying Application =="
                echo "== Deploying Successful! =="
                '''
            }
        }
    }
}
