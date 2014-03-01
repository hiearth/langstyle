use langstyle;

drop procedure if exists WordCharacter_S_By_Id;

delimiter //;
create procedure WordCharacter_S_By_Id(in p_characterId int)
begin
	select CharacterCode from WordCharacter
	where CharacterId = p_characterId;
end //
delimiter ; //