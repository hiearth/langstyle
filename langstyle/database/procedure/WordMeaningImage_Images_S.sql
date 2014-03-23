use langstyle;

drop procedure if exists WordMeaningImage_Images_S;

delimiter //;
create procedure WordMeaningImage_Images_S(in p_userId int, in p_wordMeaningId int)
begin
	select ImageId 
	from WordMeaningImage
	where UserId = p_userId and WordMeaningId = p_wordMeaningId;
end
