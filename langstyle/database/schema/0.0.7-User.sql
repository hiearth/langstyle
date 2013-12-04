use Langstyle;

create table User(
	UserId int primary key,
	Name varchar(64),
	Email varchar(256),
	UserPassword varchar(256)
);

create table UserLearning(
	UserId int,
	CharacterId int,
	RepeatCount	int,
	IsCurrent bit(1),
	LastLearningTime datetime
);

create table UserGrasp(
	UserId int,
	CharacterId int,
	RepeatCount int,
	GraspTime datetime
);

create table UserCharacterAudit(
	UserId int,
	CharacterId int,
	AuditTime datetime
);