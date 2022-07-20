CREATE TABLE savings_account
(
Customer_Id NUMBER(8) CONSTRAINT cust_pkey PRIMARY KEY,
First_Name VARCHAR2(20) NOT NULL,
Last_Name VARCHAR2(20),
Account_No NUMBER(18) NOT NULL CONSTRAINT acc_no_unq UNIQUE,
Branch_Code VARCHAR2(10) NOT NULL,
Email_Id VARCHAR2(30) CONSTRAINT email_uq UNIQUE,
Phone_no VARCHAR2(20),
Current_Balance NUMBER(20,2) NOT NULL
);

DESC savings_account

