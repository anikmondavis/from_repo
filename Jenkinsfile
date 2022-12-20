pipeline{
    agent any
    stages{
        stage("build"){
            steps{
                bat 'python setup.py bdist_wheel'
                stash(name: 'compiled-results', includes: 'sources/*.whl*')
            }
        }
        stage("deployee"){
            steps{
                 unstash(name: 'compiled-results')
            }
        }
    }
}
