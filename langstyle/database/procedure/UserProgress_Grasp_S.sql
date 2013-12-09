use langstyle;

drop procedure if exists UserProgress_Grasp_S;

delimiter //
create procedure UserProgress_Grasp_S(in userId int)
begin
	select CharacterId, RepeatCount, LastLearningTime, GraspTime
	from UserProgress as u
	where u.UserId = userId and GraspTime is not null;
end //