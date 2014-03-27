use langstyle;

drop procedure if exists User_S;

delimiter //;
create procedure User_S(in p_userId int)
begin
	select UserId, Name, UserPassword, Email, LanguageMapId 
	from User
	where UserId = p_userId;
end