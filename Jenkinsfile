pipeline {
    agent {
        docker {
            image "norbert00/python3.10_poetry:v1"
            args '-u root:root'
        }
    }

    stages {
        stage("Setup docker container") {
            steps {
                sh """
                    poetry config virtualenvs.in-project true
                    poetry env use python3.10
                    poetry update package
                    poetry install                
                """
            }
        }
        stage("Test coverage") {
            steps {
                script {
                    sh "poetry run poetry run pytest --cov=rectangle_calculator"
                }
            }
        }
    post {
        always {
            cleanWs()
        }
    }
}