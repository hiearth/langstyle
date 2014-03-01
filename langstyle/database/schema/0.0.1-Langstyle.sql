
create database langstyle
	default character set utf8
	default collate utf8_general_ci;


use langstyle;
-- ScriptName, MajorReleaseNumber, MinorReleaseNumber, BuildNumber, DateApplied
create table SchemaChange(
        Id int primary key, 
        ScriptName varchar(128), 
        MajorReleaseNumber int, 
        MinorReleaseNumber int, 
        BuildNumber int, 
        DateApplied datetime
);