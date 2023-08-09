create database banco_Poo;
use banco_poo;

create table conta_corrente(
id int auto_increment not null,
titular int,
numero int,
agencia int,
saldo float,
primary key(id),
foreign key(titular) references clientes (id)
);

create table clientes(
id int auto_increment not null,
nome varchar (50),
cpf numeric,
primary key(id)
);


insert into clientes (nome, cpf) values('Eduardo',  '076375633');
insert into conta_corrente(titular, numero, agencia, saldo) values('1', '20725', '2412', '50.00');

select * from clientes;
select * from conta_corrente;
select nome, numero, agencia, saldo from conta_corrente join clientes on conta_corrente.titular = clientes.id;
select * from conta_corrente join clientes on conta_corrente.titular = clientes.id;
DELETE FROM conta_corrente WHERE id = '2';
delete from clientes where id = '1';