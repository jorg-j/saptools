pipeline {
    agent any
    environment {
        HOST="jack@192.168.1.161"
        REPO="https://github.com/jorg-j/saptools.git"
        build_path="/home/jack/jenkins/build"
        TESTS="saptools/tests"

    }
    stages {
        stage('Preparing Build Environment') {
            steps {
                sh 'touch touchfile; rm -r *;'
                sh 'ls; echo $PWD'
                echo 'Dir Created and Cleared'
                }
            }
        
        stage('Pull From Git') {
            steps {
                // Get some code from a GitHub repository
                git credentialsId: 'git-token', url: 'https://github.com/jorg-j/saptools.git'
            }
        }
        stage('Ensuring Build Directory Is Setup') {
            steps {

                sh 'ssh ${HOST} "mkdir -p ${build_path}; touch ${build_path}/touchfile; rm -r ${build_path}/*"'
            }
        }
        stage('Sending to Server') {
            steps {
                sh 'scp -r * ${HOST}:${build_path}/'
            }
        }

        stage('Preparing VENV') {
            steps {
                sh '''
                ssh -t ${HOST} 'bash -s << 'ENDSSH'
                cd $build_path; pip install virtualenv --user; virtualenv venv
                . venv/bin/activate
                pip3 install nose
                nosetests saptools/tests
ENDSSH'
                '''
            }
        }

        //stage('Running Load to DB,') {
        //    steps {
        //        sh 'ssh -t ${HOST} "cd ${pathway}; python3 sql_load.py"'
        //    }
        //}        
        
        }
    }