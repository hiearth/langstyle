use langstyle;

drop procedure if exists UserProgress_Grasp_U;

delimiter //
create procedure UserProgress_Grasp_U(in userId int, in characterId int)
begin
	update UserProgress as u
	set u.GraspTime = now()
	where u.UserId = userId and u.CharacterId = characterId;
end //