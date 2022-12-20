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
                bat 'copy dis/mypackage-0.0.1-py3-none-any.whl newwheel.whl'
            }
        }
    }
}
