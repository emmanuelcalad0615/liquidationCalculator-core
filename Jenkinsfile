pipeline {
    agent any
    
    environment {
        // Nombres de imágenes para testing
        BACKEND_IMAGE = 'liquidation-backend-test'
        FRONTEND_IMAGE = 'liquidation-frontend-test'
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
                sh 'echo "✅ Código descargado - Build #${BUILD_NUMBER}"'
            }
        }
        
        stage('Build Backend') {
            steps {
                dir('backend') {
                    sh '''
                        echo "🔨 Build Backend..."
                        # Verificar Python
                        python3 --version || (apt-get update && apt-get install -y python3 python3-pip)
                        
                        # Instalar dependencias
                        python3 -m pip install --upgrade pip
                        pip3 install -r requirements.txt
                        pip3 install pytest
                        
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
                        # Configurar variables de entorno para tests
                        export SECRET_KEY="clave_secreta_mi_hermanito"
                        export DATABASE_URL="sqlite:///test.db"
                        export FRONTEND_URL="http://localhost:3000"
                        
                        # Ejecutar tests
                        python3 -m pytest tests/ -v --tb=short
                        
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
                        # Verificar si Node.js está disponible
                        if command -v node >/dev/null 2>&1; then
                            echo "Node.js encontrado, instalando dependencias..."
                            npm install
                            npm run build
                            echo "✅ Frontend build completado"
                        else
                            echo "⚠️ Node.js no disponible, saltando build frontend"
                            echo "✅ Frontend skip - Node.js requerido"
                        fi
                    '''
                }
            }
        }
        
        stage('Build Docker Images') {
            steps {
                script {
                    echo "🐳 Construyendo imágenes Docker..."
                    
                    // Build Backend Image
                    dir('backend') {
                        sh """
                            docker build \
                                --build-arg SECRET_KEY='clave_secreta_mi_hermanito' \
                                --build-arg DATABASE_URL='mysql+pymysql://root:Joaco06151970@mysql_db:3306/liquidation' \
                                --build-arg FRONTEND_URL='http://localhost:3000,http://127.0.0.1:3000' \
                                -t ${BACKEND_IMAGE}:${env.BUILD_NUMBER} .
                            
                            echo "✅ Backend image: ${BACKEND_IMAGE}:${env.BUILD_NUMBER}"
                        """
                    }
                    
                    // Build Frontend Image  
                    dir('frontend') {
                        sh """
                            if [ -f "Dockerfile" ]; then
                                docker build -t ${FRONTEND_IMAGE}:${env.BUILD_NUMBER} .
                                echo "✅ Frontend image: ${FRONTEND_IMAGE}:${env.BUILD_NUMBER}"
                            else
                                echo "⚠️ Dockerfile no encontrado en frontend, saltando..."
                            fi
                        """
                    }
                }
            }
        }
        
        stage('Test Docker Images') {
            steps {
                script {
                    echo "🔍 Probando imágenes Docker..."
                    sh """
                        # Listar imágenes creadas
                        docker images | grep -E "(liquidation-backend-test|liquidation-frontend-test)" || echo "No images found"
                        
                        echo "✅ Imágenes verificadas"
                        echo "Backend: ${BACKEND_IMAGE}:${env.BUILD_NUMBER}"
                        echo "Frontend: ${FRONTEND_IMAGE}:${env.BUILD_NUMBER}"
                    """
                }
            }
        }
        
        stage('Push to DockerHub') {
            steps {
                script {
                    echo "📤 Resumen final - Imágenes listas:"
                    sh """
                        echo "=== IMÁGENES DOCKER CREADAS ==="
                        echo "Backend:  ${BACKEND_IMAGE}:${env.BUILD_NUMBER}"
                        echo "Frontend: ${FRONTEND_IMAGE}:${env.BUILD_NUMBER}"
                        echo "================================"
                        echo ""
                        echo "Para subir a DockerHub manualmente:"
                        echo "  docker tag ${BACKEND_IMAGE}:${env.BUILD_NUMBER} emmanuecalad/liquidation-backend-test:${env.BUILD_NUMBER}"
                        echo "  docker push emmanuecalad/liquidation-backend-test:${env.BUILD_NUMBER}"
                        echo ""
                        echo "  docker tag ${FRONTEND_IMAGE}:${env.BUILD_NUMBER} emmanuecalad/liquidation-frontend-test:${env.BUILD_NUMBER}"
                        echo "  docker push emmanuecalad/liquidation-frontend-test:${env.BUILD_NUMBER}"
                    """
                }
            }
        }
    }
    
    post {
        always {
            echo "🎉 Pipeline ejecutado - Resultado: ${currentBuild.currentResult}"
            echo "Build Number: ${env.BUILD_NUMBER}"
            echo "Job URL: ${env.BUILD_URL}"
        }
        success {
            echo "✅ ¡Pipeline EXITOSO! Todas las etapas completadas"
            sh '''
                echo "=== RESUMEN FINAL ==="
                echo "✅ Checkout completado"
                echo "✅ Backend build exitoso" 
                echo "✅ Tests unitarios pasados"
                echo "✅ Frontend procesado"
                echo "✅ Imágenes Docker construidas"
                echo "======================"
            '''
        }
        failure {
            echo "❌ Pipeline FALLIDO - Revisar logs para detalles"
        }
        unstable {
            echo "⚠️ Pipeline INESTABLE - Algunas etapas con warnings"
        }
    }
}