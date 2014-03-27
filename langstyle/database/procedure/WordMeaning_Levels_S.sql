use langstyle;

drop procedure if exists WordMeaning_Levels_S;

delimiter //;
create procedure WordMeaning_Levels_S(in p_languageMapId int)
begin
	select distinct Level 
	from WordMeaning
	where LanguageMapId = p_languageMapId;
end