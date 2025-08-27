from dotenv import load_dotenv
import os
from sf_extract.salesforce_client import SalesforceClient, list_available_objects
import click
from rich.console import Console
import csv
from pathlib import Path

load_dotenv()  # Load environment variables from .env file
console = Console()

# Retrieve Salesforce credentials from environment variables
username = os.getenv("SALESFORCE_USERNAME")
password = os.getenv("SALESFORCE_PASSWORD")
security_token = os.getenv("SALESFORCE_SECURITY_TOKEN")


def get_csv_reader(csv_path: Path):
    f = open(csv_path, newline="", encoding="utf-8")
    return f, csv.DictReader(f)


@click.command(context_settings=dict(help_option_names=["-h", "--help"]))
@click.option(
    "--query",
    "-q",
    type=str,
    default="unit",
    help="File with list of queries either all or unit",
    show_default=True,
)
def main(query: str):

    # Initialize Salesforce client
    sf_client = SalesforceClient(username, password, security_token)

    config_path = Path("conf")

    # Read from the CSV configuration file
    file, soql_queries = get_csv_reader(config_path / f"{query}.csv")
    try:
        # Loop over all queries from the configuration and execute against SalesForce
        for soql_query in soql_queries:
            sql_path = Path("sql") / soql_query["system_name"]
            sql_filename = (
                f"category-{str(soql_query["category_id"])}-{str(soql_query["query_id"])}.sql"
            )
            query = (sql_path / sql_filename).read_text()
            results = sf_client.query(query)

            if results:
                for record in results:
                    print(record)
    finally:
        file.close()


if __name__ == "__main__":
    main()
