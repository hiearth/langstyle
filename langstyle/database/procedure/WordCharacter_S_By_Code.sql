use langstyle;

drop procedure if exists WordCharacter_S_By_Code;

delimiter //
create procedure WordCharacter_S_By_Code(in p_characterCode varchar(64))
begin
	select CharacterId from WordCharacter
	where CharacterCode = p_characterCode;
end //