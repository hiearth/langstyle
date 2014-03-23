
create database langstyle
	default character set utf8
	default collate utf8_bin;


use langstyle;
create table SchemaChange(
        Id int primary key auto_increment, 
        ScriptName varchar(128), 
        MajorReleaseNumber int, 
        MinorReleaseNumber int, 
        BuildNumber int, 
        DateApplied datetime
);

insert into SchemaChange(ScriptName, MajorReleaseNumber, MinorReleaseNumber, BuildNumber, DateApplied)
values ('0.0.1-Langstyle.sql', 0, 0, 1, now());
