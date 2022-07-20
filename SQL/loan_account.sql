CREATE TABLE loan_account
(
Loan_acc_no NUMBER(18) CONSTRAINT acc_no_pkey PRIMARY KEY,
Customer_Id NUMBER(18) CONSTRAINT cust_fkey REFERENCES savings_accoun(Customer_Id),
Loan_Amount NUMBER(20,2),
Loan_Term NUMBER(2),
Loan_Interest_Type CHAR(1) CONSTRAINT interest_type CHECK(Loan_Interest_Type = 'F' OR Loan_Interest_Type= 'V')

);

DESC loan_account