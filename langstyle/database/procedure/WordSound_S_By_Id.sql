use langstyle;

drop procedure if exists WordSound_S_By_Id;

delimiter //;
create procedure WordSound_S_By_Id(in p_soundId int)
begin
	select SoundMd5, UserProviderId
	from WordSound
	where SoundId = p_soundId;
end
