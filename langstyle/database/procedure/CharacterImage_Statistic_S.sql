use langstyle;

drop procedure if exists CharacterImage_Statistic_S;

delimiter //;
create procedure CharacterImage_Statistic_S(in p_characterId int, in p_imageCount int)
begin
	select ImageId, count(*) as UserCount
	from CharacterImage
	where CharacterId = p_characterId
	group by ImageId
	order by UserCount
	limit p_imageCount;
end //
delimiter ; //