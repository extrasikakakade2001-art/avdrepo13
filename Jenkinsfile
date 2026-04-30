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

        stage('Run extract.py') {
            steps {
                bat "${enc.PYTHON} extract.py"
            }
         }  
     }
}
                                     