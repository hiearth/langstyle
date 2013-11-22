use langstyle;

drop procedure if exists UserProgress_Count_S;

delimiter //
create procedure UserProgress_Count_S(in userId int, in characterId int)
begin
	select RepeatCount from UserProgress
	where user_id = userId and character_id = characterId;
end //