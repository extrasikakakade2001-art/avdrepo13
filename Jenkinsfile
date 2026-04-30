pipeline {
    agent any 
    enviroment {
        PYTHON = 'C:\\Users\\Aiden Pierce\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
    }
    stages {
        stage ('Checkout Code') {
            steps {
                checkout scm 
            }
        }
        stage ('Show Python Version') {
            steps {
                bat "${env.PYTHON} --Version"
            }
           stage ('Run extract.py') {
               steps {
                bat "${enc.PYTHON} extract.py"
               }
           }  
        }
    }
}                                     