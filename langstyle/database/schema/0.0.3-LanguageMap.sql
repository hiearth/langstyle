use langstyle;

create table LanguageMap(
    LanguageMapId int primary key auto_increment,
    FromLanguageId int,
    TargetLanguageId int
);

insert into SchemaChange(ScriptName, MajorReleaseNumber, MinorReleaseNumber, BuildNumber, DateApplied)
values ('0.0.3-LanguageMap.sql', 0, 0, 3, now());
