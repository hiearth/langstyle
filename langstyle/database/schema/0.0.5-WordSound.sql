use langstyle;

create table WordSound(
	SoundId int primary key auto_increment,
	SoundMd5 varchar(32),
	UserProviderId int
);
