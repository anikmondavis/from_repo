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
               sh 'scp ${WORKSAPCE}/* root@https://github.com/anikmondavis/Deployee_Jenkins.git'
               
            }
        }
    }
}
