use langstyle;

create table WordMeaningSound(
    UserId int,
    WordMeaningId int,
    SoundId int
);

insert into SchemaChange(ScriptName, MajorReleaseNumber, MinorReleaseNumber, BuildNumber, DateApplied)
values ('0.0.12-WordMeaningSound.sql', 0, 0, 12, now());
