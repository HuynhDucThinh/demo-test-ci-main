pipeline {
    agent any
    
    environment {
        PYTHON_VERSION = '3.10'
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Set up Python') {
            steps {
                script {
                    // Sử dụng Python có sẵn trên Jenkins agent
                    sh 'python3 --version'
                }
            }
        }
        
        stage('Install dependencies') {
            steps {
                sh '''
                    python3 -m pip install --upgrade pip
                    pip install ruff pytest coverage
                    if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
                '''
            }
        }
        
        stage('Lint with Ruff') {
            steps {
                sh 'ruff --format=github --target-version=py310 . || true'
            }
        }
        
        stage('Test with pytest') {
            steps {
                sh 'coverage run -m pytest -v -s'
            }
        }
        
        stage('Generate Coverage Report') {
            steps {
                sh 'coverage report -m'
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
