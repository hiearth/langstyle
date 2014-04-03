
use langstyle;

drop procedure if exists UserProgress_U;

delimiter //;
create procedure UserProgress_U(in p_userId int, in p_wordMeaningId int, in p_status varchar(32))
begin
    update UserProgress set Status = p_status, LastLearningTime = now()
    where UserId = p_userId and WordMeaningId = p_wordMeaningId;
end
