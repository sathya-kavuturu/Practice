CREATE TABLE fixed_deposit_account
(
FD_acc_no NUMBER(14) CONSTRAINT FD_pkey PRIMARY KEY,
Customer_Id NUMBER(8) CONSTRAINT cust_fkey REFERENCES savings_accoun(Customer_Id),
Fd_Amount NUMBER(20,2),
Interest_Rate NUMBER(5,2) int_rate_check CHECK(Interest_Rate>=2.5 AND Interest_Rate<=12.0)

);