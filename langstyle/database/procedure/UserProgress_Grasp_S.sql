use langstyle;

drop procedure if exists UserProgress_Grasp_S;

delimiter //
create procedure UserProgress_Grasp_S(in userId int)
begin
	select CharacterCode 
	from WordCharacter as c
	join UserProgress as u
	on c.CharacterId = u.CharacterId
	where u.UserId = userId and Grasp > 0;
end //