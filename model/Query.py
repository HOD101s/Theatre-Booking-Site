getTimings = "SELECT `tstamp` FROM `show` WHERE `mid` = (SELECT `mid` from `movie` WHERE `Movie Name` = '{}');"
getShowData = "SELECT * FROM `show` WHERE `mid` = (SELECT `mid` from `movie` WHERE `Movie Name` = '{}') AND (`tstamp` = '{}');"
updateTickets = "UPDATE `show` SET `tickets`= concat(`tickets`,'{}') WHERE `mid` = (SELECT `mid` from `movie` WHERE `Movie Name` = '{}') AND (`tstamp` = '{}')";