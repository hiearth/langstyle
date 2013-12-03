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
	RepeatCount	int,
	Grasp bit(1)
);

create table UserGrasp(
	UserId int,
	CharacterId int,
	RepeatCount int
);

create table UserCharacterAudit(
	UserId int,
	CharacterId int,
	AuditTime datetime
);