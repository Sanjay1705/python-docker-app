@Library('jenkins-shared-lib-demo') _   

pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Debug Workspace') {
            steps {
                sh 'pwd'
                sh 'ls -l'
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
