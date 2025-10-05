# Normalization in Database

**What is normalization in database?**


- Process of organizing data
- Creating smaller tables and connecting them with relationships
- Updates done easier
- Easier to understand 
- Reduces redundancy (duplicates)
- Improves data integrity (backups, validation)


**3 Types of normalization levels:**

- 1NF (First Normal Form)
- 2NF (Second Normal Form)
- 3NF (Third Normal Form)



**1NF**


In 1NF we need to apply a set of rules to the table for 1NF to be vaild, these include:


- All fields (columns) --> must be unique in each table (no two columns can be the same)
- Values in field must come from the same domain --> e.g. "name" field should only have names
- Values must be atomic --> one each cell only holds single value
- No two records (rows) can be identical --> same name appearing twice within the record (row)
- All tables must have a primary key --> a primary key is unique identifier 

**Once these rules have been applied we can move onto the next normal form**


**2NF**


In 2NF we have another set of rules to apply to the table so 2NF can be valid, these include:


- It is already in 1NF --> this means we must apply 1NF rules first before we can access 2NF
- No partial dependencies --> Each non-key attribute must depend on the entire primary key not just part of it (if its a composite key)


**Composite Key:** Two or more unique identifiers which, alone make no sense but when paired --> gives full meaning and uniquely identify each row (record)

Once table is in 2NF we can now access 3NF


**3NF**

In 3NF we apply the last rule, which is:

- No Transitive dependency, ensuring that all columns in tables ONLY depend on the primary key and don't go through another column.


**example**


StudentID - StudentName - Department - DeptHead


In this case **StudentID** is our primary key
*StudentName* depends on **StudentID**
*Department* depends on **StudentID**
*DeptHead* does NOT depend on **StudentID**
It depends on *Department* (knowning StudentID won't tell you DeptHead, you need to know Department first)
Which to fix we create a separate table (Department as PK and Depthead)


Once these 3NF is valid, data can be sent for analysis