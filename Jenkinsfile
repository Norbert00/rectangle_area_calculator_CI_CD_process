pipeline {
    agent {
        docker {
            image "norbert00/python3.10_poetry:v1"
            args '-u root:root'
        }
    }

    stages {
        stage ("Setup docker container") {
            steps {
                sh """
                    pip install --upgrade pip
                    poetry env use python3.10
                    poetry update package
                    poetry config virtualenvs.in-project true 
                    poetry install                
                """
            }
        }
        stage ("Run test") {
            steps {
                script {
                    sh "poetry run pytest"
                }
            }
        }
        stage ("Test coverage") {
            steps {
                script {
                    sh "poetry run poetry run pytest --cov=rectangle_calculator"
                }
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}