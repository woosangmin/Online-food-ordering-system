/*******************************************************************************
   Drop database if it exists
********************************************************************************/
DROP DATABASE IF EXISTS `the_Lounge`;


/*******************************************************************************
   Create database
********************************************************************************/
CREATE DATABASE `the_lounge`;


USE `the_lounge`;

/*******************************************************************************
   Create Tables
********************************************************************************/
CREATE TABLE `the_lounge`.`menu`
(
    `title_kr` VARCHAR(150) NOT NULL PRIMARY KEY,
    `title_en` VARCHAR(150) NOT NULL,
    `available` VARCHAR(150) NOT NULL,
    `time` VARCHAR(150) NOT NULL,
    `table_name` VARCHAR(150) NOT NULL
) ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;

CREATE TABLE `the_lounge`.`sub_brunch` (
    `name_kr` VARCHAR(150) NOT NULL PRIMARY KEY,
    `name_en` VARCHAR(150) NOT NULL,
    `time_weekday` VARCHAR(150) NOT NULL,
    `time_weekend_holiday` VARCHAR(150) NOT NULL,
    `table_name` VARCHAR(150) NOT NULL,
    `type` VARCHAR(150) NOT NULL
) ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;

CREATE TABLE `the_lounge`.`sub_dine` (
    `name_kr` VARCHAR(150) NOT NULL PRIMARY KEY,
    `name_en` VARCHAR(150) NOT NULL,
    `time_weekday` VARCHAR(150) NOT NULL,
    `time_weekend_holiday` VARCHAR(150) NOT NULL,
    `table_name` VARCHAR(150) NOT NULL,
    `type` VARCHAR(150) NOT NULL
) ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;

CREATE TABLE `the_lounge`.`dining_set_menu` (
    `menu_id` INT NOT NULL PRIMARY KEY,
    `menu` VARCHAR(300) NOT NULL,
    `price` VARCHAR(150) NOT NULL
) ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;

CREATE TABLE `the_lounge`.`summer_sweet_day` (
    `menu_id` INT NOT NULL PRIMARY KEY,
    `menu` VARCHAR(300) NOT NULL,
    `price` VARCHAR(150) NOT NULL
) ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;

CREATE TABLE `the_lounge`.`brunch_set_for_2_people` (
    `menu_id` INT NOT NULL PRIMARY KEY,
    `menu` VARCHAR(300) NOT NULL,
    `price` VARCHAR(150) NOT NULL
) ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;

CREATE TABLE `the_lounge`.`dining_set_for_2_people` (
  `menu_id` INT NOT NULL PRIMARY KEY,
  `menu` VARCHAR(300) NOT NULL,
  `price` VARCHAR(150) NOT NULL
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;

CREATE TABLE `the_lounge`.`dine` (
    `menu_id` INT NOT NULL PRIMARY KEY,
    `menu` VARCHAR(300) NOT NULL,
    `price` VARCHAR(150) NOT NULL
) ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;

CREATE TABLE `the_lounge`.`dessert` (
    `menu_id` INT NOT NULL PRIMARY KEY,
    `menu` VARCHAR(300) NOT NULL,
    `price` VARCHAR(150) NOT NULL
) ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;

CREATE TABLE `the_lounge`.`sweet_platter_set_menu` (
    `menu_id` INT NOT NULL PRIMARY KEY,
    `menu` VARCHAR(300) NOT NULL,
    `sub_menu` VARCHAR(150) NOT NULL,
    `price` VARCHAR(150) NOT NULL
) ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;

CREATE TABLE `the_lounge`.`coffee_set_for_2_people` (
    `menu_id` INT NOT NULL PRIMARY KEY,
    `menu` VARCHAR(300) NOT NULL,
    `price` VARCHAR(150) NOT NULL
) ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;

CREATE TABLE `the_lounge`.`coffee` (
    `menu_id` INT NOT NULL PRIMARY KEY,
    `menu` VARCHAR(300) NOT NULL,
    `price` VARCHAR(150) NOT NULL
) ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;

CREATE TABLE `the_lounge`.`traditional_tea` (
    `menu_id` INT NOT NULL PRIMARY KEY,
    `menu` VARCHAR(300) NOT NULL,
    `price` VARCHAR(150) NOT NULL
) ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;

CREATE TABLE `the_lounge`.`fresh_squeezed_juice` (
    `menu_id` INT NOT NULL PRIMARY KEY,
    `menu` VARCHAR(300) NOT NULL,
    `price` VARCHAR(150) NOT NULL
) ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;

CREATE TABLE `the_lounge`.`ronnefeldt_tea` (
    `menu_id` INT NOT NULL PRIMARY KEY,
    `menu` VARCHAR(300) NOT NULL,
    `price` VARCHAR(150) NOT NULL
) ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;

CREATE TABLE `the_lounge`.`red_wine` (
    `menu_id` INT NOT NULL PRIMARY KEY,
    `menu` VARCHAR(300) NOT NULL,
    `price` VARCHAR(150) NOT NULL
) ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;

CREATE TABLE `the_lounge`.`champagne` (
    `menu_id` INT NOT NULL PRIMARY KEY,
    `menu` VARCHAR(300) NOT NULL,
    `price` VARCHAR(150) NOT NULL
) ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;

CREATE TABLE `the_lounge`.`rose_champagne` (
    `menu_id` INT NOT NULL PRIMARY KEY,
    `menu` VARCHAR(300) NOT NULL,
    `price` VARCHAR(150) NOT NULL
) ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;

CREATE TABLE `the_lounge`.`rose_wine` (
    `menu_id` INT NOT NULL PRIMARY KEY,
    `menu` VARCHAR(300) NOT NULL,
    `price` VARCHAR(150) NOT NULL
) ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;

CREATE TABLE `the_lounge`.`white_wine` (
    `menu_id` INT NOT NULL PRIMARY KEY,
    `menu` VARCHAR(300) NOT NULL,
    `price` VARCHAR(150) NOT NULL
) ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;

CREATE TABLE `the_lounge`.`spirit` (
    `menu_id` INT NOT NULL PRIMARY KEY,
    `menu` VARCHAR(300) NOT NULL,
    `price` VARCHAR(150) NOT NULL
) ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;

CREATE TABLE `the_lounge`.`draft_beer` (
    `menu_id` INT NOT NULL PRIMARY KEY,
    `menu` VARCHAR(300) NOT NULL,
    `price` VARCHAR(150) NOT NULL
) ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;

CREATE TABLE `the_lounge`.`bottled_beer` (
    `menu_id` INT NOT NULL PRIMARY KEY,
    `menu` VARCHAR(300) NOT NULL,
    `price` VARCHAR(150) NOT NULL
) ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;

CREATE TABLE `the_lounge`.`long_drink` (
    `menu_id` INT NOT NULL PRIMARY KEY,
    `menu` VARCHAR(300) NOT NULL,
    `price` VARCHAR(150) NOT NULL
) ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;

CREATE TABLE `the_lounge`.`soft_drink` (
    `menu_id` INT NOT NULL PRIMARY KEY,
    `menu` VARCHAR(300) NOT NULL,
    `price` VARCHAR(150) NOT NULL
) ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;

CREATE TABLE `the_lounge`.`water` (
    `menu_id` INT NOT NULL PRIMARY KEY,
    `menu` VARCHAR(300) NOT NULL,
    `price` VARCHAR(150) NOT NULL
) ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;

CREATE TABLE `the_lounge`.`macallan_whisky_promotion` (
    `menu_id` INT NOT NULL PRIMARY KEY,
    `menu` VARCHAR(300) NOT NULL,
    `price` VARCHAR(150) NOT NULL
) ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;

CREATE TABLE `the_lounge`.`happy_hour_set_menu` (
    `menu_id` INT NOT NULL PRIMARY KEY,
    `menu` VARCHAR(300) NOT NULL,
    `price` VARCHAR(150) NOT NULL
) ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;

CREATE TABLE `the_lounge`.`bar_snack` (
    `menu_id` INT NOT NULL PRIMARY KEY,
    `menu` VARCHAR(300) NOT NULL,
    `price` VARCHAR(150) NOT NULL
) ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;

CREATE TABLE `the_lounge`.`wine_set` (
    `menu_id` INT NOT NULL PRIMARY KEY,
    `menu` VARCHAR(300) NOT NULL,
    `price` VARCHAR(150) NOT NULL
) ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;

/*******************************************************************************
   Populate Tables
********************************************************************************/

-- Insert data into the Menu table
INSERT INTO `the_lounge`.`menu` (`title_kr`, `title_en`, `available`, `time`, `table_name`) VALUES
    ('브런치(주중)', 'Brunch(Weekday)', 'weekday', '10:00,23:00,21:30', 'sub_brunch'),
    ('브런치(주말, 휴일)', 'Brunch(Weekend, Holiday)', 'weekend', '10:00,21:00,20:00', 'sub_brunch'),
    ('다인(주중)', 'Dine(Weekday)', 'weekday', '10:00,23:00,21:30', 'sub_dine'),
    ('다인(주말, 휴일)', 'Dine(Weekend, Holiday)', 'weekend', '10:00,21:00,20:00', 'sub_dine');

-- Insert data into the Set_Brunch table
INSERT INTO `the_lounge`.`sub_brunch` (`name_kr`, `name_en`, `time_weekday`, `time_weekend_holiday`, `table_name`, `type`) VALUES
    ('다이닝 세트 메뉴', 'Dining Set Menu', '11:00,22:00,21:30', '11:00,21:00,20:00', 'dining_set_menu', 'combo'),
    ('더라운지 빙수 프로모션', 'Summer Sweet Day', '11:00,19:00,19:00', '11:00,19:00,19:00', 'summer_sweet_day', 'promotion'),
    ('브런치 2인 세트', 'BRUNCH SET FOR 2 PEOPLE', '11:00,14:30,14:00', '11:00,14:30,14:00', 'brunch_set_for_2_people', 'combo'),
    ('다이닝 2인 세트', 'DINING SET FOR 2 PEOPLE', '11:00,22:00,21:30', '11:00,21:00,20:00', 'dining_set_for_2_people', 'combo'),
    ('스위트 플래터 세트 메뉴', 'Sweet Platter Set Menu', '10:00,22:00,21:00', '10:00,21:00,20:00', 'sweet_platter_set_menu', 'combo'),
    ('커피 2인 세트', 'COFFEE SET FOR 2 PEOPLE', '10:00,21:00,20:00', '10:00,21:00,20:00', 'coffee_set_for_2_people', 'combo'),
    ('다인', 'DINE', '11:00,22:00,21:30', '11:00,21:00,20:00', 'dine', 'meal'),
    ('디저트', 'DESSERT', '10:00,23:00,21:00', '11:00,21:00,20:00', 'dessert', 'dessert'),
    ('커피', 'COFFEE', '10:00,23:00,21:30', '10:00,21:00,20:00', 'coffee', 'beverage'),
    ('전통차', 'TRADITIONAL TEA', '10:00,23:00,21:30', '10:00,21:00,20:00', 'traditional_tea', 'beverage'),
    ('착즙 주스', 'FRESH-SQUEEZED JUICE', '10:00,23:00,21:30', '10:00,21:00,20:00', 'fresh_squeezed_juice', 'beverage'),
    ('로네펠트 차', 'RONNEFELDT TEA', '10:00,23:00,21:30', '10:00,21:00,20:00', 'ronnefeldt_tea', 'beverage'),
    ('적포도주', 'RED WINE', '10:00,23:00,21:30', '10:00,21:00,20:00', 'red_wine', 'alcohol'),
    ('샴페인', 'CHAMPAGNE', '10:00,23:00,21:30', '10:00,21:00,20:00', 'champagne', 'alcohol'),
    ('로제 샴페인', 'ROSE CHAMPAGNE', '10:00,23:00,21:30', '10:00,21:00,20:00', 'rose_champagne', 'alcohol'),
    ('로제 와인', 'ROSE WINE', '10:00,23:00,21:30', '10:00,21:00,20:00', 'rose_wine', 'alcohol'),
    ('백포도주', 'WHITE WINE', '10:00,23:00,21:30', '10:00,21:00,20:00', 'white_wine', 'alcohol'),
    ('스피릿', 'SPIRIT', '10:00,23:00,21:30', '10:00,21:00,20:00', 'spirit', 'alcohol'),
    ('드래프트 맥주', 'DRAFT BEER', '10:00,23:00,21:30', '10:00,21:00,20:00', 'draft_beer', 'alcohol'),
    ('병맥주', 'BOTTLED BEER', '10:00,23:00,21:30', '10:00,21:00,20:00', 'bottled_beer', 'alcohol'),
    ('롱 드링크', 'LONG DRINK', '10:00,23:00,21:30', '10:00,21:00,20:00', 'long_drink', 'alcohol'),
    ('일반 음료', 'SOFT DRINK', '10:00,23:00,21:30', '10:00,21:00,20:00', 'soft_drink', 'beverage'),
    ('생수', 'WATER', '10:00,23:00,21:30', '10:00,21:00,20:00', 'water', 'beverage');

-- Insert data into the Set_Brunch table
INSERT INTO `the_lounge`.`sub_dine` (`name_kr`, `name_en`, `time_weekday`, `time_weekend_holiday`, `table_name`, `type`) VALUES
    ('맥캘란 위스키 프로모션', 'Macallan Whisky Promotion', '10:00,23:00,21:30', '10:00,21:00,20:00', 'macallan_whisky_promotion', 'promotion'),
    ('바 스낵', 'BAR SNACK', '18:00,23:00,22:00', '18:00,21:00,20:00', 'bar_snack', 'meal'),
    ('와인 세트', 'WINE SET', '18:00,23:00,22:00', '18:00,21:00,20:00', 'wine_set', 'combo'),
    ('해피 아워 세트 메뉴', 'Happy Hour Set Menu', '18:30,20:30,20:30', '18:30,20:00,20:00', 'happy_hour_set_menu', 'combo'),
    ('다이닝 세트 메뉴', 'Dining Set Menu', '11:00,22:00,21:30', '11:00,21:00,20:00', 'dining_set_menu', 'combo'),
    ('더라운지 빙수 프로모션', 'Summer Sweet Day', '11:00,19:00,19:00', '11:00,19:00,19:00', 'summer_sweet_day', 'promotion'),
    ('다이닝 2인 세트', 'DINING SET FOR 2 PEOPLE', '11:00,22:00,21:30', '11:00,21:00,20:00', 'dining_set_for_2_people', 'combo'),
    ('스위트 플래터 세트 메뉴', 'Sweet Platter Set Menu', '10:00,22:00,21:00', '10:00,21:00,20:00', 'sweet_platter_set_menu', 'combo'),
    ('커피 2인 세트', 'COFFEE SET FOR 2 PEOPLE', '10:00,22:00,21:00', '10:00,21:00,20:00', 'coffee_set_for_2_people', 'combo'),
    ('다인', 'DINE', '11:00,22:00,21:30', '11:00,21:00,20:00', 'dine', 'meal'),
    ('디저트', 'DESSERT', '10:00,23:00,21:00', '10:00,21:00,20:00', 'dessert', 'dessert'),
    ('커피', 'COFFEE', '10:00,23:00,21:30', '10:00,21:00,20:00', 'coffee', 'beverage'),
    ('전통차', 'TRADITIONAL TEA', '10:00,23:00,21:30', '10:00,21:00,20:00', 'traditional_tea', 'beverage'),
    ('착즙 주스', 'FRESH-SQUEEZED JUICE', '10:00,23:00,21:30', '10:00,21:00,20:00', 'fresh_squeezed_juice', 'beverage'),
    ('로네펠트 차', 'RONNEFELDT TEA', '10:00,23:00,21:30', '10:00,21:00,20:00', 'ronnefeldt_tea', 'beverage'),
    ('적포도주', 'RED WINE', '10:00,23:00,21:30', '10:00,21:00,20:00', 'red_wine', 'alcohol'),
    ('샴페인', 'CHAMPAGNE', '10:00,23:00,21:30', '10:00,21:00,20:00', 'champagne', 'alcohol'),
    ('로제 샴페인', 'ROSE CHAMPAGNE', '10:00,23:00,21:30', '10:00,21:00,20:00', 'rose_champagne', 'alcohol'),
    ('로제 와인', 'ROSE WINE', '10:00,23:00,21:30', '10:00,21:00,20:00', 'rose_wine', 'alcohol'),
    ('백포도주', 'WHITE WINE', '10:00,23:00,21:30', '10:00,21:00,20:00', 'white_wine', 'alcohol'),
    ('스피릿', 'SPIRIT', '10:00,23:00,21:30', '10:00,21:00,20:00', 'spirit', 'alcohol'),
    ('드래프트 맥주', 'DRAFT BEER', '10:00,23:00,21:30', '10:00,21:00,20:00', 'draft_beer', 'alcohol'),
    ('병맥주', 'BOTTLED BEER', '10:00,23:00,21:30', '10:00,21:00,20:00', 'bottled_beer', 'alcohol'),
    ('롱 드링크', 'LONG DRINK', '10:00,23:00,21:30', '10:00,21:00,20:00', 'long_drink', 'alcohol'),
    ('일반 음료', 'SOFT DRINK', '10:00,23:00,21:30', '10:00,21:00,20:00', 'soft_drink', 'beverage'),
    ('생수', 'WATER', '10:00,23:00,21:30', '10:00,21:00,20:00', 'water', 'beverage');

-- Insert data into Dining_Set_Menu table
INSERT INTO `the_lounge`.`dining_set_menu` (`menu_id`, `menu`,`price`) VALUES
    (1,
    'Beef Top Blade Steak 부채살 스테이크\nSeafood Tomato Pasta 해산물 토마토 파스타\nGreen Salad 그린 샐러드\n2 Cups of Americano 아메리카노 2잔\nBlueberry Crumble 블루베리 크럼블\nfor 2 PEOPLE 2인 기준', '110000' ),
    (2,
    'Beef Top Blade Steak 부채살 스테이크\nTruffle Cream Rigatoni 트러플 크림 리가토니\nGreen Salad 그린 샐러드\n2 Cups of Americano 아메리카노 2잔\nBlueberry Crumble 블루베리 크럼블\nfor 2 PEOPLE 2인 기준', '110000');

-- Insert data into Summer_Sweet_Day table
INSERT INTO `the_lounge`.`summer_sweet_day` (`menu_id`, `menu`, `price`) VALUES
    (3,'Red Bean Bingsu with Udo Peanut\n우도 땅콩 팥빙수', '55000'),
    (4,'Mango Bingsu\n망고 빙수', '68000');

-- Insert data into Brunch_Set_For_2_People table
INSERT INTO `the_lounge`.`brunch_set_for_2_people` (`menu_id`, `menu`, `price`) VALUES
    (5, 'French Toast 프렌치 토스트\nJambon Beurre Sandwich 잠봉뵈르 샌드위치\n2 Cups of Americano 아메리카노 2잔\nTiramisu 티라미수', '90000'),
    (6, 'French Toast 프렌치 토스트\nTruffle Cream Rigatoni 트러플 크림 리가토니\n2 Cups of Americano 아메리카노 2잔\nTiramisu 티라미수', '90000');

-- Insert data into Dining_Set_For_2_People table
INSERT INTO `the_lounge`.`dining_set_for_2_people` (`menu_id`, `menu`, `price`) VALUES
    (7, 'Beef Top Blade Steak 부채살 스테이크\nSeafood Tomato Pasta 해산물 토마토 파스타\nGreen Salad 그린 샐러드\n2 Cups of Americano 아메리카노 2잔\nBlueberry Crumble 블루베리 크럼블', '110000'),
    (8, 'Beef Top Blade Steak 부채살 스테이크\nTruffle Cream Rigatoni 트러플 크림 리가토니\nGreen Salad 그린 샐러드\n2 Cups of Americano 아메리카노 2잔\nBlueberry Crumble 블루베리 크럼블', '110000');

-- Insert data into Dine table
INSERT INTO `the_lounge`.`dine` (`menu_id`, `menu`, `price`) VALUES 
    (9, 'Beef Top Blade Steak\n부채살 스테이크', '58000'),
    (10, 'Arugula Tomato Pizza\n루꼴라 토마토 피자', '38000'),
    (11, 'Gorgonzola Pizza\n고르곤졸라 피자', '38000'),
    (12, 'Jambon Beurre Sandwich\n잠봉뵈르 샌드위치', '38000'),
    (13, 'Club Sandwich\n클럽 샌드위치', '35000'),
    (14, 'Seafood Pasta with Tomato Sauce\n해산물 토마토 파스타', '38000'),
    (15, 'Truffle Cream Rigatoni\n트러플 크림 리가토니', '38000'),
    (16, 'Eggs Benedict\n에그 베네딕트', '35000'),
    (17, 'French Toast\n프렌치 토스트', '34000'),
    (18, 'Burrata Salad\n부라타 샐러드', '35000'),
    (19, 'Prosciutto & Bocconcini Salad\n프로슈토 & 보코치니 샐러드', '26000');

-- Insert data into Dessert table
INSERT INTO `the_lounge`.`dessert` (`menu_id`, `menu`, `price`) VALUES
    (20, 'Seasonal Fruit Shortcake\n계절 과일 쇼트케이크', '25000'),
    (21, 'EBA Ice Cream EBA 아이스크림\nFrench Vanilla 프렌치 바닐라', '22000'),
    (22, 'EBA Ice Cream EBA 아이스크림\nStrawberry 딸기', '22000'),
    (23, 'EBA Ice Cream EBA 아이스크림\nSeasonal 시즌', '22000'),
    (24, 'Tiramisu 티라미수', '22000'),
    (25, 'Cheese Cake 치즈 케이크', '22000');

-- Insert data into Sweet_Platter_Set_Menu table
INSERT INTO `the_lounge`.`sweet_platter_set_menu` (`menu_id`, `menu`, `sub_menu`, `price`) VALUES
    (26, 'SWEET PLATTER A SET', '4 Piece Serving Platter 스위트 피스 4종\n2 Cups of Americano 아메리카노 2잔', '55000'),
    (27, 'SWEET PLATTER B SET', '5 Piece Serving Platter 스위트 피스 5종\nOne Dish of Savoury 부르스게타 1종\n2 Cups of Americano 아메리카노 2잔', '75000');

-- Insert data into Coffee_Set_For_2_People table
INSERT INTO `the_lounge`.`coffee_set_for_2_people` (`menu_id`, `menu`, `price`) VALUES
    (28, 'Tiramisu 티라미수\n2Cups of Americano 아메리카노 2잔', '45000'),
    (29, 'Cheese Cake 치즈케이크\n2Cups of Americano 아메리카노 2잔', '45000');

-- Insert data into Coffee table
INSERT INTO `the_lounge`.`coffee` (`menu_id`, `menu`, `price`) VALUES
    (31, 'Espresso\n에스프레소', '18000'),
    (32, 'Americano\n아메리카노', '18000'),
    (33, 'Iced Americano\n아이스 아메리카노', '19000'),
    (34, 'Café Latte\n카페 라떼', '19000'),
    (35, 'Iced Café Latte\n아이스 카페 라떼','20000'),
    (36, 'Cappuccino\n카푸치노', '19000'),
    (37, 'Iced Cappuccino\n아이스 카푸치노', '20000'),
    (38, 'Espresso Macchiato\n에스프레소 마끼아또', '19000'),
    (39, 'Café Mocha\n카페 모카', '19000'),
    (40, 'Iced Café Mocha\n아이스 카페 모카', '20000'),
    (41, 'Vanilla Latte\n바닐라 라떼', '19000'),
    (42, 'Iced Vanilla Latte\n아이스 바닐라 라떼', '20000'),
    (43, 'Caramel Macchiato\n카라멜 마끼아또', '19000'),
    (44, 'Iced Caramel Macchiato\n아이스 카라멜 마끼아또', '20000'),
    (45, 'Chocolate Milk\n핫 초코', '19000'),
    (46, 'Chocolate Milk\n아이스 초코', '20000'),
    (47, 'Affogato 아포가토\nwith EBA French Vanilla Ice Cream\nEBA 프렌치 바닐라 아이스크림', '20000');

-- Insert data into traditonal_tea table
INSERT INTO `the_lounge`.`traditional_tea` (`menu_id`, `menu`, `price`) VALUES
    (48, 'Yuja Tea\n유자차', '19000'),
    (49, 'Ginseng Tea\n인삼차', '19000'),
    (50, 'Jujube Tea\n대추차', '19000');

-- Insert data into fresh_squeezed_juice table
INSERT INTO `the_lounge`.`fresh_squeezed_juice` (`menu_id`, `menu`, `price`) VALUES
    (51, 'Watermelon Juice\n수박 주스', '25000'),
    (52, 'Fresh-Squeezed Juice Orange\n생과일 주스 오렌지', '25000'),
    (53, 'Fresh-Squeezed Juice Grapefruit\n생과일 주스 자몽', '25000'),
    (54, 'Fresh-Squeezed Juice Tomato\n생과일 주스 토마토', '25000'),
    (55, 'Fresh Lemonade\n레몬 에이드', '22000');

-- Insert data into ronnefeldt_tea table
INSERT INTO `the_lounge`.`ronnefeldt_tea` (`menu_id`, `menu`, `price`) VALUES
    (56, 'Black Tea 블랙 티\nEnglish Breakfast 잉글리시 블랙퍼스트', '19000'),
    (57, 'Black Tea 블랙 티\nAssam 아쌈', '19000'),
    (58, 'Black Tea 블랙 티\nDarjeeling 다즐링', '19000'),
    (59, 'Black Tea 블랙 티\nEarl Grey 얼그레이', '19000'),
    (60, 'Peppermint 페퍼민트', '19000'),
    (61, 'Camomile 캐모마일', '19000'),
    (62, 'Green Tea 그린 티', '19000');

-- Insert data into red_wine table
INSERT INTO `the_lounge`.`red_wine` (`menu_id`, `menu`, `price`) VALUES
    (63, 'Bouchard Pere &\nFils Bourgogne France Glass', '30000'),
    (64, 'Bouchard Pere &\nFils Bourgogne France Bottle', '120000'),
    (65, 'Gigondas Domaine\nRaspail-Ay France Bottle', '160000'),
    (66, 'Daou USA\nBottle', '220000'),
    (67, 'Freemark Abbey USA\nBottle', '250000'),
    (68, 'Harmand Geoffroy,\nGevrey-Chambertin\nFrance Bottle', '300000'),
    (69, 'Masi Riserva\nCostasera Amarone\nItaly Bottle', '420000'),
    (70, 'Far Niente Napa\nValley Cabernet\nSauvignon USA Bottle', '550000');

-- Insert data into champangne table
INSERT INTO `the_lounge`.`champagne` (`menu_id`, `menu`, `price`) VALUES
    (71, 'Vallereaux Reserve\nBrut France Bottle', '140000'),
    (72, 'Moët et Chandon Grand\nVintage France Bottle', '190000'),
    (73, 'Dom Pérignon P2\n2004 France Bottle', '1500000');

-- Insert data into rose_champagne table
INSERT INTO `the_lounge`.`rose_champagne` (`menu_id`, `menu`, `price`) VALUES
    (74, 'Ruinart Rosé\nFrance Bottle', '280000'),
    (75, 'Dom Pérignon Rosé\nVintage France Bottle', '1100000');

-- Insert data into rose_wine table
INSERT INTO `the_lounge`.`rose_wine` (`menu_id`, `menu`, `price`) VALUES
    (76, 'Clos Cibonne Cuvee\nPrestige Caroline\nRose France Bottle', '150000');

-- Insert data into white_wine table
INSERT INTO `the_lounge`.`white_wine` (`menu_id`, `menu`, `price`) VALUES
    (77, 'Cloudy Bay\nNew Zealand Glass', '30000'),
    (78, 'Cloudy Bay\nNew Zealand Bottle', '120000'),
    (79, 'Robert Denogent\nVire-Clesse\nFrance Bottle', '160000'),
    (80, 'Chateau Montelena,\nNapa Valley\nChardonnay USA Bottle', '300000');

-- Insert data into spirit table
INSERT INTO `the_lounge`.`spirit` (`menu_id`, `menu`, `price`) VALUES
    (81, 'Snow Leopard\nBottle', '200000'),      
    (82, 'Bombay Gin\nBottle', '200000'), 
    (83, 'Glenrothes 12y\nBottle', '350000'),
    (84, 'Balvenie 12y\nBottle', '450000'),
    (85, 'Macallan 12y\nDouble Cask Bottle', '450000'),
    (86, 'Glenmorangie SPIOS\nBottle', '500000'),
    (87, 'Benriach 16y\nBottle', '500000'),
    (88, 'Balvenie 14y\nGlass', '30000'),
    (89, 'Balvenie 14y\nBottle', '550000'),
    (90, 'Ballantine’s 17y\nBottle', '550000'),
    (91, 'Glenrothes 18y\nBottle', '600000'),
    (92, 'Ardbeg Corryvreckan\nBottle', '600000'),
    (93, 'Glenfiddich 18y\nGlass', '35000'),
    (94, 'Glenfiddich 18y\nBottle', '650000'),
    (95, 'Balvenie 16y\nBottle', '700000'),
    (96, 'Macallan 18y\nDouble Cask\nBottle', '1000000');

-- Insert data into draft_beer table
INSERT INTO `the_lounge`.`draft_beer` (`menu_id`, `menu`, `price`) VALUES
    (97, 'Stella Artois\n(380ml)', '20000'),
    (98, 'Maisel’s Weisse\n(375ml)', '20000');

-- Insert data into bottled_beer table
INSERT INTO `the_lounge`.`bottled_beer` (`menu_id`, `menu`, `price`) VALUES
    (99, 'Heineken', '15000'),
    (100, 'Jeju Wit Ale', '15000');

-- Insert data into long_drink table
INSERT INTO `the_lounge`.`long_drink` (`menu_id`, `menu`, `price`) VALUES
    (101, 'Gin Tonic', '20000'),
    (102, 'Whisky Soda', '25000');

-- Insert data into soft_drink table
INSERT INTO `the_lounge`.`soft_drink` (`menu_id`, `menu`, `price`) VALUES
    (103, 'Coke', '10000'),
    (104, 'Coke Zero', '10000'),
    (105, 'Sprite', '10000'),
    (106, 'Ginger Ale', '10000');

-- Insert data into water table
INSERT INTO `the_lounge`.`water` (`menu_id`, `menu`, `price`) VALUES
    (107, 'Fiji (500ml)\n피지', '10000'),
    (108, 'Sanpellegrino (250ml)\n산펠레그리노', '10000');

-- Insert data into macallan_whisky_promotion table
INSERT INTO `the_lounge`.`macallan_whisky_promotion` (`menu_id`, `menu`, `price`) VALUES
    (109, 'Macallan 12y Set\n원가 : 530000', '330000'),
    (110, 'Macallan 15y Set\n원가 : 630000', '460000'),
    (111, 'Macallan 18y Set\n원가 : 1080000', '820000');

-- Insert data into happy_hour_set_menu table
INSERT INTO `the_lounge`.`happy_hour_set_menu` (`menu_id`, `menu`, `price`) VALUES
    (112, 'Unlimited Budweiser Draft Beer\n버드와이저 생맥주 무제한\nGorgonzola Pizza\n고르곤졸라 피자\nSeafood Pasta with Tomato Sauce\n해산물 토마토 파스타', '45000'),
    (113, 'Unlimited Budweiser Draft Beer\n버드와이저 생맥주 무제한\nGorgonzola Pizza\n고르곤졸라 피자\nFried Chicken Combo & French Fries\n치킨콤보 & 감자튀김', '45000'),
    (114, 'Unlimited Budweiser Draft Beer\n버드와이저 생맥주 무제한\nGorgonzola Pizza\n고르곤졸라 피자\nNacho & Grilled Shrimp\n나쵸 & 그릴 쉬림프', '45000'),
    (115, 'Unlimited Budweiser Draft Beer\n버드와이저 생맥주 무제한\nGorgonzola Pizza\n고르곤졸라 피자\nCheese Platter\n치즈 플래터', '45000'),
    (116, 'Unlimited Budweiser Draft Beer\n버드와이저 생맥주 무제한\nSeafood Pasta with Tomato Sauce\n해산물 토마토 파스타\nFried Chicken Combo & French Fries\n치킨콤보 & 감자튀김', '45000'),
    (117, 'Unlimited Budweiser Draft Beer\n버드와이저 생맥주 무제한\nSeafood Pasta with Tomato Sauce\n해산물 토마토 파스타\nNacho & Grilled Shrimp\n나쵸 & 그릴 쉬림프', '45000'),
    (118, 'Unlimited Budweiser Draft Beer\n버드와이저 생맥주 무제한\nSeafood Pasta with Tomato Sauce\n해산물 토마토 파스타\nCheese Platter\n치즈 플래터', '45000'),
    (119, 'Unlimited Budweiser Draft Beer\n버드와이저 생맥주 무제한\nFried Chicken Combo & French Fries\n치킨콤보 & 감자튀김\nNacho & Grilled Shrimp\n나쵸 & 그릴 쉬림프', '45000'),
    (120, 'Unlimited Budweiser Draft Beer\n버드와이저 생맥주 무제한\nFried Chicken Combo & French Fries\n치킨콤보 & 감자튀김\nCheese Platter\n치즈 플래터', '45000'),
    (121, 'Unlimited Budweiser Draft Beer\n버드와이저 생맥주 무제한\nNacho & Grilled Shrimp\n나쵸 & 그릴 쉬림프\nCheese Platter\n치즈 플래터', '45000');

INSERT INTO `the_lounge`.`bar_snack` (`menu_id`, `menu`, `price`) VALUES
    (122, 'Charcuterie Platter with 5J Jamon\n샤퀴테리 플래터와 5J 하몽', '75000'),
    (123, 'Fried Chicken Combo\n프라이드 치킨 콤보', '38000'),
    (124, 'Baked Brie Cheese\n브리치즈 구이\nBrie Cheese, Honey, Nuts\n브리치즈, 꿀, 견과류', '28000'),
    (125, 'Maple Cereal French Fries\n메이플 시리얼 감자튀김', '20000'),
    (126, 'French Fries\n감자튀김', '20000'),
    (127, '모듬 올리브\nAssorted Olives', '18000');

INSERT INTO `the_lounge`.`wine_set` (`menu_id`, `menu`, `price`) VALUES
    (128, 'Charcuterie Platter with 5J Jamon\n샤퀴테리 플래터와 5J 하몽\n1 Bottle of House Wine\n하우스 와인 1병', '150000');
