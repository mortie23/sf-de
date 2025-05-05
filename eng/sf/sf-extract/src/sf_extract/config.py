from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Salesforce configuration settings
SALESFORCE_USERNAME = os.getenv("SALESFORCE_USERNAME")
SALESFORCE_PASSWORD = os.getenv("SALESFORCE_PASSWORD")
SALESFORCE_SECURITY_TOKEN = os.getenv("SALESFORCE_SECURITY_TOKEN")

# You can add more configuration settings as needed
