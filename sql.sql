/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.5.5-10.4.10-MariaDB : Database - kudumbashree
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`kudumbashree` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `kudumbashree`;

/*Table structure for table `account` */

DROP TABLE IF EXISTS `account`;

CREATE TABLE `account` (
  `account_id` int(11) NOT NULL AUTO_INCREMENT,
  `member_id` int(11) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `balance` decimal(18,0) DEFAULT NULL,
  `a_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`account_id`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

/*Data for the table `account` */

insert  into `account`(`account_id`,`member_id`,`amount`,`date`,`balance`,`a_status`) values (15,1,'100','2022-02-20',100,'paid'),(14,2,'100','2022-02-16',100,'paid');

/*Table structure for table `attendance` */

DROP TABLE IF EXISTS `attendance`;

CREATE TABLE `attendance` (
  `attendance_id` int(11) NOT NULL AUTO_INCREMENT,
  `member_id` int(11) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`attendance_id`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `attendance` */

insert  into `attendance`(`attendance_id`,`member_id`,`date`) values (11,1,'2022-02-14'),(10,2,'2022-02-07'),(9,1,'2022-01-25'),(8,1,'2022-01-25');

/*Table structure for table `event` */

DROP TABLE IF EXISTS `event`;

CREATE TABLE `event` (
  `event_id` int(11) NOT NULL AUTO_INCREMENT,
  `event` varchar(100) DEFAULT NULL,
  `details` varchar(100) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`event_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `event` */

insert  into `event`(`event_id`,`event`,`details`,`image`) values (1,'event1','12-2-2022',NULL),(2,'event2','fghjkcghpoiurewsdfghjk','static/uploads/c335c58b-f82a-4db2-8783-8d6f2c279599doctor_reg.jpg');

/*Table structure for table `loanrequest` */

DROP TABLE IF EXISTS `loanrequest`;

CREATE TABLE `loanrequest` (
  `loanrequest_id` int(11) NOT NULL AUTO_INCREMENT,
  `member_id` int(11) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`loanrequest_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `loanrequest` */

insert  into `loanrequest`(`loanrequest_id`,`member_id`,`amount`,`date`,`status`) values (9,1,'89000','2022-02-14','accept'),(8,1,'80000','2022-02-12','accept');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `usertype` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values (1,'admin','admin','admin'),(2,'mmm','mmm','member'),(3,'aaa','aaa','member'),(4,'nnn','nnn','reject');

/*Table structure for table `meeting` */

DROP TABLE IF EXISTS `meeting`;

CREATE TABLE `meeting` (
  `meeting_id` int(11) NOT NULL AUTO_INCREMENT,
  `meeting` varchar(100) DEFAULT NULL,
  `link` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`meeting_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `meeting` */

insert  into `meeting`(`meeting_id`,`meeting`,`link`,`date`) values (1,'meeting 2','https://apps.google.com/meet/','2022-02-24');

/*Table structure for table `member` */

DROP TABLE IF EXISTS `member`;

CREATE TABLE `member` (
  `member_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `firstname` varchar(100) DEFAULT NULL,
  `lastname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`member_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `member` */

insert  into `member`(`member_id`,`login_id`,`firstname`,`lastname`,`place`,`phone`,`email`) values (1,2,'member11','szdd','ekmxcc','4598662','a@gmail.com'),(2,3,'ammu','a','ekm','45668888','a@gmail.com'),(3,4,'nimmy','df','erty','74589635488','n@gmail.com');

/*Table structure for table `payments` */

DROP TABLE IF EXISTS `payments`;

CREATE TABLE `payments` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `loanrequest_id` int(11) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `payments` */

insert  into `payments`(`payment_id`,`loanrequest_id`,`amount`,`date`) values (13,8,'2000','2022-02-26'),(12,8,'2000','2022-02-24');

/*Table structure for table `product` */

DROP TABLE IF EXISTS `product`;

CREATE TABLE `product` (
  `product_id` int(11) NOT NULL AUTO_INCREMENT,
  `productname` varchar(100) DEFAULT NULL,
  `details` varchar(100) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `product` */

insert  into `product`(`product_id`,`productname`,`details`,`image`,`status`) values (3,'shhhsd','ddddde','static/uploads/ff5974ab-f7ae-4b37-91ea-2d085bb52816doctor_reg.jpg','accept'),(4,'ahjfjnf','wsdwdef','static/uploads/256fb091-718d-4ab2-8e45-023a8d470b1fdoctor_reg.jpg','reject'),(5,'kkjgdggfv','wererer','static/uploads/3477c955-e6a8-4e94-b2c3-d852f579a9f0doctor_reg.jpg',NULL),(6,'rghghgrfg','fbgfbgfbgf','static/uploads/25db849f-c504-4b36-b95d-7f7b2dbe03f0doctor_reg.jpg',NULL),(7,'dfggbn','xfgghjjj','static/uploads/1a7ecb1c-434a-4bcf-ae16-e41d70fa37c7abc.jpg','pending'),(8,'dfhj','cgjj','static/uploads/d507a4c3-3278-4a57-95b3-f93e82d95a9fabc.jpg','pending'),(9,'product 88','ssssssssss','static/uploads/6363b8d3-85b8-4a80-8bba-c512627560d2abc.jpg','pending');

/*Table structure for table `profile` */

DROP TABLE IF EXISTS `profile`;

CREATE TABLE `profile` (
  `profile_id` int(11) NOT NULL AUTO_INCREMENT,
  `firstname` varchar(100) DEFAULT NULL,
  `lastname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`profile_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `profile` */

insert  into `profile`(`profile_id`,`firstname`,`lastname`,`place`,`phone`,`email`) values (1,'anu','a','chalakudi','2563201478','a@gmail.com'),(2,'demo','a','chalakudi','2563201478','a@gmail.com'),(3,'demo','a','chalakudi','2563201478','a@gmail.com'),(4,'demo','a','chalakudi','2563201478','a@gmail.com'),(5,'demo','a','chalakudi','2563201478','a@gmail.com'),(6,'sneha','s','ekm','8956231452','as@gmail.com');

/*Table structure for table `request` */

DROP TABLE IF EXISTS `request`;

CREATE TABLE `request` (
  `request_id` int(11) NOT NULL AUTO_INCREMENT,
  `member_id` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`request_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `request` */

insert  into `request`(`request_id`,`member_id`,`product_id`,`status`) values (1,1,2,'reject'),(2,1,2,'pending'),(3,2,5,'pending'),(4,2,6,'pending');

/*Table structure for table `store` */

DROP TABLE IF EXISTS `store`;

CREATE TABLE `store` (
  `store_id` int(11) NOT NULL AUTO_INCREMENT,
  `product_id` int(11) DEFAULT NULL,
  `storename` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`store_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `store` */

insert  into `store`(`store_id`,`product_id`,`storename`) values (1,2,'store1'),(2,2,'store1'),(3,3,'store1');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
