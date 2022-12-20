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
               sh '''
               git init
               git add README.md
               git commit -m "first commit"
               git branch -M main
               git remote add origin git@github.com:anikmondavis/Deployee_Jenkins.git
               git push -u origin main
               '''
            }
        }
    }
}
