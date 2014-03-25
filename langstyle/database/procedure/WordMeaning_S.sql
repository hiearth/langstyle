use langstyle;

drop procedure if exists WordMeaning_S;

delimiter //;
create procedure WordMeaning_S(in p_wordMeaningId int)
begin
    select WordMeaningId, wc.CharacterId, wc.CharacterCode, LanguageMapId, Explaination, Level
    from WordMeaning as wm join WordCharacter as wc
    on wm.CharacterId = wc.CharacterId
    where WordMeaningId = p_wordMeaningId;
end
