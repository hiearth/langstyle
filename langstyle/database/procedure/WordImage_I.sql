use langstyle;

drop procedure if exists WordImage_I;

delimiter //;
create procedure WordImage_I(in p_imageMd5 varchar(32), in p_userProviderId int, out p_imageId int)
begin
	insert into WordImage (ImageMd5, UserProviderId)
	values (p_imageMd5, p_userProviderId);
	set p_imageId = last_insert_id();
end //
delimiter ; //