pipeline{
    agent any
    stages{
        stage("build"){
            steps{
                bat 'python sample_email.py'
            }
        }
        stage("deployee"){
            steps{
                 git remote add origin https://github.com/anikmondavis/Deployee_Jenkins.git
                 git branch -M main
                 git push -u origin main
               
            }
        }
    }
}
