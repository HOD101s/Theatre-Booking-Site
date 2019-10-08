getTimings = "SELECT `tstamp` FROM `show` WHERE `mid` = (SELECT `mid` from `movie` WHERE `Movie Name` = '{}');"
getShowData = "SELECT * FROM `show` WHERE `mid` = (SELECT `mid` from `movie` WHERE `Movie Name` = '{}') AND (`tstamp` = '{}');"
updateTickets = "UPDATE `show` SET `tickets`= concat(`tickets`,'{}') WHERE `mid` = (SELECT `mid` from `movie` WHERE `Movie Name` = '{}') AND (`tstamp` = '{}')";
check_login = "SELECT * FROM `client` WHERE (`uid` = '{}') AND (`password` = '{}');"
check_register = "SELECT * FROM `client` WHERE (`uid` = '{}');"
regUser = "INSERT INTO `client`(`uid`, `password`, `credential`) VALUES ('{}','{}',0);"
insertTicket = "INSERT INTO `tickets`(`tid`, `tstamp`, `seat_no`, `showid`, `uid`) VALUES ('{}','{}','{}','{}','{}');"

allShow = "SELECT * FROM `show`;";
allTicket = "SELECT * FROM `tickets`;";
allClient = "SELECT * FROM `client`;";
allMovie = "SELECT * FROM `movie`;";


'''
CREATE TABLE `Client` (
  `uid` VARCHAR(20)PRIMARY KEY,
  `password` VARCHAR(20),
  `credential` VARCHAR(20)
);

CREATE TABLE `Movie` (
  `mid` VARCHAR(5) PRIMARY KEY,
  `Movie Name` VARCHAR(20)
);

CREATE TABLE `Show` (
  `ShowID` VARCHAR(5) PRIMARY KEY,
  `Screen` VARCHAR(5),
  `tstamp` VARCHAR(5),
  `cost` int(3),
  `tickets` VARCHAR(1000),
  `mid` VARCHAR(5),
  FOREIGN KEY(`mid`) REFERENCES `Movie`(`mid`)
  
);

CREATE TABLE `Tickets` (
  `tid` VARCHAR(100) PRIMARY KEY,
  `tstamp` VARCHAR(100),
  `seat_no` VARCHAR(100),
  `showid` VARCHAR(100),
  `uid` VARCHAR(20),
  FOREIGN KEY(`ShowID`) REFERENCES `Show` (`ShowID`),
  FOREIGN KEY(`uid`) REFERENCES `Client` (`uid`)
);
'''


'''
Jeremy Queries:


Movie Queries
INSERT INTO `movie`(`mid`, `Movie Name`) VALUES (1,'Abominable')
INSERT INTO `movie`(`mid`, `Movie Name`) VALUES (2,'Spider Man')
INSERT INTO `movie`(`mid`, `Movie Name`) VALUES (3,'Deadpool')
INSERT INTO `movie`(`mid`, `Movie Name`) VALUES (4,'Ragnarok')
INSERT INTO `movie`(`mid`, `Movie Name`) VALUES (5,'Justice league')
INSERT INTO `movie`(`mid`, `Movie Name`) VALUES (6,'Star Wars')
INSERT INTO `movie`(`mid`, `Movie Name`) VALUES (7,'joker')
INSERT INTO `movie`(`mid`, `Movie Name`) VALUES (8,'panther')
INSERT INTO `movie`(`mid`, `Movie Name`) VALUES (9,'wall')



Show Queries
INSERT INTO `show`(`ShowID`, `Screen`, `tstamp`, `cost`, `mid`) VALUES (1, 1, '12:30', 100, 1)
INSERT INTO `show`(`ShowID`, `Screen`, `tstamp`, `cost`, `mid`) VALUES (2, 2, '13:00', 100, 1)
INSERT INTO `show`(`ShowID`, `Screen`, `tstamp`, `cost`, `mid`) VALUES (3, 1, '19:00', 120, 2 )
INSERT INTO `show`(`ShowID`, `Screen`, `tstamp`, `cost`, `mid`) VALUES (4, 2, '16:00', 120, 2 )
INSERT INTO `show`(`ShowID`, `Screen`, `tstamp`, `cost`, `mid`) VALUES (5, 1, '03:00', 90, 3 )
INSERT INTO `show`(`ShowID`, `Screen`, `tstamp`, `cost`, `mid`) VALUES (6, 2, '13:00', 80, 4 )
INSERT INTO `show`(`ShowID`, `Screen`, `tstamp`, `cost`, `mid`) VALUES (7, 1, '16:00', 80, 4 )
INSERT INTO `show`(`ShowID`, `Screen`, `tstamp`, `cost`, `mid`) VALUES (8, 3, '09:00', 150, 5 )
INSERT INTO `show`(`ShowID`, `Screen`, `tstamp`, `cost`, `mid`) VALUES (9, 1, '19:00', 150, 5 )
INSERT INTO `show`(`ShowID`, `Screen`, `tstamp`, `cost`, `mid`) VALUES (10, 2, '07:00', 150, 5 )
INSERT INTO `show`(`ShowID`, `Screen`, `tstamp`, `cost`, `mid`) VALUES (11, 1, '10:00', 150, 6 )
INSERT INTO `show`(`ShowID`, `Screen`, `tstamp`, `cost`, `mid`) VALUES (12, 2, '11:00', 60, 6 )
INSERT INTO `show`(`ShowID`, `Screen`, `tstamp`, `cost`, `mid`) VALUES (13, 2, '21:00', 160, 7 )
INSERT INTO `show`(`ShowID`, `Screen`, `tstamp`, `cost`, `mid`) VALUES (14, 1, '21:00', 160, 7 )
INSERT INTO `show`(`ShowID`, `Screen`, `tstamp`, `cost`, `mid`) VALUES (15, 1, '11:00', 160, 7 )
INSERT INTO `show`(`ShowID`, `Screen`, `tstamp`, `cost`, `mid`) VALUES (16, 1, '01:00', 110, 8 )
INSERT INTO `show`(`ShowID`, `Screen`, `tstamp`, `cost`, `mid`) VALUES (17, 2, '16:00', 110, 8 )
INSERT INTO `show`(`ShowID`, `Screen`, `tstamp`, `cost`, `mid`) VALUES (18, 1, '16:00', 100, 9 )
INSERT INTO `show`(`ShowID`, `Screen`, `tstamp`, `cost`, `mid`) VALUES (19, 2,'21:00', 100, 9 )







'''