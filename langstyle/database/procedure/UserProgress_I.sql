use langstyle;

drop procedure if exists UserProgress_I;

delimiter //
create procedure UserProgress_I(in userId int, in characterId int)
begin
	insert into UserProgress
	(UserId, CharacterId, RepeatCount, IsCurrent, LastLearningTime, GraspTime)	
	values
	(userId, characterId, 0, 0, null, null);
end //