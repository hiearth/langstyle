use langstyle;

create table UserCharacterAudit(
	UserId int,
    WordMeaningId int,
	AuditTime datetime
);

insert into SchemaChange(ScriptName, MajorReleaseNumber, MinorReleaseNumber, BuildNumber, DateApplied)
values ('0.0.10-User.sql', 0, 0, 10, now());
