import subprocess

def deploy(repo_dir,deploy_branch,deploy_dir,deploy_command):
    subprocess.call(['bash','./scripts/deploy.sh',repo_dir,deploy_branch,deploy_dir,deploy_command])
