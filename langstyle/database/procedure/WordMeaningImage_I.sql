use langstyle;

drop procedure if exists WordMeaningImage_I;

delimiter //;
create procedure WordMeaningImage_I(in p_userId int, in p_wordMeaningId int, in p_imageId int)
begin
	insert into WordMeaningImage(UserId, WordMeaningId, ImageId)
	values (p_userId, p_wordMeaningId, p_imageId);
end
