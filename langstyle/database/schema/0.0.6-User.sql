use langstyle;

create table User(
	UserId int primary key auto_increment,
	Name varchar(64) not null,
	UserPassword varchar(64) not null,
	Email varchar(256)
);

create table UserProgress(
	UserId int,
	CharacterId int,
	RepeatCount int,
	IsCurrent bit(1),
	LastLearningTime datetime,
	GraspTime datetime
);

create table UserCharacterAudit(
	UserId int,
	CharacterId int,
	AuditTime datetime
);

insert into SchemaChange(ScriptName, MajorReleaseNumber, MinorReleaseNumber, BuildNumber, DateApplied)
values ('0.0.6-User.sql', 0, 0, 6, now());