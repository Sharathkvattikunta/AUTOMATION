pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'your-docker-repo/cicd-test-app'
        KUBE_CONFIG = credentials('kubeconfig')
    }
    
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t ${DOCKER_IMAGE}:${BUILD_NUMBER} .'
                sh 'docker tag ${DOCKER_IMAGE}:${BUILD_NUMBER} ${DOCKER_IMAGE}:latest'
            }
        }
        
        stage('Test') {
            steps {
                sh 'python -m pytest tests/'
            }
        }
        
        stage('Push') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo ${DOCKER_PASS} | docker login -u ${DOCKER_USER} --password-stdin'
                    sh 'docker push ${DOCKER_IMAGE}:${BUILD_NUMBER}'
                    sh 'docker push ${DOCKER_IMAGE}:latest'
                }
            }
        }
        
        stage('Deploy to Kubernetes') {
            steps {
                sh "kubectl --kubeconfig=${KUBE_CONFIG} apply -f kubernetes/"
                sh "kubectl --kubeconfig=${KUBE_CONFIG} rollout status deployment/cicd-test-app"
            }
        }
    }
}
