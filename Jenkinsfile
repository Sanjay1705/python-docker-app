@Library('jenkins-shared-lib-demo') _   

pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    buildDockerImage("my-python-app:latest")  
                }
            }
        }
    }
}
