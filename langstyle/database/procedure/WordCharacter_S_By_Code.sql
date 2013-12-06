use langstyle;

drop procedure if exists WordCharacter_S_By_Code;

delimiter //
create procedure WordCharacter_S_By_Code(in characterCode varchar(64))
begin
	select c.CharacterId from WordCharacter as c 
	where c.CharacterCode = characterCode;
end //