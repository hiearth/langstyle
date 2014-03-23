use langstyle;

create table WordCharacter(
	CharacterId int primary key auto_increment, 
	CharacterCode varchar(64)
);


insert into SchemaChange(ScriptName, MajorReleaseNumber, MinorReleaseNumber, BuildNumber, DateApplied)
values ('0.0.4-Character.sql', 0, 0, 4, now());
