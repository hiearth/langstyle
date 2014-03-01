use langstyle;

drop procedure if exists CharacterSound_D;

delimiter //;
create procedure CharacterSound_D(in p_userId int, in p_characterId int, in p_soundId int)
begin
	delete from CharacterSound
	where UserId = p_userId and CharacterId = p_characterId and SoundId = p_soundId;
end //
delimiter ; //