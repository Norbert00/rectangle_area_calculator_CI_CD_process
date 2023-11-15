pipeline {
    agent {
        docker {
            image "norbert00/python3.10_poetry:v1"
            args '-u root:root'
        }
    }

    environment {
        GITHUB_CREDENTIALS = credentials('github') // 'github' is the credentials ID
        GITHUB_USERNAME = "${GITHUB_CREDENTIALS_USR}"
        GITHUB_TOKEN = "${GITHUB_CREDENTIALS_PSW}"
        REPO_OWNER = 'Norbert00'
        REPO_NAME = 'rectangle_area_calculator_CI_CD_process'
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
        stage("Test Coverage") {
            steps {
                script {
                    sh "poetry run pytest --cov=rectangle_calculator"
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