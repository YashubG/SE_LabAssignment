pipeline {
    agent any

    stages {

        stage('Clone from GitHub') {
            steps {
                git branch: 'main', url: 'https://github.com/YashubG/SE_LabAssignment.git'
            }
        }

        stage('Install dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t YashubG/IMT2023117_Assignment:latest .'
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh 'echo $PASS | docker login -u $USER --password-stdin'
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                sh 'docker push YashubG/IMT2023117_Assignment:latest'
            }
        }
    }
}
