pipeline{
    agent any
    stages{
        stage("build"){
            steps{
                bat 'python setup.py bdist_wheel'
            }
        }
        stage("deployee"){
            steps{
                echo "hello"
            }
        }
    }
}
