pipeline {
    agent any
    
    environment {
        // Nombres de imágenes CON tu usuario de DockerHub
        BACKEND_IMAGE = 'emmanuecalad/liquidation-backend-test'
        FRONTEND_IMAGE = 'emmanuecalad/liquidation-frontend-test'
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
                sh 'echo "✅ Código descargado - Build #${BUILD_NUMBER}"'
            }
        }
        
        stage('Setup Environment') {
            steps {
                sh '''
                    echo "🔧 Configurando entorno..."
                    apt-get update
                    apt-get install -y python3-venv
                    echo "✅ Entorno configurado"
                '''
            }
        }
        
        stage('Build Backend') {
            steps {
                dir('backend') {
                    sh '''
                        echo "🔨 Build Backend..."
                        
                        python3 -m venv venv
                        . venv/bin/activate
                        
                        pip install --upgrade pip
                        pip install -r requirements.txt
                        pip install pytest
                        
                        echo "✅ Backend dependencies instaladas"
                    '''
                }
            }
        }
        
        stage('Unit Tests') {
            steps {
                dir('backend') {
                    sh '''
                        echo "🧪 Ejecutando tests..."
                        
                        . venv/bin/activate

                        export SECRET_KEY="clave_secreta_mi_hermanito"
                        export DATABASE_URL="sqlite:///test.db"
                        export FRONTEND_URL='["http://localhost:3000", "http://127.0.0.1:3000"]'
                        
                        python -m pytest tests/ -v --tb=short
                        
                        echo "✅ Tests completados"
                    '''
                }
            }
        }
        
        stage('Build Frontend') {
            steps {
                dir('frontend') {
                    sh '''
                        echo "🔨 Build Frontend..."

                        if ! command -v node >/dev/null 2>&1; then
                            echo "⚠️ Node.js no disponible, instalando..."
                            apt-get install -y nodejs npm
                        fi

                        npm install

                        # Construcción sin warnings que bloqueen el build
                        CI=false npm run build

                        echo "✅ Frontend build completado"
                    '''
                }
            }
        }
        
        stage('Build Docker Images') {
            steps {
                script {
                    echo "🐳 Construyendo imágenes Docker..."
                    
                    dir('backend') {
                        sh """
                            docker build \
                                --build-arg SECRET_KEY='clave_secreta_mi_hermanito' \
                                --build-arg DATABASE_URL='mysql+pymysql://root:Joaco06151970@mysql_db:3306/liquidation' \
                                --build-arg FRONTEND_URL='["http://localhost:3000", "http://127.0.0.1:3000"]' \
                                -t ${BACKEND_IMAGE}:${env.BUILD_NUMBER} .

                            echo "✅ Backend image: ${BACKEND_IMAGE}:${env.BUILD_NUMBER}"
                        """
                    }
                    
                    dir('frontend') {
                        sh """
                            docker build -t ${FRONTEND_IMAGE}:${env.BUILD_NUMBER} .
                            echo "✅ Frontend image: ${FRONTEND_IMAGE}:${env.BUILD_NUMBER}"
                        """
                    }
                }
            }
        }
        
        stage('Push to DockerHub') {
            steps {
                script {
                    echo "📤 Subiendo imágenes a DockerHub..."
                    
                    sh """
                        docker login -u emmanuecalad -p tu_password_dockerhub

                        docker push ${BACKEND_IMAGE}:${env.BUILD_NUMBER}
                        docker push ${FRONTEND_IMAGE}:${env.BUILD_NUMBER}

                        docker tag ${BACKEND_IMAGE}:${env.BUILD_NUMBER} ${BACKEND_IMAGE}:latest
                        docker tag ${FRONTEND_IMAGE}:${env.BUILD_NUMBER} ${FRONTEND_IMAGE}:latest

                        docker push ${BACKEND_IMAGE}:latest
                        docker push ${FRONTEND_IMAGE}:latest

                        echo "✅ Imágenes subidas exitosamente"
                    """
                }
            }
        }
    }
    
    post {
        always {
            echo "🎉 Pipeline terminado - Resultado: ${currentBuild.currentResult}"
            echo "Build Number: ${env.BUILD_NUMBER}"
            sh 'rm -rf backend/venv || true'
        }
        success {
            echo "✅ ¡Pipeline EXITOSO!"
        }
        failure {
            echo "❌ Pipeline FALLIDO"
        }
    }
}
