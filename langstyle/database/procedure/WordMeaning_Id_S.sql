
use langstyle;

drop procedure if exists WordMeaning_Id_S;

delimiter //;
create procedure WordMeaning_Id_S(in p_characterId int, in p_languageMapId int, in p_explaination varchar(1024))
begin
    select WordMeaningId from WordMeaning
    where CharacterId = p_characterId and LanguageMapId = p_languageMapId and Explaination = p_explaination;
end
