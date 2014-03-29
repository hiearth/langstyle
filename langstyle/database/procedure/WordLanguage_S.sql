
use langstyle;

drop procedure if exists WordLanguage_S;

delimiter //;
create procedure WordLanguage_S(in p_languageId int)
begin
    select Name from WordLanguage
    where LanguageId = p_languageId;
end
