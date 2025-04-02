# CSV to SQL Script

## CSV to SQL Script
CSV to SQL Converter is a simple and intuitive Python GUI application that converts a CSV file into an SQL script compatible with Microsoft SQL Server. The generated script includes:
- Database creation with collation `Latin1_General_100_CI_AS_SC_UTF8`.
- Table creation based on the CSV file name.
- Data insertion statements for each row in the CSV file.

![alt text](https://github.com/hipolitorodrigues/assets-for-github/blob/373671accf24bbada67b5d866b5f6946dc5cf35f/images/01/img-csv_to_sql.png)

The application is built with `Tkinter` for a modern and responsive user interface.

## Features
- Select a CSV file via the GUI.
- Automatically infer column data types for SQL Server.
- Generate an SQL script with `CREATE DATABASE`, `CREATE TABLE`, and `INSERT` statements.
- User-friendly interface.

## Requirements
Ensure you have the following dependencies installed:

```sh
pip install pandas ttkbootstrap
```

## Usage
1. Run the Python script:

```sh
python csv_to_sql.py
```

2. Select a CSV file.
3. Enter the desired database name.
4. Click `Generate SQL Script` to create the `.sql` file.
5. The script will be saved in the same directory as the CSV file.

## Example Output
An example SQL script generated from a CSV named `DimClients.csv`:

```sql
CREATE DATABASE MyDatabase COLLATE Latin1_General_100_CI_AS_SC_UTF8;
GO
USE MyDatabase;

CREATE TABLE [DimClients] (
    [id] INT PRIMARY KEY,
    [name] NVARCHAR(255),
    [email] NVARCHAR(255),
    [age] INT
);

INSERT INTO [DimClients] VALUES (1, 'John Doe', 'john@example.com', 30);
INSERT INTO [DimClients] VALUES (2, 'Jane Smith', 'jane@example.com', 25);
```

## Autor

- **Developer**: Hipolito Rodrigues
- **Creation Date**: 04/02/2025
- **Last Update**: 04/02/2025
- **Current Version**: 1.1

---

## 📜 License

This project is licensed under the MIT License. This means you are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software, as long as you keep the original copyright notice and license included in all copies or substantial portions of the software.
