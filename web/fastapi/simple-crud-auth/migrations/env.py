import os
import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# --- CRITICAL: Add your project directory to the sys.path ---
# This allows Alembic to find your local database.py and models.py files
sys.path.append(os.getcwd())

# Import your database components
from database import Base, SQLALCHEMY_DATABASE_URL
import models  # This ensures all models are loaded for autogenerate

# this is the Alembic Config object
config = context.config

# --- Update the SQLAlchemy URL dynamically ---
# This tells Alembic to use the URL defined in your database.py
config.set_main_option("sqlalchemy.url", SQLALCHEMY_DATABASE_URL)

# Interpret the config file for Python logging.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# --- Set target_metadata ---
# This allows 'autogenerate' to compare models vs database
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, 
            target_metadata=target_metadata,
            # This is recommended for SQLite to handle migrations correctly:
            render_as_batch=True 
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()