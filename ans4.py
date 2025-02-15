import subprocess
import sys
import logging
from datetime import datetime


logging.basicConfig(filename='package_update.log', level=logging.ERROR, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def check_updates():
   
    try:
        if subprocess.run(["which", "apt"], stdout=subprocess.PIPE).returncode == 0:
            package_manager = "apt"
            update_command = ["sudo", "apt", "update"]
            upgrade_command = ["sudo", "apt", "list", "--upgradable"]
    
        else:
            print("Unsupported package manager. This script supports apt and yum.")
            sys.exit(1)

       
        subprocess.run(update_command, check=True)

        
        result = subprocess.run(upgrade_command, stdout=subprocess.PIPE, text=True, check=True)
        upgradable_packages = result.stdout.splitlines()

        if not upgradable_packages:
            print("No updates available.")
            sys.exit(0)

        print("Available updates:")
        for i, package in enumerate(upgradable_packages):
            print(f"{i + 1}. {package}")

        return package_manager, upgradable_packages

    except subprocess.CalledProcessError as e:
        logging.error(f"Error checking for updates: {e}")
        print("Failed to check for updates. Check the log for details.")
        sys.exit(1)

def install_updates(package_manager, packages=None):
    
    try:
        if package_manager == "apt":
            if packages:
                install_command = ["sudo", "apt", "install"] + packages
            else:
                install_command = ["sudo", "apt", "upgrade", "-y"]
        

        subprocess.run(install_command, check=True)
        print("Updates installed successfully.")

    except subprocess.CalledProcessError as e:
        logging.error(f"Error installing updates: {e}")
        print("Failed to install updates. Check the log for details.")

def main():
    package_manager, upgradable_packages = check_updates()

    if not upgradable_packages:
        return

    user_input = input("Do you want to update all packages at once? (yes/no): ").strip().lower()
    if user_input == "yes":
        install_updates(package_manager)
    else:
        package_index = input("Enter the index number of the package you want to update: ").strip()
        try:
            package_index = int(package_index) - 1
            if 0 <= package_index < len(upgradable_packages):
                package_name = upgradable_packages[package_index].split()[0]
                install_updates(package_manager, [package_name])
            else:
                print("Invalid package index.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()