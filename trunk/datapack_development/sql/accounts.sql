-- ---------------------------
-- Table structure for accounts
-- ---------------------------
CREATE TABLE `accounts` (
  `login` VARCHAR(45) NOT NULL default '',
  `password` VARCHAR(45) ,
  `lastactive` INT,
  `access_level` INT,
  `lastIP` VARCHAR(20),
  PRIMARY KEY (`login`)
);
