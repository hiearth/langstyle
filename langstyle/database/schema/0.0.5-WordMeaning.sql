use langstyle;

create table WordMeaning(
    WordMeaningId int primary key auto_increment,
    CharacterId int,
    LanguageMapId int,
    Explaination varchar(1024),
    Level int
)
collate utf8_bin;

insert into SchemaChange(ScriptName, MajorReleaseNumber, MinorReleaseNumber, BuildNumber, DateApplied)
values ('0.0.5-WordMeaning.sql', 0, 0, 5, now());
