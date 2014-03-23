use langstyle;

drop procedure if exists WordMeaningImage_D;

delimiter //;
create procedure WordMeaningImage_D(in p_userId int, in p_wordMeaningId int, in p_imageId int)
begin
	delete from WordMeaningImage
	where UserId = p_userId 
    and WordMeaningId = p_wordMeaningId and ImageId = p_imageId;
end
