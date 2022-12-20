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
               sh 'scp sample_email.py root@https://github.com/anikmondavis/Deployee_Jenkins.git'
               
            }
        }
    }
}
