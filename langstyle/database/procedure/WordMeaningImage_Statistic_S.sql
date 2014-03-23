use langstyle;

drop procedure if exists WordMeaningImage_Statistic_S;

delimiter //;
create procedure WordMeaningImage_Statistic_S(in p_wordMeaningId int, in p_imageCount int)
begin
	select ImageId, count(*) as UserCount
	from WordMeaningImage
	where WordMeaningId = p_wordMeaningId
	group by ImageId
	order by UserCount
	limit p_imageCount;
end
