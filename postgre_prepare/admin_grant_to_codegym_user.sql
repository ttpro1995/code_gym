


-- Grant all privileges on the database to the user
GRANT ALL PRIVILEGES ON DATABASE codegym TO codegym_user;

GRANT CREATE ON DATABASE codegym TO codegym_user;


-- Connect to the 'codegym' database
\c codegym

-- Grant all privileges on all tables in the database to the user
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO codegym_user;

-- Grant all privileges on all sequences in the database to the user
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO codegym_user;

-- Grant all privileges on all functions in the database to the user
GRANT ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public TO codegym_user;

-- Ensure that the user has the necessary privileges on future tables, sequences, and functions
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON TABLES TO codegym_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON SEQUENCES TO codegym_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON FUNCTIONS TO codegym_user;