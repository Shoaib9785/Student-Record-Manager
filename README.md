# Student Record Manager

A web app to manage student records, built with **Python, Streamlit and MySQL**.
It supports all four CRUD operations (add, view, update, remove) with input
validation and a custom dark-blue theme.

## Features

- **Add student** - name, ID, grade and CGPA, with duplicate-ID and empty-name checks
- **View students** - all records in a clean table
- **Update student** - change the name, grade or CGPA of an existing record
- **Remove student** - shows the record and asks for confirmation before deleting
- Parameterized SQL queries to prevent SQL injection
- Custom CSS styling using Streamlit's `data-testid` selectors

## Tech Stack

| Tool | Use |
|---|---|
| Python | Main language |
| Streamlit | Web interface |
| MySQL | Database |
| PyMySQL | Python-MySQL connection |
| Pandas | Displaying records as a table |

## Project Structure

```
Student-Record-Manager/
|-- app.py                          # main application
|-- schema.sql                      # database and table setup
|-- requirements.txt                # Python dependencies
|-- static/
|   `-- image.png                   # page icon
|-- .streamlit/
|   `-- secrets.toml.example        # template for DB credentials
|-- .gitignore
|-- LICENSE
`-- README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Shoaib9785/Student-Record-Manager.git
cd Student-Record-Manager
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up the database

Make sure MySQL is running, then run:

```bash
mysql -u root -p < schema.sql
```

This creates the database `w` and the table `student_managers`.

### 4. Add your credentials

Copy `.streamlit/secrets.toml.example` to `.streamlit/secrets.toml` and put in
your own MySQL details. This file is ignored by Git.

### 5. Run the app

```bash
streamlit run app.py
```

The app opens at `http://localhost:8501`.

## Database Schema

| Column | Type | Description |
|---|---|---|
| name | VARCHAR(100) | Student name |
| students_id | INT (primary key) | Unique student ID |
| grade | VARCHAR(2) | Letter grade (A+ to F) |
| cgpa | DECIMAL(3,1) | CGPA from 0 to 10 |

## Future Improvements

- Login system with admin roles
- Search and filter by name, ID or grade
- Export records to CSV or PDF
- Charts for CGPA and grade distribution
- Deploy online with a cloud database

## Author

**Mohammad Shoaib Khan** - B.Tech AI, MITS-DU, Gwalior
GitHub: [Shoaib9785](https://github.com/Shoaib9785)

## License

Released under the [MIT License](LICENSE).
