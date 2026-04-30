pipeline {
    agent any

    environment {
        // Define Python path once, so we can reuse it
        PYTHON = 'C:\\Users\\Aiden Pierce\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
    }

    stages {
        stage('Checkout') {
            steps {
                // Pull code from your GitHub repo
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                // Check Python version to confirm it's available
                bat "${env.PYTHON} --version"
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install all required libraries from requirements.txt
                // Make sure you have a requirements.txt file in your repo
                bat "${env.PYTHON} -m pip install -r requirements.txt"
            }
        }

        stage('Extract') {
            steps {
                // Run your Python script after dependencies are installed
                bat "${env.PYTHON} extract.py"
            }
        }
    }
}\