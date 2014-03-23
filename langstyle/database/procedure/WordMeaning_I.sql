use langstyle;

drop procedure if exists WordMeaning_I;

delimiter //;
create procedure WordMeaning_I(in p_characterId int, in p_languageMapId int, 
    in p_explaination varchar(1024), in p_level int, out p_wordMeaningId int)
begin
    insert into WordMeaning(CharacterId, LanguageMapId, Explaination, Level)
    values
    (p_characterId, p_languageMapId, p_explaination, p_level);

    set p_wordMeaningId = last_insert_id();
end
