pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // Check out your source code from version control
                checkout scm
            }
        }
        stage('Build and Deploy') {
            steps {
                // Build your application (if required)
                sh 'mvn clean package'
                // Deploy to AWS Elastic Beanstalk
                awsElasticBeanstalk(application: 'my-app', environment: 'production', region: 'us-east-1')
            }
        }
    }
}
