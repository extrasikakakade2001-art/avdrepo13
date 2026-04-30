pipeline {
    agent any 


    environment {
        PYTHON = 'C:\\Users\\Aiden Pierce\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
    }

    stages {
        stage('Checkout Code') {
            steps {
              checkout scm 
            }
        }

        stage('Show Python version') {
            steps {
                bat "${env.PYTHON} --version"
            }
        }
        stage('install dependencies') {
            steps{
                bat "${env.PYTHON} -m pip install -r requirements.txt "
            }
        }
        stage('Run extract.py') {
            steps {
                bat "${env.PYTHON} extract.py"
            
            }
         }  
     }
}
                                     