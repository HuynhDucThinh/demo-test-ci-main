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
                sh '''
                    python3 --version
                    # Tạo virtual environment
                    python3 -m venv venv
                    # Kích hoạt venv
                    . venv/bin/activate
                    # Upgrade pip
                    pip install --upgrade pip
                '''
            }
        }
        
        stage('Install dependencies') {
            steps {
                sh '''
                    . venv/bin/activate
                    pip install ruff pytest coverage
                    if [ -f requirements.txt ]; then 
                        pip install -r requirements.txt
                    fi
                '''
            }
        }
        
        stage('Lint with Ruff') {
            steps {
                sh '''
                    . venv/bin/activate
                    ruff --format=github --target-version=py310 . || true
                '''
            }
        }
        
        stage('Test with pytest') {
            steps {
                sh '''
                    . venv/bin/activate
                    coverage run -m pytest -v -s
                '''
            }
        }
        
        stage('Generate Coverage Report') {
            steps {
                sh '''
                    . venv/bin/activate
                    coverage report -m
                '''
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
