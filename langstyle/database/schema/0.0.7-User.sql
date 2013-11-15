use Langstyle;

create table User(
	UserId int primary key,
	Name varchar(64),
	Email varchar(256),
	UserPassword varchar(256)
)

-- create table UserProgress