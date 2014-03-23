use langstyle;

drop procedure if exists WordMeaningSound_Sounds_S;

delimiter //;
create procedure WordMeaningSound_Sounds_S(in p_userId int, in p_wordMeaningId int)
begin
	select SoundId
	from WordMeaningSound
	where UserId = p_userId and WordMeaningId = p_wordMeaningId;
end
