from db import Base, engine
from sqlalchemy import text

# Drop all tables
print("Dropping all tables...")
Base.metadata.drop_all(bind=engine)

# Ensure the tables are dropped
with engine.connect() as connection:
    connection.execute(text("DROP TABLE IF EXISTS urls"))

# Create all tables
print("Creating all tables...")
Base.metadata.create_all(bind=engine)

# Execute the SQL script to set up the database
print("Executing SQL script...")
with engine.connect() as connection:
    with open("db_create.sql") as file:
        query = text(file.read())
        connection.execute(query)

print("Database reset complete.")