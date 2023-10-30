-- CREATE TABLE students (

-- 	first_name TEXT,
-- 	last_name TEXT,
-- 	age INTEGER
-- );

-- CREATE TABLE employees (

-- 	first_name TEXT,
-- 	last_name TEXT,
-- 	age INTEGER
-- );

-- SELECT * FROM students;

INSERT INTO employees (first_name, last_name, age)
VALUES ('John', 'Bonjovi', 42);

INSERT INTO employees (first_name, last_name, age)
VALUES ('Jane', 'Air', 29);

INSERT INTO employees (first_name, last_name, age)
VALUES ('John', 'Legend', 38);

INSERT INTO employees (first_name, last_name, age)
VALUES ('Paul', 'Mccartney', 54);

INSERT INTO employees (first_name, last_name, age)
VALUES ('John', 'Lenon', 36);

INSERT INTO employees (first_name, last_name, age)
VALUES ('Richard', 'Starkey', 40);

INSERT INTO employees (first_name, last_name, age)
VALUES ('John', 'Bonjovi', 42);

INSERT INTO employees (first_name, last_name, age)
VALUES ('Jane', 'Air', 29);

INSERT INTO employees (first_name, last_name, age)
VALUES ('John', 'Legend', 38);

INSERT INTO employees (first_name, last_name, age)
VALUES ('Paul', 'Mccartney', 54);

INSERT INTO employees (first_name, last_name, age)
VALUES ('John', 'Lenon', 36);

INSERT INTO employees (first_name, last_name, age)
VALUES ('Richard', 'Starkey', 40);

SELECT * FROM employees WHERE first_name IS 'John';

ALTER TABLE employees
ADD COLUMN CostumerID INTEGER;