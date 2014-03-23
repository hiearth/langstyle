use langstyle;

drop procedure if exists UserProgress_Grasp_U;

delimiter //;
create procedure UserProgress_Grasp_U(in p_userId int, in p_wordMeaningId int)
begin
	update UserProgress
	set GraspTime = now()
	where UserId = p_userId and WordMeaningId = p_wordMeaningId;
end
