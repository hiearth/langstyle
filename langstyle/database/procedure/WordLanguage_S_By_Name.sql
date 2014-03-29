
use langstyle;

drop procedure if exists WordLanguage_S_By_Name;

delimiter //;
create procedure WordLanguage_S_By_Name(in p_name varchar(64))
begin
    select LanguageId from WordLanguage
    where Name = p_name;
end
