use langstyle;

create table WordSound(
	SoundId int primary key auto_increment,
	SoundMd5 varchar(32),
	UserProviderId int
);

insert into SchemaChange(ScriptName, MajorReleaseNumber, MinorReleaseNumber, BuildNumber, DateApplied)
values ('0.0.7-WordSound.sql', 0, 0, 7, now());
