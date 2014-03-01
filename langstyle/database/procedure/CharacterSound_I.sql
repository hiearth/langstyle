use langstyle;

drop procedure if exists CharacterSound_I;

delimiter //;
create procedure CharacterSound_I(in p_userId int, in p_characterId int, in p_soundId int)
begin
	insert into CharacterSound(UserId, CharacterId, SoundId)
	values (p_userId, p_characterId, p_soundId);
end //
delimiter ; //