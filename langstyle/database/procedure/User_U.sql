
use langstyle;

drop procedure if exists User_U;

delimiter //;
create procedure User_U(in p_userId int, in p_email varchar(256), in p_lanuageMapId int)
begin
    update User set Email = p_email, LanguageMapId = p_lanuageMapId
    where UserId = p_userId;
end
