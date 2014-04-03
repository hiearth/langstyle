
use langstyle;

drop procedure if exists UserProgress_S;

delimiter //;
create procedure UserProgress_S(in p_userId int, in p_wordMeaningId int)
begin
    select RepeatCount, IsCurrent, Status, LastLearningTime from UserProgress
    where UserId = p_userId and WordMeaningId = p_wordMeaningId;
end
