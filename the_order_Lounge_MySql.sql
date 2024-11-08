/*******************************************************************************
   Drop database if it exists
********************************************************************************/
DROP DATABASE IF EXISTS `the_order_lounge`;


/*******************************************************************************
   Create database
********************************************************************************/
CREATE DATABASE `the_order_lounge`;


USE `the_order_lounge`;

/*******************************************************************************
   Create Tables
********************************************************************************/

CREATE TABLE `the_order_lounge`.`status`
(
    `stage` VARCHAR(150) NOT NULL PRIMARY KEY
) ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;

CREATE TABLE `the_order_lounge`.`orders`
(
    `order_id` INT NOT NULL PRIMARY KEY,
    `title` VARCHAR(150) NOT NULL,
    `customer_name` VARCHAR(150) NOT NULL,
    `room_number` VARCHAR(150) NOT NULL,
    `order_total` INT NOT NULL,
    `order_time` VARCHAR(150) NOT NULL,
    `status` VARCHAR(150) NOT NULL,
    FOREIGN KEY (`status`) REFERENCES `status`(`stage`)
) ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;

CREATE TABLE `the_order_lounge`.`order_items`
(
    `order_id` INT NOT NULL,
    `item_name` VARCHAR(300) NOT NULL,
    `quantity` INT NOT NULL,
    `price` INT NOT NULL
) ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;

CREATE TABLE `the_order_lounge`.`order_count`
(
    `order_id` INT NOT NULL PRIMARY KEY
) ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;

/*******************************************************************************
   Populate Tables
********************************************************************************/

INSERT INTO `order_count` (`order_id`) VALUES (1);

INSERT INTO `status` (`stage`) VALUES
    ("Ordered"),
    ("Reordered"),
    ("Checked"),
    ("Preparing"),
    ("Cooked"),
    ("Delivering"),
    ("Delivered"),
    ("Canceled");
    


