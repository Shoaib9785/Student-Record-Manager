CREATE DATABASE IF NOT EXISTS w;
USE w;

CREATE TABLE IF NOT EXISTS student_managers (
    name        VARCHAR(100)  NOT NULL,
    students_id INT           PRIMARY KEY,
    grade       VARCHAR(2)    NOT NULL,
    cgpa        DECIMAL(3,1)  NOT NULL
);

-- optional sample data
INSERT INTO student_managers (name, students_id, grade, cgpa) VALUES
('Aarav Sharma', 101, 'A',  8.7),
('Priya Verma',  102, 'B+', 7.9),
('Rohan Singh',  103, 'A+', 9.4);
