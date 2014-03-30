
use langstyle;

drop procedure if exists UserProgressAudit_I;

delimiter //;
create procedure UserProgressAudit_I(in p_userId int, in p_wordMeaningId int, in p_result varchar(32))
begin
    insert into UserProgressAudit (UserId, WordMeaningId, Result, AuditTime)
    values (p_userId, p_wordMeaningId, p_result, now());
end
