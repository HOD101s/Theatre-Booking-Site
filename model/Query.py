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





Show Queries
INSERT INTO `show`(`ShowID`, `Screen`, `tstamp`, `cost`, `mid`) VALUES (1, 1, '12:30', 100, 1)
INSERT INTO `show`(`ShowID`, `Screen`, `tstamp`, `cost`, `mid`) VALUES (2, 2, '3:00', 100, 1)
INSERT INTO `show`(`ShowID`, `Screen`, `tstamp`, `cost`, `mid`) VALUES (3, 1, '9:00', 120, 2 )
INSERT INTO `show`(`ShowID`, `Screen`, `tstamp`, `cost`, `mid`) VALUES (4, 2, '6:00', 120, 2 )
INSERT INTO `show`(`ShowID`, `Screen`, `tstamp`, `cost`, `mid`) VALUES (5, 1, '3:00', 90, 3 )
INSERT INTO `show`(`ShowID`, `Screen`, `tstamp`, `cost`, `mid`) VALUES (6, 2, '3:00', 80, 4 )
INSERT INTO `show`(`ShowID`, `Screen`, `tstamp`, `cost`, `mid`) VALUES (7, 1, '6:00', 80, 4 )
INSERT INTO `show`(`ShowID`, `Screen`, `tstamp`, `cost`, `mid`) VALUES (8, 3, '9:00', 150, 5 )
INSERT INTO `show`(`ShowID`, `Screen`, `tstamp`, `cost`, `mid`) VALUES (9, 1, '9:00', 150, 5 )
INSERT INTO `show`(`ShowID`, `Screen`, `tstamp`, `cost`, `mid`) VALUES (10, 2, '7:00', 150, 5 )
INSERT INTO `show`(`ShowID`, `Screen`, `tstamp`, `cost`, `mid`) VALUES (11, 1, '10:00', 150, 6 )
INSERT INTO `show`(`ShowID`, `Screen`, `tstamp`, `cost`, `mid`) VALUES (12, 2, '11:00', 60, 6 )







'''