use langstyle;

drop procedure if exists UserProgress_Level_Complete;

delimiter //;
create procedure UserProgress_Level_Complete(in p_userId int, in p_level int)
begin
	if exists(select WordMeaningId from WordMeaning 
			  where Level = p_level 
			  and WordMeaningId not in (select WordMeaningId 
										from UserProgress 
										where UserId = p_userId)) then
		select 0;
	else
		select 1;
	end if;
end
