pipeline {
    agent {
        docker {
            image "norbert00/python3.10_poetry:v1"
            args '-u root:root'
        }
    }

    environment {
        GITHUB_CREDENTIALS = credentials('github') // 'github' is the credentials ID
        GITHUB_USERNAME = GITHUB_CREDENTIALS_USR
        GITHUB_TOKEN = GITHUB_CREDENTIALS_PSW
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
        stage("GitHub API Request") {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: GITHUB_CREDENTIALS, usernameVariable: 'GITHUB_USERNAME_USR', passwordVariable: 'GITHUB_USERNAME_PSW')]) {
                        def curlCommand = "curl -u ${GITHUB_USERNAME_USR}:${GITHUB_USERNAME_PSW} \
                            -d '{\"conclusion\": \"success\", \"name\": \"Jenkins\", \"output\": {\"title\": \"Tests Passed\", \"summary\": \"All tests passed successfully.\"}}' \
                            -H 'Accept: application/vnd.github.v3+json' \
                            -X POST https://api.github.com/repos/${REPO_OWNER}/${REPO_NAME}/check-runs"
                        
                        sh curlCommand
                    }
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