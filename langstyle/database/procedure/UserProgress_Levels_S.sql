use langstyle;

drop procedure if exists UserProgress_Levels_S;

delimiter //;
create procedure UserProgress_Levels_S(in p_userId int)
begin
	select distinct wm.Level 
	from UserProgress as up 
	join WordMeaning as wm 
	on up.WordMeaningId = wm.WordMeaningId 
	where up.UserId = p_userId;
end