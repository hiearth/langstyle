use langstyle;

drop procedure if exists UserProgress_Learning_S;

delimiter //;
create procedure UserProgress_Learning_S(in p_userId int)
begin
	select WordMeaningId, RepeatCount, IsCurrent, Status, LastLearningTime
	from UserProgress
	where UserId = p_userId and Status = 'Learning';
end
