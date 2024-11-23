from neo4j import GraphDatabase

# Configure Neo4j connection
neo4j_uri = "neo4j+s://c6ab7e4d.databases.neo4j.io"  # Corrected URI
neo4j_user = "neo4j"  # Default username
neo4j_password = "ju4lJVXYMSSJNhtj97YUDgSalrM8OfORctIAhgt1zds"  # Password

# Connect to Neo4j
driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_user, neo4j_password))

# Test query
def test_connection():
    with driver.session() as session:
        greeting = session.run("RETURN 'Connection successful!' AS message")
        for record in greeting:
            print(record["message"])

test_connection()

