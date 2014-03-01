use langstyle;

create table WordImage(
	ImageId int primary key auto_increment,
	ImageMd5 varchar(32),
	UserProviderId int
);
