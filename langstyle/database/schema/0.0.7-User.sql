use Langstyle;

create table User(
	UserId int primary key,
	Name varchar(64),
	Email varchar(256),
	UserPassword varchar(256)
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