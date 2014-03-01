use langstyle;

drop procedure if exists CharacterImage_I;

delimiter //;
create procedure CharacterImage_I(in p_userId int, in p_characterId int, in p_imageId int)
begin
	insert into CharacterImage(UserId, CharacterId, ImageId)
	values (p_userId, p_characterId, p_imageId);
end //
delimiter ; //