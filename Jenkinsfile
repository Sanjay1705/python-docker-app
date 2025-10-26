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
                echo "Workspace: ${env.WORKSPACE}"
                sh 'ls -l'
                sh 'cat Dockerfile'
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
