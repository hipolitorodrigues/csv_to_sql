import pandas as pd
import os
import tkinter as tk
from tkinter import filedialog, messagebox
import ttkbootstrap as ttk

# Function to map Pandas data types to SQL Server data types
def infer_sql_type(dtype: str) -> str:
    """Maps Pandas data types to SQL Server data types."""
    if "int" in dtype:
        return "INT"
    elif "float" in dtype:
        return "FLOAT"
    elif "bool" in dtype:
        return "BIT"
    elif "datetime" in dtype:
        return "DATETIME"
    else:
        return "NVARCHAR(255)"

# Function that converts a CSV file into an SQL script
def csv_to_sql(csv_path: str, db_name: str):
    """Converts a CSV file into an SQL script."""
    table_name = os.path.splitext(os.path.basename(csv_path))[0]
    df = pd.read_csv(csv_path)
    
    # Generate table column definitions
    columns_sql = []
    for col, dtype in df.dtypes.items():
        sql_type = infer_sql_type(str(dtype))
        constraints = "PRIMARY KEY" if col.lower() == "id" else ""
        columns_sql.append(f"    [{col}] {sql_type} {constraints}".strip())
    
    # Create SQL statement for database creation
    create_db_sql = f"""
    CREATE DATABASE {db_name} COLLATE Latin1_General_100_CI_AS_SC_UTF8;
    GO
    USE {db_name};
    """
    
    # Create SQL statement for table creation
    create_table_sql = f"""
    CREATE TABLE [{table_name}] (
{',\n'.join(columns_sql)}
    );
    """
    
    # Create SQL statements for data insertion
    insert_statements = []
    for _, row in df.iterrows():
        values = ', '.join([f"'{str(v).replace("'", "''")}'" if isinstance(v, str) else str(v) for v in row])
        insert_statements.append(f"INSERT INTO [{table_name}] VALUES ({values});")
    
    # Create the final SQL script
    sql_script = f"{create_db_sql}\n{create_table_sql}\n" + "\n".join(insert_statements)
    
    # Save the generated SQL script
    output_path = csv_path.replace(".csv", ".sql")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(sql_script)
    
    messagebox.showinfo("Success", f"SQL script generated: {output_path}")

# Function to select a CSV file
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        entry_file.delete(0, tk.END)
        entry_file.insert(0, file_path)

# Function to generate the SQL script
def generate_sql():
    csv_file = entry_file.get()
    database_name = entry_db.get()
    if not csv_file or not database_name:
        messagebox.showerror("Error", "Please select a CSV file and enter the database name.")
        return
    csv_to_sql(csv_file, database_name)
    
# ==================================
# GUI configuration
# ==================================
tk_root = ttk.Window(themename="journal")
tk_root.title("CSV to SQL Script")
tk_root.geometry("500x300")
tk_root.resizable(True, True)

# Field for CSV file selection
ttk.Label(tk_root, text="CSV File:").pack(pady=5)
frame_file = ttk.Frame(tk_root)
frame_file.pack(fill=tk.X, padx=10)
entry_file = ttk.Entry(frame_file)
entry_file.pack(side=tk.LEFT, fill=tk.X, expand=True)
ttk.Button(frame_file, text="Select", command=select_file).pack(side=tk.RIGHT, padx=5)

# Field for database name input
ttk.Label(tk_root, text="Database Name:").pack(pady=5)
entry_db = ttk.Entry(tk_root)
entry_db.pack(fill=tk.X, padx=10)

# Button to generate the SQL script
ttk.Button(tk_root, text="Generate SQL Script", command=generate_sql).pack(pady=20)

# Start the application
tk_root.mainloop()
