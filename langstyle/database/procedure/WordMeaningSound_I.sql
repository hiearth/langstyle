use langstyle;

drop procedure if exists WordMeaningSound_I;

delimiter //;
create procedure WordMeaningSound_I(in p_userId int, in p_wordMeaningId int, in p_soundId int)
begin
	insert into WordMeaningSound(UserId, WordMeaningId, SoundId)
	values (p_userId, p_wordMeaningId, p_soundId);
end
