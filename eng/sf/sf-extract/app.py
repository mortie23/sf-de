from dotenv import load_dotenv
import os
from sf_extract.salesforce_client import SalesforceClient, list_available_objects


def main():
    load_dotenv()  # Load environment variables from .env file

    # Retrieve Salesforce credentials from environment variables
    username = os.getenv("SALESFORCE_USERNAME")
    password = os.getenv("SALESFORCE_PASSWORD")
    security_token = os.getenv("SALESFORCE_SECURITY_TOKEN")

    # Initialize Salesforce client
    sf_client = SalesforceClient(username, password, security_token)

    # Execute a sample SOQL query
    query = "SELECT Id, Name FROM Contact WHERE Name LIKE '%Shane%'"

    results = sf_client.query(query)

    # Print the results (with error handling)
    if results:
        for record in results:
            print(record)
    else:
        print("No results returned or query failed")


if __name__ == "__main__":
    main()
