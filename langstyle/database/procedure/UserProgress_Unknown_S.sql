use langstyle;

drop procedure if exists UserProgress_Unknown_S;

delimiter //;
create procedure UserProgress_Unknown_S(in p_userId int)
begin
    declare v_languageMapId int;
    set v_languageMapId = (select LanguageMapId from User where UserId = p_userId);
	select WordMeaningId 
	from WordMeaning
	where LanguageMapId = v_languageMapId 
    and WordMeaningId not in (
		select WordMeaningId
		from UserProgress 
		where UserId = p_userId
	);
end
