create database VRP;
use VRP;

create table users(
	id int primary key,
    name varchar(255) not null, 
    email varchar(255) not null,
    password varchar(255) not null,
    constraint uk1
    unique(name,email)
);

create table citizen(
	citizen_id int primary key,
	name varchar(255) not null,
    email varchar(255) not null,
    age int not null,
    vaccine varchar(255) not null,
    dose_no int not null,
    nid_type varchar(255) not null,
    nid_num varchar(255) not null,
    constraint c1
    foreign key(name,email)
    references users(name,email),
    constraint cu1
    unique(name,email)
);

create table slot_booking(
	id int primary key,
    state varchar(255) not null,
    district varchar(255) not null,
    centre  varchar(255) not null,
    slot_date date not null,
    beneficiary_id varchar(16), 
    /*
    It can be null since beneficiary_id is 
    generated after slot booking is successful.
    */
    foreign key(id) references citizen(citizen_id)
);

describe users;
describe citizens;
describe slot_booking;

alter table citizen rename citizens;
drop database vrp;

insert into users values(1,"gaurav","abc@xyz.com","12345678");
insert into users values(1,"gaurav","abc@xyz.com","12345678");
insert into users values(2,"gaurav","abc1@xyz.com","12345678");

insert into citizens values(1,"gaurav","abc@xyz.com",23,"abc",1,"aadhar","abc123");
insert into citizens values(2,"gaurav2","abc@xyz.com",23,"abc",1,"aadhar","abc123");

insert into users values(3,"sathwik","sat@xyz.com","34567812"),
	(4,"bhawna","bwn@xyz.com","45678912"),
    (5,"abhilash","abhi@xyz.com","56789123");
    
select * from users;

insert into citizens values(2,"sathwik","sat@xyz.com",22,"covaxin",2,"passport","xyz123456"),
	(4,"bhawna","bwn@xyz.com",22,"sputnik",1,"aadhar","12345689021"),
    (5,"abhilash","abhi@xyz.com",23,"covishield",2,"voter id","ba511c12d");
    
select * from citizens; 

update citizens set vaccine="covishield" where email="abc@xyz.com";

select * from citizens;