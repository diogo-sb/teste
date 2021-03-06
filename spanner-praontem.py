# Imports the Google Cloud Client Library.
from google.cloud import spanner

# Instantiate a client.
spanner_client = spanner.Client()

# Your Cloud Spanner instance ID.
instance_id = 'praontem'

# Get a Cloud Spanner instance by ID.
instance = spanner_client.instance(instance_id)

# Your Cloud Spanner database ID.
database_id = 'bd-teste'

# Get a Cloud Spanner database by ID.
database = instance.database(database_id)

# Execute a simple SQL statement.
with database.snapshot() as snapshot:
    results = snapshot.execute_sql('SELECT * FROM TEST')

    for row in results:
        print(row)

    print("Marcha na boneca 2012")