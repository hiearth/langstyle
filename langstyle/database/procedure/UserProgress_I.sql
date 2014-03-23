use langstyle;

drop procedure if exists UserProgress_I;

delimiter //;
create procedure UserProgress_I(in p_userId int, in p_wordMeaningId int)
begin
	insert into UserProgress
	(UserId, WordMeaningId, RepeatCount, IsCurrent, LastLearningTime, GraspTime)	
	values
	(p_userId, p_wordMeaningId, 0, 0, null, null);
end
