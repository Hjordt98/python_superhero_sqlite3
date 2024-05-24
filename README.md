# Sqlite3 Project with Superhero Theme

## Purpose of this project

The purpose of this project is made to show how I taught myself to learn about sqlite3 using python. I asked Chat-GPT to give me some problems to solve, and each folder is one problem. Some of the code might show up in several folders, and to get the best overview is most likely to see the code in the last folder.

### Problems Chat-GPT gave me

#### Problem 1: Insert Multiple Records

Task: Extend your script to insert multiple superhero records at once.

- Create a list of dictionaries where each dictionary represents a superhero.
- Insert all superheroes into the database using a single transaction.

#### Problem 2: Create a Villains Table

Task: Create a new table for supervillains with a similar structure and insert some records.

- Table name: supervillains
- Fields: id, first_name, last_name, debut_year, villain_name, powers

#### Problem 3: Establish Relationships

Task: Create a table to establish relationships between superheroes and supervillains (e.g., arch-nemeses).

- Table name: hero_villain_relationships
- Fields: id, hero_id, villain_id

Establish some relationships and insert records.

#### Problem 4: Update Records

Task: Write a script to update the powers of a specific superhero.

- Choose a superhero and change their powers.
- Make sure to print out the updated record to verify the change.

#### Problem 5: Delete Records

Task: Write a script to delete a specific superhero or supervillain from the database.

- Choose a superhero or supervillain and delete their record.
- Print the remaining records to verify the deletion.

#### Problem 6: Query with Conditions

Task: Retrieve superheroes who debuted before a certain year.

- Write a query to select all superheroes who debuted before 1950.
- Print the results.

#### Problem 7: Join Queries

Task: Write a script to perform a join query to find the arch-nemesis of a specific superhero.

- Use the hero_villain_relationships table to join the superheroes and supervillains tables.
- Print the results.

#### Problem 8: Create and Use Indexes

Task: Create an index on the release_date field of the superheroes table to improve query performance.

- Create the index.
- Write a query that benefits from this index and measure the performance improvement.

#### Problem 9: Aggregate Functions

Task: Use aggregate functions to get some insights.

- Find the average debut year of all superheroes.
- Count the number of superheroes with a specific power.

#### Problem 10: Backup and Restore

Task: Write scripts to backup and restore the database.

- Create a backup of the current database.
- Write a script to restore the database from the backup file.