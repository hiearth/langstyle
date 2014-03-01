use langstyle;

drop procedure if exists WordImage_S_By_Id;

delimiter //;
create procedure WordImage_S_By_Id(in p_imageId int)
begin
	select ImageMd5, UserProviderId 
	from WordImage
	where ImageId = p_imageId;
end
