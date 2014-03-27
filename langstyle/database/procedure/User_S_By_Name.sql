use langstyle;

drop procedure if exists User_S_By_Name;

delimiter //;
create procedure User_S_By_Name(in p_userName varchar(64))
begin
	select UserId, Name, UserPassword, Email, LanguageMapId
	from User
	where Name = p_userName;
end
