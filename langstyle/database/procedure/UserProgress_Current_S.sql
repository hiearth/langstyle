use langstyle;

drop procedure if exists UserProgress_Current_S;

delimiter //;
create procedure UserProgress_Current_S(in p_userId int)
begin
	select WordMeaningId, RepeatCount, LastLearningTime
	from UserProgress
	where UserId = p_userId and IsCurrent is true;
end
