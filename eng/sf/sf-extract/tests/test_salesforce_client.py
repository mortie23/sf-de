import pytest
from unittest.mock import MagicMock
import io
from contextlib import redirect_stdout
import sys
import os

# Add the parent directory to sys.path to import the module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sf_extract.salesforce_client import list_available_objects


def test_list_available_objects_success():
    # Create a mock SalesforceClient
    mock_sf_client = MagicMock()

    # Mock data that would be returned by Salesforce describe call
    mock_sobjects = {
        "sobjects": [
            {"name": "Account", "queryable": True},
            {"name": "Contact", "queryable": True},
            {"name": "Opportunity", "queryable": False},
            {"name": "CustomObject__c", "queryable": True},
        ]
    }

    # Configure the mock to return our test data
    mock_sf_client.sf.describe.return_value = mock_sobjects

    # Capture stdout to verify printed output
    captured_output = io.StringIO()
    with redirect_stdout(captured_output):
        result = list_available_objects(mock_sf_client)

    # Verify the correct objects were returned
    assert result == mock_sobjects["sobjects"]

    # Verify the function called describe()
    mock_sf_client.sf.describe.assert_called_once()

    # Verify the correct objects were printed
    output = captured_output.getvalue()
    assert "Available objects in your Salesforce org:" in output
    assert "- Account" in output
    assert "- Contact" in output
    assert "- CustomObject__c" in output
    assert "- Opportunity" not in output  # This one is not queryable
