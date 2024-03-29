import subprocess

def check_and_install_packages(requirements_file):
    with open(requirements_file, 'r') as file:
        required_packages = file.readlines()

    for package in required_packages:
        package = package.strip()
        try:
            subprocess.check_call(["pip", "show", package])
            print(f"{package} is already installed.")
        except subprocess.CalledProcessError:
            print(f"Installing {package}...")
            subprocess.check_call(["pip", "install", package])
            print(f"{package} has been installed.")

if __name__ == "__main__":
    requirements_file = "requirements.txt"
    check_and_install_packages(requirements_file)
