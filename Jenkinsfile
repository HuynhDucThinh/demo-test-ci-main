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
                    # Kiểm tra và cài pip nếu chưa có
                    if ! python3 -m pip --version 2>/dev/null; then
                        curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
                        python3 get-pip.py --user
                        rm get-pip.py
                    fi
                    
                    # Upgrade pip và cài dependencies
                    python3 -m pip install --upgrade pip --user
                    python3 -m pip install ruff pytest coverage --user
                    
                    # Cài requirements.txt nếu có
                    if [ -f requirements.txt ]; then 
                        python3 -m pip install -r requirements.txt --user
                    fi
                '''
            }
        }
        
        stage('Lint with Ruff') {
            steps {
                sh 'python3 -m ruff --format=github --target-version=py310 . || true'
            }
        }
        
        stage('Test with pytest') {
            steps {
                sh 'python3 -m coverage run -m pytest -v -s'
            }
        }
        
        stage('Generate Coverage Report') {
            steps {
                sh 'python3 -m coverage report -m'
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
