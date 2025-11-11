pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub')
        IMAGE_NAME = "andresnjr10/liquidationcalculator-core"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/emmanuelcalad0615/liquidationCalculator-core.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Compilando el proyecto...'
                bat 'mvn clean package -DskipTests=false'
            }
        }

        stage('Test') {
            steps {
                echo 'Ejecutando pruebas unitarias...'
                bat 'mvn test'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Construyendo imagen Docker...'
                bat "docker build -t %IMAGE_NAME%:latest ."
            }
        }

        stage('Push to DockerHub') {
            steps {
                echo 'Publicando imagen en DockerHub...'
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    bat 'echo %PASS% | docker login -u %USER% --password-stdin'
                    bat "docker push %IMAGE_NAME%:latest"
                }
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completado exitosamente.'
        }
        failure {
            echo '❌ Pipeline falló.'
        }
    }
}
