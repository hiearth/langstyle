use langstyle;

drop procedure if exists UserProcess_Learning_S;

delimiter //
create procedure UserProcess_Learning_S(in userId int)
begin
	select Code as CharacterCode 
	from WordCharacter as c
	join UserProcess as u
	on c.CharacterId = u.CharacterId
	where u.UserId = userId;
end //