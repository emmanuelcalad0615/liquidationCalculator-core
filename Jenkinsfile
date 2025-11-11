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
                        
                        # Crear y activar virtual environment
                        python3 -m venv venv
                        . venv/bin/activate
                        
                        # Instalar dependencias en el virtual environment
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
                        
                        # Activar virtual environment
                        . venv/bin/activate
                        
                        # Configurar variables de entorno EXACTAMENTE como Pydantic las espera
                        export SECRET_KEY="clave_secreta_mi_hermanito"
                        export DATABASE_URL="sqlite:///test.db"
                        export FRONTEND_URL='["http://localhost:3000", "http://127.0.0.1:3000"]'  # ¡EXACTO formato JSON!
                        
                        # Ejecutar tests
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
                        # Verificar si Node.js está disponible
                        if command -v node >/dev/null 2>&1; then
                            echo "Node.js encontrado, instalando dependencias..."
                            npm install
                            npm run build
                            echo "✅ Frontend build completado"
                        else
                            echo "⚠️ Node.js no disponible, instalando..."
                            apt-get install -y nodejs npm
                            npm install
                            npm run build
                            echo "✅ Frontend build completado"
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
                            echo "Construyendo imagen backend..."
                            docker build \\
                                --build-arg SECRET_KEY='clave_secreta_mi_hermanito' \\
                                --build-arg DATABASE_URL='mysql+pymysql://root:Joaco06151970@mysql_db:3306/liquidation' \\
                                --build-arg FRONTEND_URL='["http://localhost:3000", "http://127.0.0.1:3000"]' \\
                                -t ${BACKEND_IMAGE}:${env.BUILD_NUMBER} .
                            
                            echo "✅ Backend image: ${BACKEND_IMAGE}:${env.BUILD_NUMBER}"
                        """
                    }
                    
                    // Build Frontend Image  
                    dir('frontend') {
                        sh """
                            echo "Construyendo imagen frontend..."
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
                        echo "=== SUBIENDO IMÁGENES A DOCKERHUB ==="
                        echo "Backend: ${BACKEND_IMAGE}:${env.BUILD_NUMBER}"
                        echo "Frontend: ${FRONTEND_IMAGE}:${env.BUILD_NUMBER}"
                        
                        # Login a DockerHub (reemplaza con tu password real)
                        docker login -u emmanuecalad -p tu_password_dockerhub
                        
                        # Push de las imágenes
                        docker push ${BACKEND_IMAGE}:${env.BUILD_NUMBER}
                        docker push ${FRONTEND_IMAGE}:${env.BUILD_NUMBER}
                        
                        # También push latest
                        docker tag ${BACKEND_IMAGE}:${env.BUILD_NUMBER} ${BACKEND_IMAGE}:latest
                        docker tag ${FRONTEND_IMAGE}:${env.BUILD_NUMBER} ${FRONTEND_IMAGE}:latest
                        docker push ${BACKEND_IMAGE}:latest
                        docker push ${FRONTEND_IMAGE}:latest
                        
                        echo "✅ Imágenes subidas exitosamente a DockerHub"
                    """
                }
            }
        }
    }
    
    post {
        always {
            echo "🎉 Pipeline terminado - Resultado: ${currentBuild.currentResult}"
            echo "Build Number: ${env.BUILD_NUMBER}"
            // Limpiar virtual environment
            sh 'rm -rf backend/venv || true'
        }
        success {
            echo "✅ ¡Pipeline EXITOSO! Todas las etapas completadas"
            sh '''
                echo "=== 🎊 PIPELINE COMPLETADO 🎊 ==="
                echo "✅ Checkout exitoso"
                echo "✅ Backend build y tests"
                echo "✅ Frontend build" 
                echo "✅ Imágenes Docker construidas"
                echo "✅ Imágenes subidas a DockerHub"
                echo ""
                echo "=== 📦 IMÁGENES PUBLICADAS ==="
                echo "Backend:  emmanuecalad/liquidation-backend-test:${BUILD_NUMBER}"
                echo "Backend:  emmanuecalad/liquidation-backend-test:latest"
                echo "Frontend: emmanuecalad/liquidation-frontend-test:${BUILD_NUMBER}"
                echo "Frontend: emmanuecalad/liquidation-frontend-test:latest"
                echo "==============================="
            '''
        }
        failure {
            echo "❌ Pipeline FALLIDO - Revisar logs para detalles"
        }
    }
}