SELECT sqlite_version();
CREATE TABLE students (
    id   INTEGER PRIMARY KEY,
    name TEXT,
    age  INTEGER
);
INSERT INTO students (name, age) VALUES ('Ali', 18);
INSERT INTO students (name, age) VALUES ('Fatima', 20);
INSERT INTO students (name, age) VALUES ('Sara', 16);
SELECT * FROM students;
PRAGMA table_info(students);