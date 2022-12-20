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
                bat 'git init'
                bat 'git add .'
                bat 'git commit -m "first commit"'
                bat 'git branch -M main'
                bat 'git remote add origin https://github.com/anikmondavis/Deployee_Jenkins.git'
                bat 'git push -u origin main'
            }
        }
    }
}
