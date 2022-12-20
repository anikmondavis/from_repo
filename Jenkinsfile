pipeline{
    agent any
    stages{
        stage("build"){
            steps{
                git branch: 'main', url: 'https://github.com/anikmondavis/from_repo.git'
                bat 'python sample_email.py'
            }
        }
        stage("deployee"){
            steps{
                  git branch: 'main', url: 'https://github.com/anikmondavis/from_repo.git'
                 sh '''git remote add origin https://github.com/anikmondavis/Deployee_Jenkins.git '''
                 sh ''' git branch -M main '''
                 sh ''' git push -u origin main'''
               
            }
        }
    }
}
