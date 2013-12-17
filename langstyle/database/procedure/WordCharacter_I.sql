use langstyle;

drop procedure if exists WordCharacter_I;

delimiter //
create procedure WordCharacter_I(in p_characterCode varchar(64), out p_characterId int)
begin
	insert into WordCharacter (CharacterId,CharacterCode) 
	values (0, p_characterCode);
	set p_characterId = last_insert_id();
end //