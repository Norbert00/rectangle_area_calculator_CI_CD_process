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
                    pip install --upgrade pip
                    poetry config virtualenvs.in-project true
                    poetry env use python3.10
                    poetry update package
                    poetry install                
                """
            }
        }
        stage("Run test") {
            steps {
                script {
                    sh "poetry run pytest"
                }
            }
        }
        stage("Test coverage") {
            steps {
                script {
                    sh "poetry run poetry run pytest --cov=rectangle_calculator"
                }
            }
        }
        stage("Triger job merge dev to main") {
            steps {
                script {
                    currentBuild.resultIsBetterOrEqualTo("SUCCESS")
                    build job: "merge_dev_to_main_rectangle_area_calculator_CI"
                }
            }
            failure {
                echo "Job failed, not triggering merge."
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}