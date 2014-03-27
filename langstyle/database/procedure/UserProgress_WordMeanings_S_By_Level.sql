use langstyle;

drop procedure if exists UserProgress_WordMeanings_S_By_Level;

delimiter //;
create procedure UserProgress_WordMeanings_S_By_Level(in p_userId int, in p_level int)
begin
	select WordMeaningId from UserProgress as up
	where UserId = p_userId 
	and p_level = (select Level from WordMeaning 
					where WordMeaningId = up.WordMeaningId);
end