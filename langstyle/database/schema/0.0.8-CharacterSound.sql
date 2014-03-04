use langstyle;

create table CharacterSound(
    UserId int,
    CharacterId int,
    SoundId int
);

insert into SchemaChange(ScriptName, MajorReleaseNumber, MinorReleaseNumber, BuildNumber, DateApplied)
values ('0.0.8-CharacterSound.sql', 0, 0, 8, now());