create table authors (
	id serial primary key,
	first_name varchar(50),
	last_name varchar(50)
	);


create table books (
	id serial primary key,
	title varchar(200),
	author_id int references authors(id),
	publication_year int
	);


create table sales (
	id serial primary key,
	quantity int,
	book_id int references books(id)
	);


insert into authors (first_name, last_name)
values
	('Лев', 'Толстой'),
	('Александр', 'Пушкин'),
	('Янка', 'Купала'),
	('Якуб', 'Колос'),
	('Максим', 'Богданович'),
	('Владимир', 'Короткевич');


insert into books (title, author_id, publication_year)
values
	('Новая земля', 4, 2011),
	('Курган', 3, 2007),
	('Евгений Онегин', 2, 2022),
	('Анна Каренина', 1, 2009),
	('Вишнёвый сад', null, 2026),
	('Герой нашего времени', null, 2016);


insert into sales (quantity, book_id)
values
	(58, 1),
	(71, 2),
	(67, 3),
	(54, 4),
	(24, 5),
	(33, 6);


select b.title as book_title,
	a.first_name as author_first_name,
	a.last_name as author_last_name
from books b
inner join authors a on b.author_id = a.id;


select a.first_name as author_first_name,
	a.last_name as author_last_name,
	b.title as book_title
from authors a
left join books b on a.id = b.author_id;


select a.first_name as author_first_name,
	a.last_name as author_last_name,
	b.title as book_title
from authors a
right join books b on a.id = b.author_id;


select a.first_name as author_first_name,
	a.last_name as author_last_name,
	b.title as book_title,
	s.quantity as quantity_of_sales
from authors a
join books b on a.id = b.author_id
join sales s on b.id = s.book_id;


select a.first_name as author_first_name,
	a.last_name as author_last_name,
	b.title as book_title,
	s.quantity as quantity_of_sales
from authors a
left join books b on a.id = b.author_id
left join sales s on b.id = s.book_id;
