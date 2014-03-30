use langstyle;

create table UserProgressAudit(
	UserId int,
    WordMeaningId int,
    Result varchar(32),
	AuditTime datetime
);

insert into SchemaChange(ScriptName, MajorReleaseNumber, MinorReleaseNumber, BuildNumber, DateApplied)
values ('0.0.10-UserProgressAudit.sql', 0, 0, 10, now());
