
use langstyle;

drop procedure if exists WordMeaning_S_By_Level;

delimiter //;
create procedure WordMeaning_S_By_Level(in p_languageMapId int, in p_level int)
begin
    select wm.WordMeaningId, wc.CharacterCode, wm.Explaination
    from WordMeaning as wm
    join WordCharacter as wc on wm.CharacterId = wc.CharacterId 
    where wm.LanguageMapId = p_languageMapId and wm.Level = p_level;
end
