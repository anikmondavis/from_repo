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
                sh 'git remote add origin "https://github.com/anikmondavis/Deployee_Jenkins.git"'
                sh 'git push -u main main'
               
            }
        }
    }
}
