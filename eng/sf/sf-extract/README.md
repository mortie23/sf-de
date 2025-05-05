# Extract objects from SalesForce

This will run all the SQL scripts in the SQL directory based on the list in the configuration CSV.

```sh
python3 app.py --query all
```

```log
2025-05-05 14:47:40,042 - INFO - Successfully connected to Salesforce
2025-05-05 14:47:40,051 - INFO - Executing query: select
  count(Id)
from
  account
2025-05-05 14:47:40,553 - INFO - Query returned 1 records
OrderedDict({'attributes': OrderedDict({'type': 'AggregateResult'}), 'expr0': 14})
2025-05-05 14:47:40,559 - INFO - Executing query: select
  count(Id)
from
  contact
2025-05-05 14:47:40,908 - INFO - Query returned 1 records
OrderedDict({'attributes': OrderedDict({'type': 'AggregateResult'}), 'expr0': 21})
2025-05-05 14:47:40,915 - INFO - Executing query: select
  Id
, name
from
  contact
2025-05-05 14:47:41,194 - INFO - Query returned 21 records
OrderedDict({'attributes': OrderedDict({'type': 'Contact', 'url': '/services/data/vM.m/sobjects/Contact/<>hQAE'}), 'Id': '<>hQAE', 'Name': 'Rose Gonzalez'})
OrderedDict({'attributes': OrderedDict({'type': 'Contact', 'url': '/services/data/vM.m/sobjects/Contact/<>iQAE'}), 'Id': '<>iQAE', 'Name': 'Sean Forbes'})
OrderedDict({'attributes': OrderedDict({'type': 'Contact', 'url': '/services/data/vM.m/sobjects/Contact/<>jQAE'}), 'Id': '<>jQAE', 'Name': 'Jack Rogers'})
OrderedDict({'attributes': OrderedDict({'type': 'Contact', 'url': '/services/data/vM.m/sobjects/Contact/<>kQAE'}), 'Id': '<>kQAE', 'Name': 'Pat Stumuller'})
OrderedDict({'attributes': OrderedDict({'type': 'Contact', 'url': '/services/data/vM.m/sobjects/Contact/<>lQAE'}), 'Id': '<>lQAE', 'Name': 'Andy Young'})
OrderedDict({'attributes': OrderedDict({'type': 'Contact', 'url': '/services/data/vM.m/sobjects/Contact/<>mQAE'}), 'Id': '<>mQAE', 'Name': 'Tim Barr'})
OrderedDict({'attributes': OrderedDict({'type': 'Contact', 'url': '/services/data/vM.m/sobjects/Contact/<>nQAE'}), 'Id': '<>nQAE', 'Name': 'John Bond'})
OrderedDict({'attributes': OrderedDict({'type': 'Contact', 'url': '/services/data/vM.m/sobjects/Contact/<>oQAE'}), 'Id': '<>oQAE', 'Name': 'Stella Pavlova'})
OrderedDict({'attributes': OrderedDict({'type': 'Contact', 'url': '/services/data/vM.m/sobjects/Contact/<>pQAE'}), 'Id': '<>pQAE', 'Name': 'Lauren Boyle'})
OrderedDict({'attributes': OrderedDict({'type': 'Contact', 'url': '/services/data/vM.m/sobjects/Contact/<>qQAE'}), 'Id': '<>qQAE', 'Name': 'Babara Levy'})
OrderedDict({'attributes': OrderedDict({'type': 'Contact', 'url': '/services/data/vM.m/sobjects/Contact/<>rQAE'}), 'Id': '<>rQAE', 'Name': 'Josh Davis'})
OrderedDict({'attributes': OrderedDict({'type': 'Contact', 'url': '/services/data/vM.m/sobjects/Contact/<>sQAE'}), 'Id': '<>sQAE', 'Name': 'Jane Grey'})
OrderedDict({'attributes': OrderedDict({'type': 'Contact', 'url': '/services/data/vM.m/sobjects/Contact/<>tQAE'}), 'Id': '<>tQAE', 'Name': 'Arthur Song'})
OrderedDict({'attributes': OrderedDict({'type': 'Contact', 'url': '/services/data/vM.m/sobjects/Contact/<>uQAE'}), 'Id': '<>uQAE', 'Name': 'Ashley James'})
OrderedDict({'attributes': OrderedDict({'type': 'Contact', 'url': '/services/data/vM.m/sobjects/Contact/<>vQAE'}), 'Id': '<>vQAE', 'Name': 'Tom Ripley'})
OrderedDict({'attributes': OrderedDict({'type': 'Contact', 'url': '/services/data/vM.m/sobjects/Contact/<>wQAE'}), 'Id': '<>wQAE', 'Name': "Liz D'Cruz"})
OrderedDict({'attributes': OrderedDict({'type': 'Contact', 'url': '/services/data/vM.m/sobjects/Contact/<>xQAE'}), 'Id': '<>xQAE', 'Name': 'Edna Frank'})
OrderedDict({'attributes': OrderedDict({'type': 'Contact', 'url': '/services/data/vM.m/sobjects/Contact/<>yQAE'}), 'Id': '<>yQAE', 'Name': 'Avi Green'})
OrderedDict({'attributes': OrderedDict({'type': 'Contact', 'url': '/services/data/vM.m/sobjects/Contact/<>zQAE'}), 'Id': '<>zQAE', 'Name': 'Siddartha Nedaerk'})
OrderedDict({'attributes': OrderedDict({'type': 'Contact', 'url': '/services/data/vM.m/sobjects/Contact/?'}), 'Id': '?', 'Name': 'Jake Llorrac'})
OrderedDict({'attributes': OrderedDict({'type': 'Contact', 'url': '/services/data/vM.m/sobjects/Contact/&'}), 'Id': '&', 'Name': 'Shane Warne'})
```
