use langstyle;

drop procedure if exists WordCharacter_S_By_Id;

delimiter //
create procedure WordCharacter_S_By_Id(in characterId int)
begin
	select c.CharacterCode from WordCharacter as c 
	where c.CharacterId = characterId;
end //