from simple_salesforce import Salesforce
from simple_salesforce.exceptions import SalesforceError
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class SalesforceClient:
    def __init__(
        self,
        username: str,
        password: str,
        security_token: str,
        domain="login",
    ):
        try:
            self.sf = Salesforce(
                username=username,
                password=password,
                security_token=security_token,
                domain=domain,
            )
            logging.info("Successfully connected to Salesforce")
        except Exception as e:
            logging.error(f"Failed to connect to Salesforce: {str(e)}")
            raise

    def query(
        self,
        soql_query: str,
    ):
        """
        Execute a SOQL query and return the results
        """
        try:
            logging.info(f"Executing query: {soql_query}")
            results = self.sf.query_all(soql_query)
            logging.info(f"Query returned {len(results['records'])} records")
            return results["records"]
        except SalesforceError as e:
            logging.error(f"An error occurred while executing the query: {str(e)}")
            return []
        except Exception as e:
            logging.error(f"Unexpected error during query execution: {str(e)}")
            return []


def list_available_objects(
    sf_client,
):
    """List all available objects in the Salesforce org"""
    try:
        # Get the list of objects from the describe global result
        describe_result = sf_client.sf.describe()

        print("Available objects in your Salesforce org:")
        for obj in describe_result["sobjects"]:
            if obj["queryable"]:
                print(f"- {obj['name']}")

        return describe_result["sobjects"]
    except Exception as e:
        print(f"Error listing objects: {str(e)}")
        return []
