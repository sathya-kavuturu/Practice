-- Q. To retrieve all employess in the database
-- SELECT * FROm "employees";

-- Q. How many departments are there in the company?
-- SELECT count( * ) FROM "departments";

-- Q. HOw many time employee 10001 had a raise?
-- SELECT * FROM "salaries";

-- Q. What title does employee 10006 have?
-- select * FROM "titles";

-- Q. Renaming columns
-- SELECT emp_no AS "Employee No", birth_date AS "Birthday", first_name AS "First Name" FROM "employees";

-- Q. To concatenate and rename columns first name and last name from employees
-- SELECT concat( first_name, ' ', last_name ) AS "name" from "employees";

-- Q. To concatenate and rename columns emp_no and title from titles
-- SELECT concat( emp_no, ' is a ', title ) AS "Employee Title" from "titles";

-- AGGREGATE FUNCTIONS - AVG(), COUNT(), MAX(), MIN(),  SUM()
-- Q. Get the highest salary available
-- SELECT max(salary) FROM salaries;

--Q. Get the total amount of salaries paid
-- SELECT sum(salary) FROM "salaries";

-- Q. select the employee with the name "MAYUMI SCHUELLER"
--SELECT first_name, last_name FROM 
/* 
filter on first name and last name
focus the filtering on single person 
*/
--WHERE first_name='Mayumi' AND last_name='Schueller';

/*
COMMON SELECT MISTAKES
1. Mispelling
2. using ; instead of , or vice versa
3. using " instead of ' 
4.  invalid common name 
*/

-- Q. get a list of all emale employees
-- SELECT first_name FROM employees
-- WHERE gender = 'F';

--Q. How many female customers do we have from te state of oregan(OR) or new york(NY)
-- SELECT firstname, lastname, gender FROM customers
-- WHERE gender='F' AND (state='OR' OR state='NY');

-- Q. How many customers are not 55
-- SELECT count( age) FROM customers
-- WHERE NOT age=55;

-- syntax for not equal to:  != or <>

-- How many female customers do we have from the state of Oregon (OR)?
/*
* Write your query here
*/

-- Who over the age of 44 has an income of 100 000 or more? (excluding 44)
/*
* Write your query here
*/

-- Who between the ages of 30 and 50 has an income less than 50 000?
-- (include 30 and 50 in the results)

/*
* Write your query here
*/

-- What is the average income between the ages of 20 and 50? (Excluding 20 and 50)
/*
* Write your query here
*/















