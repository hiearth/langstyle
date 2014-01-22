use langstyle;

drop procedure if exists UserProgress_Unknown_S;

delimiter //
create procedure UserProgress_Unknown_S(in p_userId int)
begin
	select CharacterId 
	from WordCharacter
	where CharacterId not in (
		select CharacterId 
		from UserProgress 
		where UserId = p_userId
	);
end //