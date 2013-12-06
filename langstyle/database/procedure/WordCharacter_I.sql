use langstyle;

drop procedure if exists WordCharacter_I;

delimiter //
create procedure WordCharacter_I(in characterCode varchar(64), out characterId int)
begin
	insert into WordCharacter (CharacterId,CharacterCode) values (0, characterCode);
	set characterId = last_insert_id();
end //