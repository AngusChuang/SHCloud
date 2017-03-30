/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50711
 Source Host           : localhost
 Source Database       : homeSystem_db

 Target Server Type    : MySQL
 Target Server Version : 50711
 File Encoding         : utf-8

 Date: 03/30/2017 15:43:27 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `h_alarm`
-- ----------------------------
DROP TABLE IF EXISTS `h_alarm`;
CREATE TABLE `h_alarm` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `time` varchar(255) DEFAULT NULL,
  `path` varchar(255) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `h_alarm`
-- ----------------------------
BEGIN;
INSERT INTO `h_alarm` VALUES ('10', '14:15', 'http://m2.music.126.net/a7-uKueLfjL2ge3rhraHRA==/7959364675015343.mp3', '2017-03-30 14:06:21');
COMMIT;

-- ----------------------------
--  Table structure for `h_mp3`
-- ----------------------------
DROP TABLE IF EXISTS `h_mp3`;
CREATE TABLE `h_mp3` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mp3_path` varchar(255) DEFAULT NULL,
  `mp3_name1` varchar(255) DEFAULT NULL,
  `mp3_name` varchar(255) DEFAULT NULL,
  `mp3_author` varchar(255) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `h_mp3`
-- ----------------------------
BEGIN;
INSERT INTO `h_mp3` VALUES ('6', 'http://m2.music.126.net/a7-uKueLfjL2ge3rhraHRA==/7959364675015343.mp3', '丑八怪', '意外', '薛之谦', '2017-03-30 13:51:15'), ('7', 'http://m2.music.126.net/ozBvF6hcs9wJK9PwDGw9CQ==/7964862233517713.mp3', '兄弟', '热门华语275', '龙井说唱', '2017-03-30 13:52:02');
COMMIT;

-- ----------------------------
--  Table structure for `h_mp3_mq`
-- ----------------------------
DROP TABLE IF EXISTS `h_mp3_mq`;
CREATE TABLE `h_mp3_mq` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mp3_path` varchar(255) DEFAULT NULL,
  `type` int(11) DEFAULT NULL COMMENT '0 未播放 1已经播放',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `h_mp3_mq`
-- ----------------------------
BEGIN;
INSERT INTO `h_mp3_mq` VALUES ('1', 'http://192.168.3.20:8088/static/mp3/1.mp3', '1'), ('2', 'http://m2.music.126.net/ozBvF6hcs9wJK9PwDGw9CQ==/7964862233517713.mp3', '1'), ('3', 'http://m2.music.126.net/ozBvF6hcs9wJK9PwDGw9CQ==/7964862233517713.mp3', '1');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
