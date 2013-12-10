use langstyle;

drop procedure if exists UserProgress_Grasp_S;

delimiter //
create procedure UserProgress_Grasp_S(in p_userId int)
begin
	select CharacterId, RepeatCount, LastLearningTime, GraspTime
	from UserProgress
	where UserId = p_userId and GraspTime is not null;
end //