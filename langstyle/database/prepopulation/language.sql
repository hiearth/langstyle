use langstyle;

insert into wordlanguage (Name) values ('Chinese');
insert into wordlanguage (Name) values ('English');

insert into languagemap (FromLanguageId, TargetLanguageId) 
values 
((select LanguageId from wordlanguage where Name = 'Chinese'), 
(select LanguageId from wordlanguage where Name = 'English'));
