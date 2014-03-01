use langstyle;

drop procedure if exists UserProgress_Count_U;

delimiter //;
create procedure UserProgress_Count_U(in p_userId int, in p_characterId int)
begin
	update UserProgress
	set RepeatCount = RepeatCount + 1
	where UserId = p_userId and CharacterId = p_characterId;
end //
delimiter ; //