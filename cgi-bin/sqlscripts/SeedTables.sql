--insert some developers
INSERT INTO Developers(name) VALUES ('John')
/
INSERT INTO Developers(name) VALUES ('Sal')
/
INSERT INTO Developers(name) VALUES ('Fredrick')
/
INSERT INTO Developers(name) VALUES ('Jiminy')
/

--insert some games
INSERT INTO games(asin,title,price,developers) values ('1234567890','title1',1.00,dev_table(dev_id(1),dev_id(2)))
/
INSERT INTO games(asin,title,price,developers) values ('0987654321','title2',2.97,dev_table(dev_id(1),dev_id(3)))
/


--insert some customers
INSERT INTO Customers(name,account) VALUES ('Jemma',purchased_game_table(purchased_game_t('0987654321',2,5.94),purchased_game_t('1234567890',1,1.00)))
/
INSERT INTO Customers(name,account) VALUES ('Fitz',purchased_game_table(purchased_game_t('1234567890',7,7.00)))
/

commit
/
commit
/
