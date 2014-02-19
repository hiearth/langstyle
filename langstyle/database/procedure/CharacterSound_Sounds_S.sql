use langstyle;

drop procedure if exists CharacterSound_Sounds_S;

delimiter //
create procedure CharacterSound_Sounds_S(in p_userId int, in p_characterId int)
begin
	select SoundId
	from CharacterSound
	where UserId = p_userId and CharacterId = p_characterId;
end //