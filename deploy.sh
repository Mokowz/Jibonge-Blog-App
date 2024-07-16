# Deploy the application to the server 
# Run this script and install all dependencies

cd Jibonge-Blog-App

# Pull changes made
git pull origin main

# Install dependencies
pip install -r requirements.txt

# Start the gunicorn and nginx server
sudo systemctl restart gunicorn nginx