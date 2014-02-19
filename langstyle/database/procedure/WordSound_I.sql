use langstyle;

drop procedure if exists WordSound_I;

delimiter //
create procedure WordSound_I(in p_soundMd5 varchar(32), in p_userProviderId int, out p_soundId int)
begin
	insert into WordSound(SoundMd5, UserProviderId)
	values (p_soundMd5, p_userProviderId);
	set p_soundId = last_insert_id();
end //