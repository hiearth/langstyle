use langstyle;

create table WordMeaningImage(
    UserId int,
    WordMeaningId int,
    ImageId int
);

-- aggregate algrithom: 
-- compute the top most 3(for example) images used by all users for one
-- character.
-- The top count should be configured in config file

-- When some user does not have custom image of some character
-- use the aggregate algrithom.

-- if some user does not have enough images for one character, 
-- first get custom images for this character of this user,
-- then use the aggregate algrithom to get the additional images.


insert into SchemaChange(ScriptName, MajorReleaseNumber, MinorReleaseNumber, BuildNumber, DateApplied)
values ('0.0.11-WordMeaningImage.sql', 0, 0, 11, now());
