pipeline {
    agent any

    environment {
        IMAGE_NAME = "crimereporting_image"
        CONTAINER_NAME = "crime_reporting_container"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'master', url: 'https://github.com/PSY-Taruu/crimereporting.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker version'  // To verify Docker is accessible
                    sh "docker build -t $IMAGE_NAME ."
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Stop and remove existing container if any
                    sh "docker rm -f $CONTAINER_NAME || true"
                    // Run container
                    sh "docker run -d -p 5000:5000 --name $CONTAINER_NAME $IMAGE_NAME"
                }
            }
        }
    }
}