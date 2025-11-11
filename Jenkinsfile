pipeline {
    agent any
    
    environment {
        // Nombres DIFERENTES a tus imágenes de producción
        BACKEND_IMAGE = 'emmanuecalad/liquidation-backend-test'
        FRONTEND_IMAGE = 'emmanuecalad/liquidation-frontend-test'
        DOCKERHUB_CREDENTIALS = 'dockerhub-credentials'
    }
    
    stages {
        // PASO 1: Descargar código
        stage('Checkout') {
            steps {
                checkout scm
                sh 'echo "✅ Código descargado"'
            }
        }
        
        // PASO 2: Compilar Backend
        stage('Build Backend') {
            steps {
                dir('backend') {
                    sh '''
                        echo "🔨 Instalando Python dependencias..."
                        pip install -r requirements.txt
                        pip install pytest pytest-cov
                    '''
                }
            }
        }
        
        // PASO 3: Compilar Frontend  
        stage('Build Frontend') {
            steps {
                dir('frontend') {
                    sh '''
                        echo "🔨 Instalando Node.js dependencias..."
                        npm install
                        npm run build
                    '''
                }
            }
        }
        
        // PASO 4: Pruebas Unitarias
        stage('Unit Tests') {
            steps {
                dir('backend') {
                    sh '''
                        echo "🧪 Ejecutando tests..."
                        python -m pytest tests/ -v
                    '''
                }
            }
        }
        
        // PASO 5: Construir imágenes Docker
        stage('Build Docker Images') {
            steps {
                script {
                    echo "🐳 Construyendo imágenes Docker..."
                    
                    // Backend
                    dir('backend') {
                        docker.build("${BACKEND_IMAGE}:${env.BUILD_NUMBER}")
                    }
                    
                    // Frontend
                    dir('frontend') {
                        docker.build("${FRONTEND_IMAGE}:${env.BUILD_NUMBER}")
                    }
                }
            }
        }
        
        // PASO 6: Subir a DockerHub
        stage('Push to DockerHub') {
            steps {
                script {
                    echo "📤 Subiendo a DockerHub..."
                    
                    docker.withRegistry('https://docker.io', "${DOCKERHUB_CREDENTIALS}") {
                        docker.image("${BACKEND_IMAGE}:${env.BUILD_NUMBER}").push()
                        docker.image("${FRONTEND_IMAGE}:${env.BUILD_NUMBER}").push()
                    }
                    
                    echo "✅ TODO LISTO!"
                    echo "Imágenes subidas:"
                    echo "- ${BACKEND_IMAGE}:${env.BUILD_NUMBER}"
                    echo "- ${FRONTEND_IMAGE}:${env.BUILD_NUMBER}"
                }
            }
        }
    }
}