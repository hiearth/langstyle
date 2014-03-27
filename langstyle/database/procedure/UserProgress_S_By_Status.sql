use langstyle;

drop procedure if exists UserProgress_S_By_Status;

delimiter //;
create procedure UserProgress_S_By_Status(in p_userId int, in p_status varchar(32))
begin
	select WordMeaningId, RepeatCount, IsCurrent, Status, LastLearningTime
	from UserProgress
	where UserId = p_userId and Status = p_status;
end
