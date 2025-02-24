pipeline {
    agent any

    stages {
        stage('Clone Git') {
            steps {
                echo "Checkout the source code from the Git repository"
                git branch: 'main', url:'https://github.com/bhavyadora2002/Calculator.git'
            }
        }

        stage('Build') {
            steps {
                echo "Execute build commands or scripts"
                sh "chmod u+x sci_cal.py"
                sh 'python3 sci_cal.py ${choice} ${num1} ${num2}'
            }
        }

        stage('Test') {
            steps {
                echo "Execute test commands or scripts"
                sh "chmod u+x sci_cal_test.py"
                sh 'python3 sci_cal_test.py'
            }
        }
    }
}
