use langstyle;

drop procedure if exists WordMeaningSound_D;

delimiter //;
create procedure WordMeaningSound_D(in p_userId int, in p_wordMeaningId int, in p_soundId int)
begin
	delete from WordMeaningSound
	where UserId = p_userId and WordMeaningId  = p_wordMeaningId and SoundId = p_soundId;
end
