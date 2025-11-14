pipeline {
    agent any

    options {
        // Keep only last 10 builds to save space
        buildDiscarder(logRotator(numToKeepStr: '10'))
        // Timeout in case scan hangs
        timeout(time: 20, unit: 'MINUTES')
    }

    triggers {
        // Optional: Poll SCM or use webhook triggers
        // pollSCM('H/5 * * * *')
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run Gitleaks Secret Scan') {
            steps {
                script {
                    echo "🔍 Running Gitleaks scan for secrets..."

                    // Ensure reports directory exists
                    sh 'mkdir -p reports'

                    // Run Gitleaks via Docker
                    sh """
                    docker run --rm -v \$(pwd):/repo zricethezav/gitleaks:latest \
                        detect --source=/repo \
                        --config=/repo/gitleaks.toml \
                        --report-path=/repo/reports/gitleaks-report.json \
                        --no-banner
                    """

                    // Explicitly fail build if secrets found
                    sh """
                    if [ -s reports/gitleaks-report.json ]; then
                        echo '❌ Secrets detected! Failing the build.'
                        exit 1
                    else
                        echo '✅ No secrets detected.'
                    fi
                    """
                }
            }
        }

    }

    post {
        always {
            echo "📄 Archiving Gitleaks report..."
            archiveArtifacts artifacts: 'reports/gitleaks-report.json', fingerprint: true
        }

        failure {
            echo "🚨 Build failed due to secrets detection!"
        }

        success {
            echo "🎉 Build passed. No secrets found."
        }
    }
}
