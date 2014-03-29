
use langstyle;

drop procedure if exists LanguageMap_Id_S;

delimiter //;
create procedure LanguageMap_Id_S(in p_fromId int, in p_targetId int)
begin
    select LanguageMapId from LanguageMap
    where FromLanguageId = p_fromId and TargetLanguageId = p_targetId;
end
