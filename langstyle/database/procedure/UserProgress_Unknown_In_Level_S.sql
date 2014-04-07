
use langstyle;

drop procedure if exists UserProgress_Unknown_In_Level_S;

delimiter //;
create procedure UserProgress_Unknown_In_Level_S(in p_userId int, in p_level int)
begin
    declare v_languageMapId int;
    set v_languageMapId = (select LanguageMapId from User where UserId = p_userId);

    select WordMeaningId 
	from WordMeaning
	where LanguageMapId = v_languageMapId and Level = p_level
    and WordMeaningId not in (
		select WordMeaningId
		from UserProgress 
		where UserId = p_userId
	); 
end
