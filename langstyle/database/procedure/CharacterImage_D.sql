use langstyle;

drop procedure if exists CharacterImage_D;

delimiter //;
create procedure CharacterImage_D(in p_userId int, in p_characterId int, in p_imageId int)
begin
	delete from CharacterImage
	where UserId = p_userId and CharacterId = p_characterId and ImageId = p_imageId;
end
