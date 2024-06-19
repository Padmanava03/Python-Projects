create database bank;
create table customer(
	CUS_id varchar(50) PRIMARY KEY,
  ACC_no varchar(50) UNIQUE,
	Name varchar(150),
	DOB varchar(10),
  Gender varchar(10),
	Status varchar(10),
	Nationality varchar(100),
	PAN varchar(50) UNIQUE,
  Father varchar(150),
	Address varchar(200),
	Landmark varchar(100),
	City varchar(100),
  pin_code varchar(50),
	res_type varchar(20),
  ph_no varchar(50),
	email varchar(200),
  occupation varchar(200),
	an_inc bigint
)ENGINE=INNODB;
Create table account(
  cus_id varchar(50) UNIQUE,
  acc_no varchar(50) UNIQUE,
  balance bigint,
  INDEX CUS(cus_id),
  FOREIGN KEY(cus_id)
  REFERENCES customer(CUS_id)
  ON DELETE CASCADE
)ENGINE=INNODB;
Create table transaction(
  cus_id varchar(50),
  acc_no varchar(50),
  amount bigint,
  t_method varchar(50),
  t_date varchar(20),
  t_time varchar(20),
  INDEX CUS(cus_id),
  FOREIGN KEY(cus_id)
  REFERENCES customer(CUS_id)
  ON DELETE CASCADE
)ENGINE=INNODB;
create table pass(
  pas varchar(20)
)ENGINE=INNODB;
INSERT INTO pass(pas) VALUES('0123456');
select * from customer;
Select * from account;
select * from transaction;
select * from pass;
