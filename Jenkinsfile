pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'docker-compose -f test.yaml up --build'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
