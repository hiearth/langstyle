use langstyle;

create table UserProgress(
	UserId int,
    WordMeaningId int,
	RepeatCount int,
	IsCurrent bit(1),
    Status varchar(32),
	LastLearningTime datetime
);

insert into SchemaChange(ScriptName, MajorReleaseNumber, MinorReleaseNumber, BuildNumber, DateApplied)
values ('0.0.9-UserProgress.sql', 0, 0, 9, now());
