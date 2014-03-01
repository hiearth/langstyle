use langstyle;

drop procedure if exists CharacterImage_Images_S;

delimiter //;
create procedure CharacterImage_Images_S(in p_userId int, in p_characterId int)
begin
	select ImageId 
	from CharacterImage
	where UserId = p_userId and CharacterId = p_characterId;
end
