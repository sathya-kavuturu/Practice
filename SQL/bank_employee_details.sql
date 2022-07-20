CREATE TABLE bank_employee_details
(
Employee_No NUMBER(6) CONSTRAINT emp_no_pkey PRIMARY KEY,
First_Name VARCHAR2(20) NOT NULL,
Last_Name VARCHAR2(20) NOT NULL,
Email_Id VARCHAR2(30) CONSTRAINT email_uq UNIQUE,
Department_No NUMBER(2) DEFAULT 10,
Manager_Emp_No NUMBER(6) CONSTRAINT manager_fkey REFERENCES bank_employee_details(Employee_No)
);
