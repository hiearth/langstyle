use Langstyle;

-- ScriptName, MajorReleaseNumber, MinorReleaseNumber, BuildNumber, DateApplied
create table SchemaChange(
	Id int primary key, 
	ScriptName varchar(128), 
	MajorReleaseNumber int, 
	MinorReleaseNumber int, 
	BuildNumber int, 
	DateApplied datetime
);