pipeline {
    agent any

    environment {
        PATH = "$PATH:/var/lib/jenkins/.local/bin"
        IMAGE_NAME = "yashubg/imt2023117_assignment:latest"
    }

    stages {

        stage('Clone from GitHub') {
            steps {
                git branch: 'main', url: 'https://github.com/YashubG/SE_LabAssignment.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }

        stage('Build & Push Docker Image') {
            steps {
                script {
                    // Use Jenkins Docker credentials to login and push
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub') {
                        // Build the Docker image
                        def appImage = docker.build("${IMAGE_NAME}")
                        // Push image to Docker Hub
                        appImage.push()
                    }
                }
            }
        }

    }

    post {
        success {
            echo "Pipeline finished successfully! Docker image pushed: ${IMAGE_NAME}"
        }
        failure {
            echo "Pipeline failed. Check console logs for errors."
        }
    }
}
