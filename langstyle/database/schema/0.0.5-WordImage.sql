use Langstyle;

create table WordImage(
	ImageId int primary key auto_increment,
	ImagePath varchar(1024),
	UserProviderId int
);