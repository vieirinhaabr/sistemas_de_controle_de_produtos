drop database if exists scp;

create database scp;
use scp;

create table PRODUCTS(ID INT NOT NULL auto_increment primary KEY,
						NAME varchar(50),
                        DESCRIPTION varchar(300),
                        PRICE float,
                        AMOUNT tinyint);
                        
select * from PRODUCTS;
