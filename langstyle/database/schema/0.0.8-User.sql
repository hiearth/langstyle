use langstyle;

create table User(
	UserId int primary key auto_increment,
    LanguageMapId int,
	Name varchar(64) not null,
	UserPassword varchar(64) not null,
	Email varchar(256)
);

insert into SchemaChange(ScriptName, MajorReleaseNumber, MinorReleaseNumber, BuildNumber, DateApplied)
values ('0.0.8-User.sql', 0, 0, 8, now());
