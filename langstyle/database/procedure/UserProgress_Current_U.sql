use langstyle;

drop procedure if exists UserProgress_Current_U;

delimiter //
create procedure UserProgress_Current_U(in p_userId int, in p_characterId int)
begin
	update UserProgress
	set IsCurrent = true
	where UserId = p_userId and CharacterId = p_characterId;
end //