use langstyle;

drop procedure if exists UserCurrentCharacter_S;

delimiter //
create procedure UserCurrentCharacter_S(in userId int)
begin
	select c.CharacterCode 
	from WordCharacter as c
	join UserCurrentCharacter as uc
	on c.CharacterId = uc.CharacterId
	where uc.UserId = userId;
end //