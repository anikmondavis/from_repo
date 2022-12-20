pipeline{
    agent any
    stage{
        stage("build"){
            steps{
                sh "python sample_email.py"
            }
        }
        stage("deployee"){
            steps{
                sh "git init"
                sh "git add ."
                sh 'git commit -m "first commit"'
                sh "git branch -M main"
                sh "git remote add origin https://github.com/anikmondavis/Deployee_Jenkins.git"
                sh "git push -u origin main"
            }
        }
    }
}
