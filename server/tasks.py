import subprocess

def deploy(config,param):
    if param == 'stable':
        subprocess.call(['./scripts/deploy.sh',config['repository_dir'],config['stable_branch'],config['stable_deploy_dir'],param])
        return 0
    elif param == 'testing':
        subprocess.call(['./scripts/deploy.sh',config['repository_dir'],config['testing_branch'],config['testing_deploy_dir'],param])
        return 0
    else:
        message = "Error: wrong deploy parameters"
        print message
        return message
