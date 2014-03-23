use langstyle;

create table WordLanguage(
	LanguageId int primary key auto_increment, 
	Name varchar(64)
);

insert into SchemaChange(ScriptName, MajorReleaseNumber, MinorReleaseNumber, BuildNumber, DateApplied)
values ('0.0.2-Language.sql', 0, 0, 2, now());
