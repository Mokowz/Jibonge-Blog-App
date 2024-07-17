# Deploy the application to the server 
# Run this script and install all dependencies
# Install python and its dependencies
sudo apt install -y python3 python3-pip
sudo pip3 install virtualenv

cd Jibonge-Blog-App

# Pull changes made
git pull origin main

# Activate the virtualenv
virtualvenv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Deactivate the virtual env
deactivate

# Start the gunicorn and nginx server
sudo systemctl restart gunicorn nginx
