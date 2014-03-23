use langstyle;

drop procedure if exists UserProgress_Count_S;

delimiter //;
create procedure UserProgress_Count_S(in p_userId int, in p_wordMeaningId int)
begin
	select RepeatCount from UserProgress
	where UserId = p_userId and WordMeaningId = p_wordMeaningId;
end
