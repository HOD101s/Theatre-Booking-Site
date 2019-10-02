getTimings = "SELECT `tstamp` FROM `show` WHERE `mid` = (SELECT `mid` from `movie` WHERE `Movie Name` = '{}');"
