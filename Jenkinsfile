pipeline{
    agent any
    stages{
        stage("build/deploy"){
            steps{
                bat 'python setup.py bdist_wheel'
            }
        }
    }
}
