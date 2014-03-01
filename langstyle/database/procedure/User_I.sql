use langstyle;

drop procedure if exists User_I;

delimiter //;
create procedure User_I(in p_name varchar(64), in p_password varchar(64), in p_email varchar(256), out p_userId int)
begin
	insert into User(Name, UserPassword, Email)
	values (p_name, p_password, p_email);

	set p_userId = last_insert_id();
end
