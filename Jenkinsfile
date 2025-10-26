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
                sh 'cat Dockerfile'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // '.' points to repo root where Dockerfile exists
                    buildDockerImage("my-python-app:latest", '.')
                }
            }
        }
    }
}
