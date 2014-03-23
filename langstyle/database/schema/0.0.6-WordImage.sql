use langstyle;

create table WordImage(
	ImageId int primary key auto_increment,
	ImageMd5 varchar(32),
	UserProviderId int
);

insert into SchemaChange(ScriptName, MajorReleaseNumber, MinorReleaseNumber, BuildNumber, DateApplied)
values ('0.0.6-WordImage.sql', 0, 0, 6, now());
