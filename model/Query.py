getTimings = "SELECT `tstamp` FROM `show` WHERE `mid` = (SELECT `mid` from `movie` WHERE `Movie Name` = '{}');"
getShowData = "SELECT * FROM `show` WHERE `mid` = (SELECT `mid` from `movie` WHERE `Movie Name` = '{}') AND (`tstamp` = '{}');"
updateTickets = "UPDATE `show` SET `tickets`= concat(`tickets`,'{}') WHERE `mid` = (SELECT `mid` from `movie` WHERE `Movie Name` = '{}') AND (`tstamp` = '{}')";
check_login = "SELECT * FROM `client` WHERE (`uid` = '{}') AND (`password` = '{}')";
check_register = "SELECT * FROM `client` WHERE (`uid` = '{}')";
regUser = "INSERT INTO `client`(`uid`, `password`, `credential`) VALUES ('{}','{}',0)";

'''
Create Database `theatre`;

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
  `tid` VARCHAR(5) PRIMARY KEY,
  `tstamp` VARCHAR(5),
  `seat_no` VARCHAR(5),
  `showid` VARCHAR(5),
  `uid` VARCHAR(20),
  FOREIGN KEY(`ShowID`) REFERENCES `Show` (`ShowID`),
  FOREIGN KEY(`uid`) REFERENCES `Client` (`uid`)
);
'''