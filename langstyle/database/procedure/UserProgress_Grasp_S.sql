use langstyle;

drop procedure if exists UserProgress_Grasp_S;

delimiter //;
create procedure UserProgress_Grasp_S(in p_userId int)
begin
	select WordMeaningId, RepeatCount, LastLearningTime
	from UserProgress
	where UserId = p_userId and Status = 'Grasp';
end
