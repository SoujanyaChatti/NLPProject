# Database Documentation

This directory contains the database-related components for the AI-Powered English Learning Platform. It includes schemas for user data, progress tracking, and content management, as well as migration scripts for initializing the database.

## Directory Structure

- **schemas/**: Contains JSON schema files that define the structure of the data stored in the database.
  - `user_schema.json`: Schema for user data.
  - `progress_schema.json`: Schema for tracking user progress.
  - `content_schema.json`: Schema for educational content.

- **migrations/**: Contains scripts for database migrations.
  - `init_migration.py`: Script for initializing the database schema.

## Usage

To set up the database, run the migration script located in the `migrations` directory. Ensure that the database server is running and accessible.

## Contributing

If you wish to contribute to the database design or functionality, please follow the project's contribution guidelines and ensure that any changes are well-documented.