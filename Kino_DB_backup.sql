-- MySQL dump 10.13  Distrib 8.3.0, for macos14.2 (arm64)
--
-- Host: localhost    Database: Kino_DB
-- ------------------------------------------------------
-- Server version	8.3.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin_pages_contacts`
--

DROP TABLE IF EXISTS `admin_pages_contacts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin_pages_contacts` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `cinema_name` varchar(20) NOT NULL,
  `adress_cinema_contacts` varchar(50) NOT NULL,
  `numbers_contacts` varchar(50) NOT NULL,
  `email_cinema_contacts` varchar(50) NOT NULL,
  `coordinates_long` varchar(12) NOT NULL,
  `coordinates_lat` varchar(12) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `logo_id` bigint DEFAULT NULL,
  `seo_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cinema_name` (`cinema_name`),
  UNIQUE KEY `logo_id` (`logo_id`),
  KEY `admin_pages_contacts_seo_id_5d7f3c98_fk_core_seomixin_id` (`seo_id`),
  CONSTRAINT `admin_pages_contacts_logo_id_ab4107f9_fk_core_galleryimage_id` FOREIGN KEY (`logo_id`) REFERENCES `core_galleryimage` (`id`),
  CONSTRAINT `admin_pages_contacts_seo_id_5d7f3c98_fk_core_seomixin_id` FOREIGN KEY (`seo_id`) REFERENCES `core_seomixin` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_pages_contacts`
--

LOCK TABLES `admin_pages_contacts` WRITE;
/*!40000 ALTER TABLE `admin_pages_contacts` DISABLE KEYS */;
/*!40000 ALTER TABLE `admin_pages_contacts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `admin_pages_mainpage`
--

DROP TABLE IF EXISTS `admin_pages_mainpage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin_pages_mainpage` (
  `seomixin_ptr_id` bigint NOT NULL,
  `status` tinyint(1) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `seo_text_main_page` longtext NOT NULL,
  PRIMARY KEY (`seomixin_ptr_id`),
  UNIQUE KEY `phone` (`phone`),
  CONSTRAINT `admin_pages_mainpage_seomixin_ptr_id_7ff6393f_fk_core_seom` FOREIGN KEY (`seomixin_ptr_id`) REFERENCES `core_seomixin` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_pages_mainpage`
--

LOCK TABLES `admin_pages_mainpage` WRITE;
/*!40000 ALTER TABLE `admin_pages_mainpage` DISABLE KEYS */;
/*!40000 ALTER TABLE `admin_pages_mainpage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `admin_pages_page`
--

DROP TABLE IF EXISTS `admin_pages_page`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin_pages_page` (
  `seomixin_ptr_id` bigint NOT NULL,
  `name` varchar(12) NOT NULL,
  `description` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `gallery_id` bigint DEFAULT NULL,
  `main_image_id` bigint DEFAULT NULL,
  `slug` varchar(255) NOT NULL,
  `description_en` longtext,
  `description_uk` longtext,
  `name_en` varchar(12) DEFAULT NULL,
  `name_uk` varchar(12) DEFAULT NULL,
  PRIMARY KEY (`seomixin_ptr_id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `slug` (`slug`),
  UNIQUE KEY `main_image_id` (`main_image_id`),
  UNIQUE KEY `name_en` (`name_en`),
  UNIQUE KEY `name_uk` (`name_uk`),
  KEY `admin_pages_page_gallery_id_830a3571_fk_core_gallery_id` (`gallery_id`),
  CONSTRAINT `admin_pages_page_gallery_id_830a3571_fk_core_gallery_id` FOREIGN KEY (`gallery_id`) REFERENCES `core_gallery` (`id`),
  CONSTRAINT `admin_pages_page_main_image_id_09da4831_fk_core_galleryimage_id` FOREIGN KEY (`main_image_id`) REFERENCES `core_galleryimage` (`id`),
  CONSTRAINT `admin_pages_page_seomixin_ptr_id_821dbae3_fk_core_seomixin_id` FOREIGN KEY (`seomixin_ptr_id`) REFERENCES `core_seomixin` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_pages_page`
--

LOCK TABLES `admin_pages_page` WRITE;
/*!40000 ALTER TABLE `admin_pages_page` DISABLE KEYS */;
INSERT INTO `admin_pages_page` VALUES (556,'Cafe-bar','Café at Our Cinema: Tasty and Convenient\r\n\r\nWe invite you to visit our cozy café, located right inside the cinema. Here you can enjoy aromatic coffee, fresh pastries, and delicious snacks before your movie or during a break. We offer a variety of drinks, light snacks, popcorn, and sweets to make your movie experience even more enjoyable.\r\n\r\nCome to us for a tasty treat and get ready for an exciting film!','2024-09-03 15:09:04.716287',1,563,2596,'cafe-bar','Café at Our Cinema: Tasty and Convenient\r\n\r\nWe invite you to visit our cozy café, located right inside the cinema. Here you can enjoy aromatic coffee, fresh pastries, and delicious snacks before your movie or during a break. We offer a variety of drinks, light snacks, popcorn, and sweets to make your movie experience even more enjoyable.\r\n\r\nCome to us for a tasty treat and get ready for an exciting film!','Кафе в нашому кінотеатрі: смачно і зручно\r\n\r\nЗапрошуємо вас завітати до нашого затишного кафе, яке розташоване прямо в кінотеатрі. Тут ви зможете насолодитися ароматною кавою, свіжою випічкою та смачними снеками перед сеансом або під час перерви. Ми пропонуємо різноманітні напої, легкі закуски, попкорн та солодощі, щоб зробити ваш кіноперегляд ще приємнішим.\r\n\r\nПриходьте до нас, щоб смачно підкріпитися і налаштуватися на захоплюючий фільм!','Cafe-bar','Кафе-бар'),(558,'Rules','Dear guests, please note that photography and video recording during screenings are strictly prohibited in our cinema. This rule is in place to protect copyright and ensure a comfortable viewing experience for all visitors. We kindly ask you to adhere to this rule and respect the work of filmmakers. Violation of this prohibition may result in administrative consequences. Thank you for your understanding and cooperation!','2024-09-03 15:09:04.726874',1,565,2616,'rules','Dear guests, please note that photography and video recording during screenings are strictly prohibited in our cinema. This rule is in place to protect copyright and ensure a comfortable viewing experience for all visitors. We kindly ask you to adhere to this rule and respect the work of filmmakers. Violation of this prohibition may result in administrative consequences. Thank you for your understanding and cooperation!','Заборона на зйомку в кінотеатрі\r\n\r\nШановні глядачі, звертаємо вашу увагу, що в нашому кінотеатрі суворо заборонено проводити фото- та відеозйомку під час сеансів. Це правило введено для захисту авторських прав та забезпечення комфортного перегляду для всіх відвідувачів. Просимо вас дотримуватись цього правила та поважати працю творців фільмів. Порушення заборони може призвести до адміністративних наслідків. Дякуємо за розуміння та співпрацю!','Rules','Правила');
/*!40000 ALTER TABLE `admin_pages_page` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=565 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (473,'Can add permission',119,'add_permission'),(474,'Can change permission',119,'change_permission'),(475,'Can delete permission',119,'delete_permission'),(476,'Can view permission',119,'view_permission'),(477,'Can add group',120,'add_group'),(478,'Can change group',120,'change_group'),(479,'Can delete group',120,'delete_group'),(480,'Can view group',120,'view_group'),(481,'Can add content type',121,'add_contenttype'),(482,'Can change content type',121,'change_contenttype'),(483,'Can delete content type',121,'delete_contenttype'),(484,'Can view content type',121,'view_contenttype'),(485,'Can add session',122,'add_session'),(486,'Can change session',122,'change_session'),(487,'Can delete session',122,'delete_session'),(488,'Can view session',122,'view_session'),(489,'Can add user',123,'add_user'),(490,'Can change user',123,'change_user'),(491,'Can delete user',123,'delete_user'),(492,'Can view user',123,'view_user'),(493,'Can add cinema',124,'add_cinema'),(494,'Can change cinema',124,'change_cinema'),(495,'Can delete cinema',124,'delete_cinema'),(496,'Can view cinema',124,'view_cinema'),(497,'Can add hall',125,'add_hall'),(498,'Can change hall',125,'change_hall'),(499,'Can delete hall',125,'delete_hall'),(500,'Can view hall',125,'view_hall'),(501,'Can add gallery',126,'add_gallery'),(502,'Can change gallery',126,'change_gallery'),(503,'Can delete gallery',126,'delete_gallery'),(504,'Can view gallery',126,'view_gallery'),(505,'Can add seo mixin',127,'add_seomixin'),(506,'Can change seo mixin',127,'change_seomixin'),(507,'Can delete seo mixin',127,'delete_seomixin'),(508,'Can view seo mixin',127,'view_seomixin'),(509,'Can add gallery image',128,'add_galleryimage'),(510,'Can change gallery image',128,'change_galleryimage'),(511,'Can delete gallery image',128,'delete_galleryimage'),(512,'Can view gallery image',128,'view_galleryimage'),(513,'Can add main page',129,'add_mainpage'),(514,'Can change main page',129,'change_mainpage'),(515,'Can delete main page',129,'delete_mainpage'),(516,'Can view main page',129,'view_mainpage'),(517,'Can add page',130,'add_page'),(518,'Can change page',130,'change_page'),(519,'Can delete page',130,'delete_page'),(520,'Can view page',130,'view_page'),(521,'Can add contacts',131,'add_contacts'),(522,'Can change contacts',131,'change_contacts'),(523,'Can delete contacts',131,'delete_contacts'),(524,'Can view contacts',131,'view_contacts'),(525,'Can add background banner',132,'add_backgroundbanner'),(526,'Can change background banner',132,'change_backgroundbanner'),(527,'Can delete background banner',132,'delete_backgroundbanner'),(528,'Can view background banner',132,'view_backgroundbanner'),(529,'Can add main page banners',133,'add_mainpagebanners'),(530,'Can change main page banners',133,'change_mainpagebanners'),(531,'Can delete main page banners',133,'delete_mainpagebanners'),(532,'Can view main page banners',133,'view_mainpagebanners'),(533,'Can add main page news banners',134,'add_mainpagenewsbanners'),(534,'Can change main page news banners',134,'change_mainpagenewsbanners'),(535,'Can delete main page news banners',134,'delete_mainpagenewsbanners'),(536,'Can view main page news banners',134,'view_mainpagenewsbanners'),(537,'Can add banner image',135,'add_bannerimage'),(538,'Can change banner image',135,'change_bannerimage'),(539,'Can delete banner image',135,'delete_bannerimage'),(540,'Can view banner image',135,'view_bannerimage'),(541,'Can add movie',136,'add_movie'),(542,'Can change movie',136,'change_movie'),(543,'Can delete movie',136,'delete_movie'),(544,'Can view movie',136,'view_movie'),(545,'Can add email template',137,'add_emailtemplate'),(546,'Can change email template',137,'change_emailtemplate'),(547,'Can delete email template',137,'delete_emailtemplate'),(548,'Can view email template',137,'view_emailtemplate'),(549,'Can add email campaign',138,'add_emailcampaign'),(550,'Can change email campaign',138,'change_emailcampaign'),(551,'Can delete email campaign',138,'delete_emailcampaign'),(552,'Can view email campaign',138,'view_emailcampaign'),(553,'Can add post',139,'add_post'),(554,'Can change post',139,'change_post'),(555,'Can delete post',139,'delete_post'),(556,'Can view post',139,'view_post'),(557,'Can add show time',140,'add_showtime'),(558,'Can change show time',140,'change_showtime'),(559,'Can delete show time',140,'delete_showtime'),(560,'Can view show time',140,'view_showtime'),(561,'Can add ticket',141,'add_ticket'),(562,'Can change ticket',141,'change_ticket'),(563,'Can delete ticket',141,'delete_ticket'),(564,'Can view ticket',141,'view_ticket');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `banners_backgroundbanner`
--

DROP TABLE IF EXISTS `banners_backgroundbanner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `banners_backgroundbanner` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `back` varchar(12) NOT NULL,
  `background_color` varchar(7) DEFAULT NULL,
  `background_image_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `background_image_id` (`background_image_id`),
  CONSTRAINT `banners_backgroundba_background_image_id_878a1993_fk_core_gall` FOREIGN KEY (`background_image_id`) REFERENCES `core_galleryimage` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `banners_backgroundbanner`
--

LOCK TABLES `banners_backgroundbanner` WRITE;
/*!40000 ALTER TABLE `banners_backgroundbanner` DISABLE KEYS */;
INSERT INTO `banners_backgroundbanner` VALUES (4,'photo',NULL,2697);
/*!40000 ALTER TABLE `banners_backgroundbanner` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `banners_bannerimage`
--

DROP TABLE IF EXISTS `banners_bannerimage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `banners_bannerimage` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `url` varchar(200) DEFAULT NULL,
  `gallery_image_id` bigint NOT NULL,
  `main_page_banner_id` bigint DEFAULT NULL,
  `news_banner_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `banners_bannerimage_gallery_image_id_9ea3821a_fk_core_gall` (`gallery_image_id`),
  KEY `banners_bannerimage_main_page_banner_id_475143ac_fk_banners_m` (`main_page_banner_id`),
  KEY `banners_bannerimage_news_banner_id_650378c2_fk_banners_m` (`news_banner_id`),
  CONSTRAINT `banners_bannerimage_gallery_image_id_9ea3821a_fk_core_gall` FOREIGN KEY (`gallery_image_id`) REFERENCES `core_galleryimage` (`id`),
  CONSTRAINT `banners_bannerimage_main_page_banner_id_475143ac_fk_banners_m` FOREIGN KEY (`main_page_banner_id`) REFERENCES `banners_mainpagebanners` (`id`),
  CONSTRAINT `banners_bannerimage_news_banner_id_650378c2_fk_banners_m` FOREIGN KEY (`news_banner_id`) REFERENCES `banners_mainpagenewsbanners` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `banners_bannerimage`
--

LOCK TABLES `banners_bannerimage` WRITE;
/*!40000 ALTER TABLE `banners_bannerimage` DISABLE KEYS */;
INSERT INTO `banners_bannerimage` VALUES (33,'https://leronochka.com/legenda',2681,8,NULL),(34,NULL,2693,8,NULL),(35,NULL,2680,NULL,11),(36,NULL,2688,NULL,11);
/*!40000 ALTER TABLE `banners_bannerimage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `banners_mainpagebanners`
--

DROP TABLE IF EXISTS `banners_mainpagebanners`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `banners_mainpagebanners` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `rotation_speed` int NOT NULL,
  `status` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `banners_mainpagebanners`
--

LOCK TABLES `banners_mainpagebanners` WRITE;
/*!40000 ALTER TABLE `banners_mainpagebanners` DISABLE KEYS */;
INSERT INTO `banners_mainpagebanners` VALUES (8,4000000,1);
/*!40000 ALTER TABLE `banners_mainpagebanners` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `banners_mainpagenewsbanners`
--

DROP TABLE IF EXISTS `banners_mainpagenewsbanners`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `banners_mainpagenewsbanners` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `rotation_speed` int NOT NULL,
  `status` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `banners_mainpagenewsbanners`
--

LOCK TABLES `banners_mainpagenewsbanners` WRITE;
/*!40000 ALTER TABLE `banners_mainpagenewsbanners` DISABLE KEYS */;
INSERT INTO `banners_mainpagenewsbanners` VALUES (11,2000,1);
/*!40000 ALTER TABLE `banners_mainpagenewsbanners` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cinemas_cinema`
--

DROP TABLE IF EXISTS `cinemas_cinema`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cinemas_cinema` (
  `seomixin_ptr_id` bigint NOT NULL,
  `name` varchar(20) NOT NULL,
  `description` longtext NOT NULL,
  `city` varchar(12) NOT NULL,
  `gallery_id` bigint DEFAULT NULL,
  `logo_id` bigint DEFAULT NULL,
  `main_image_id` bigint DEFAULT NULL,
  `slug` varchar(255) NOT NULL,
  `name_en` varchar(20) DEFAULT NULL,
  `name_uk` varchar(20) DEFAULT NULL,
  `description_en` longtext,
  `description_uk` longtext,
  PRIMARY KEY (`seomixin_ptr_id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `slug` (`slug`),
  UNIQUE KEY `logo_id` (`logo_id`),
  UNIQUE KEY `main_image_id` (`main_image_id`),
  UNIQUE KEY `name_en` (`name_en`),
  UNIQUE KEY `name_uk` (`name_uk`),
  KEY `cinemas_cinema_gallery_id_93f785c0_fk_core_gallery_id` (`gallery_id`),
  CONSTRAINT `cinemas_cinema_gallery_id_93f785c0_fk_core_gallery_id` FOREIGN KEY (`gallery_id`) REFERENCES `core_gallery` (`id`),
  CONSTRAINT `cinemas_cinema_logo_id_4ef9cd8e_fk_core_galleryimage_id` FOREIGN KEY (`logo_id`) REFERENCES `core_galleryimage` (`id`),
  CONSTRAINT `cinemas_cinema_main_image_id_23b02c67_fk_core_galleryimage_id` FOREIGN KEY (`main_image_id`) REFERENCES `core_galleryimage` (`id`),
  CONSTRAINT `cinemas_cinema_seomixin_ptr_id_b00ebcd8_fk_core_seomixin_id` FOREIGN KEY (`seomixin_ptr_id`) REFERENCES `core_seomixin` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cinemas_cinema`
--

LOCK TABLES `cinemas_cinema` WRITE;
/*!40000 ALTER TABLE `cinemas_cinema` DISABLE KEYS */;
INSERT INTO `cinemas_cinema` VALUES (547,'Супутник','Супутник - сучасний 6-тизальний мультиплекс, що поєднує в собі все найкраще, що є сьогодні в галузі кіно в світі.\r\n\r\nНайвища якість кінопоказу в нашому кінотеатрі досягається завдяки новітньому обладнанню, з можливістю показу кіно у форматах 2D і популярному сьогодні 3D, із застосуванням спеціальних окулярів зі стереоскопічним ефектом.\r\n\r\nКінозали відрізняються високим рівнем комфорту, а також відповідають найвищим вимогам дизайну. Унікальні екрани підвищеної яскравості забезпечують кращу якість зображення. Зручні м\'які крісла з ортопедичним ефектом забезпечені підставками для попкорну та напоїв, а також в залі Альфа можна піднімати підлокітники, що особливо  зручно для закоханих парочок. Величезною перевагою є велика відстань між рядами в залах.','Київ',554,2704,2701,'suputnik','Suputnik','Супутник','Sputnik is a modern six-screen multiplex that combines the best of today\'s global cinema industry.\r\n\r\nThe highest quality of movie screenings in our theater is achieved through state-of-the-art equipment, allowing films to be shown in both 2D and the popular 3D format using special stereoscopic glasses.\r\n\r\nThe cinemas are characterized by a high level of comfort and meet the highest design standards. Unique high-brightness screens provide superior image quality. Comfortable soft seats with an orthopedic effect are equipped with holders for popcorn and drinks, and in the Alpha hall, armrests can be lifted, which is especially convenient for couples. A major advantage is the large distance between rows in the halls.','Супутник - сучасний 6-тизальний мультиплекс, що поєднує в собі все найкраще, що є сьогодні в галузі кіно в світі.\r\n\r\nНайвища якість кінопоказу в нашому кінотеатрі досягається завдяки новітньому обладнанню, з можливістю показу кіно у форматах 2D і популярному сьогодні 3D, із застосуванням спеціальних окулярів зі стереоскопічним ефектом.\r\n\r\nКінозали відрізняються високим рівнем комфорту, а також відповідають найвищим вимогам дизайну. Унікальні екрани підвищеної яскравості забезпечують кращу якість зображення. Зручні м\'які крісла з ортопедичним ефектом забезпечені підставками для попкорну та напоїв, а також в залі Альфа можна піднімати підлокітники, що особливо  зручно для закоханих парочок. Величезною перевагою є велика відстань між рядами в залах.'),(548,'Кіноман','Кінотеатр оснащений високоякісним устаткуванням: звуковою системою JBL, цифровими проекторами BARCO та CHRISTIE, процесорами Dolby. Спеціальне акустичне покриття дозволяє максимально передати звукові спецефекти новітніх блокбастерів, це звук, який пронизує все тіло.','Київ',555,2708,2709,'kinoman','Kinoman','Кіноман','Kinoman','Кінотеатр оснащений високоякісним устаткуванням: звуковою системою JBL, цифровими проекторами BARCO та CHRISTIE, процесорами Dolby. Спеціальне акустичне покриття дозволяє максимально передати звукові спецефекти новітніх блокбастерів, це звук, який пронизує все тіло.'),(549,'Мультиплекс','Public-key 4thgeneration analyzer','Port Melissa',556,2626,2616,'multiplex','Multiplex','Мультиплекс','Public-key 4thgeneration analyzer','Public-key 4thgeneration analyzer');
/*!40000 ALTER TABLE `cinemas_cinema` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cinemas_hall`
--

DROP TABLE IF EXISTS `cinemas_hall`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cinemas_hall` (
  `seomixin_ptr_id` bigint NOT NULL,
  `name` varchar(20) NOT NULL,
  `description` longtext NOT NULL,
  `schema_json` json NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `gallery_id` bigint DEFAULT NULL,
  `main_image_id` bigint DEFAULT NULL,
  `schema_picture_id` bigint DEFAULT NULL,
  `cinema_hall_id` bigint DEFAULT NULL,
  `slug` varchar(255) NOT NULL,
  `description_en` longtext,
  `description_uk` longtext,
  `name_en` varchar(20) DEFAULT NULL,
  `name_uk` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`seomixin_ptr_id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `slug` (`slug`),
  UNIQUE KEY `main_image_id` (`main_image_id`),
  UNIQUE KEY `schema_picture_id` (`schema_picture_id`),
  UNIQUE KEY `name_en` (`name_en`),
  UNIQUE KEY `name_uk` (`name_uk`),
  KEY `cinemas_hall_cinema_hall_id_ea13aa0b_fk_cinemas_c` (`cinema_hall_id`),
  KEY `cinemas_hall_gallery_id_ef4b4d64_fk_core_gallery_id` (`gallery_id`),
  CONSTRAINT `cinemas_hall_cinema_hall_id_ea13aa0b_fk_cinemas_c` FOREIGN KEY (`cinema_hall_id`) REFERENCES `cinemas_cinema` (`seomixin_ptr_id`),
  CONSTRAINT `cinemas_hall_gallery_id_ef4b4d64_fk_core_gallery_id` FOREIGN KEY (`gallery_id`) REFERENCES `core_gallery` (`id`),
  CONSTRAINT `cinemas_hall_main_image_id_aef86349_fk_core_galleryimage_id` FOREIGN KEY (`main_image_id`) REFERENCES `core_galleryimage` (`id`),
  CONSTRAINT `cinemas_hall_schema_picture_id_183ed8f2_fk_core_galleryimage_id` FOREIGN KEY (`schema_picture_id`) REFERENCES `core_galleryimage` (`id`),
  CONSTRAINT `cinemas_hall_seomixin_ptr_id_31839744_fk_core_seomixin_id` FOREIGN KEY (`seomixin_ptr_id`) REFERENCES `core_seomixin` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cinemas_hall`
--

LOCK TABLES `cinemas_hall` WRITE;
/*!40000 ALTER TABLE `cinemas_hall` DISABLE KEYS */;
INSERT INTO `cinemas_hall` VALUES (550,'Альфа','В залі Альфа можна піднімати підлокітники, що особливо  зручно для закоханих парочок. Величезною перевагою є велика відстань між рядами в залах.','{\"rows\": [{\"seats\": [{\"status\": \"available\", \"seat_number\": 1}, {\"status\": \"available\", \"seat_number\": 2}, {\"status\": \"available\", \"seat_number\": 3}, {\"status\": \"available\", \"seat_number\": 4}, {\"status\": \"available\", \"seat_number\": 5}], \"row_number\": 1}, {\"seats\": [{\"status\": \"available\", \"seat_number\": 1}, {\"status\": \"available\", \"seat_number\": 2}, {\"status\": \"available\", \"seat_number\": 3}, {\"status\": \"available\", \"seat_number\": 4}, {\"status\": \"available\", \"seat_number\": 5}], \"row_number\": 2}, {\"seats\": [{\"status\": \"available\", \"seat_number\": 1}, {\"status\": \"available\", \"seat_number\": 2}, {\"status\": \"available\", \"seat_number\": 3}, {\"status\": \"available\", \"seat_number\": 4}, {\"status\": \"available\", \"seat_number\": 5}], \"row_number\": 3}, {\"seats\": [{\"status\": \"available\", \"seat_number\": 1}, {\"status\": \"available\", \"seat_number\": 2}, {\"status\": \"available\", \"seat_number\": 3}, {\"status\": \"available\", \"seat_number\": 4}, {\"status\": \"available\", \"seat_number\": 5}], \"row_number\": 4}, {\"seats\": [{\"status\": \"available\", \"seat_number\": 1}, {\"status\": \"available\", \"seat_number\": 2}, {\"status\": \"available\", \"seat_number\": 3}, {\"status\": \"available\", \"seat_number\": 4}, {\"status\": \"available\", \"seat_number\": 5}], \"row_number\": 5}, {\"seats\": [{\"status\": \"available\", \"seat_number\": 1}, {\"status\": \"available\", \"seat_number\": 2}, {\"status\": \"available\", \"seat_number\": 3}, {\"status\": \"available\", \"seat_number\": 4}, {\"status\": \"available\", \"seat_number\": 5}], \"row_number\": 6}, {\"seats\": [{\"status\": \"available\", \"seat_number\": 1}, {\"status\": \"available\", \"seat_number\": 2}, {\"status\": \"available\", \"seat_number\": 3}, {\"status\": \"available\", \"seat_number\": 4}, {\"status\": \"available\", \"seat_number\": 5}], \"row_number\": 7}, {\"seats\": [{\"status\": \"available\", \"seat_number\": 1}, {\"status\": \"available\", \"seat_number\": 2}, {\"status\": \"available\", \"seat_number\": 3}, {\"status\": \"available\", \"seat_number\": 4}, {\"status\": \"available\", \"seat_number\": 5}], \"row_number\": 8}]}','2024-09-03 15:09:04.667372',557,2584,2650,547,'mrs-dark-spring','В залі Альфа можна піднімати підлокітники, що особливо  зручно для закоханих парочок. Величезною перевагою є велика відстань між рядами в залах.','В залі Альфа можна піднімати підлокітники, що особливо  зручно для закоханих парочок. Величезною перевагою є велика відстань між рядами в залах.','Альфа','Альфа'),(551,'VIP-зал','Справжні кіномани неодмінно оцінять наші VIP-зали, які обладнані зручними і м’якими кріслами-реклайнерами. Вони розкладаються, як крісла в салоні першого класу авіалайнера, – так само можна не лише сидіти, але й лежати.','{\"rows\": [{\"seats\": [{\"status\": \"available\", \"seat_number\": 1}, {\"status\": \"available\", \"seat_number\": 2}, {\"status\": \"available\", \"seat_number\": 3}, {\"status\": \"available\", \"seat_number\": 4}, {\"status\": \"available\", \"seat_number\": 5}], \"row_number\": 1}, {\"seats\": [{\"status\": \"available\", \"seat_number\": 1}, {\"status\": \"available\", \"seat_number\": 2}, {\"status\": \"available\", \"seat_number\": 3}, {\"status\": \"available\", \"seat_number\": 4}, {\"status\": \"available\", \"seat_number\": 5}], \"row_number\": 2}, {\"seats\": [{\"status\": \"available\", \"seat_number\": 1}, {\"status\": \"available\", \"seat_number\": 2}, {\"status\": \"available\", \"seat_number\": 3}, {\"status\": \"available\", \"seat_number\": 4}, {\"status\": \"available\", \"seat_number\": 5}], \"row_number\": 3}, {\"seats\": [{\"status\": \"available\", \"seat_number\": 1}, {\"status\": \"available\", \"seat_number\": 2}, {\"status\": \"available\", \"seat_number\": 3}, {\"status\": \"available\", \"seat_number\": 4}, {\"status\": \"available\", \"seat_number\": 5}], \"row_number\": 4}, {\"seats\": [{\"status\": \"available\", \"seat_number\": 1}, {\"status\": \"available\", \"seat_number\": 2}, {\"status\": \"available\", \"seat_number\": 3}, {\"status\": \"available\", \"seat_number\": 4}, {\"status\": \"available\", \"seat_number\": 5}], \"row_number\": 5}, {\"seats\": [{\"status\": \"available\", \"seat_number\": 1}, {\"status\": \"available\", \"seat_number\": 2}, {\"status\": \"available\", \"seat_number\": 3}, {\"status\": \"available\", \"seat_number\": 4}, {\"status\": \"available\", \"seat_number\": 5}], \"row_number\": 6}, {\"seats\": [{\"status\": \"available\", \"seat_number\": 1}, {\"status\": \"available\", \"seat_number\": 2}, {\"status\": \"available\", \"seat_number\": 3}, {\"status\": \"available\", \"seat_number\": 4}, {\"status\": \"available\", \"seat_number\": 5}], \"row_number\": 7}, {\"seats\": [{\"status\": \"available\", \"seat_number\": 1}, {\"status\": \"available\", \"seat_number\": 2}, {\"status\": \"available\", \"seat_number\": 3}, {\"status\": \"available\", \"seat_number\": 4}, {\"status\": \"available\", \"seat_number\": 5}], \"row_number\": 8}]}','2024-09-03 15:09:04.672450',558,2650,2709,548,'star-choose-much','Справжні кіномани неодмінно оцінять наші VIP-зали, які обладнані зручними і м’якими кріслами-реклайнерами. Вони розкладаються, як крісла в салоні першого класу авіалайнера, – так само можна не лише сидіти, але й лежати.','Справжні кіномани неодмінно оцінять наші VIP-зали, які обладнані зручними і м’якими кріслами-реклайнерами. Вони розкладаються, як крісла в салоні першого класу авіалайнера, – так само можна не лише сидіти, але й лежати.','VIP-зал','VIP-зал'),(552,'Mention clearly.','Learn beat his mean. True structure sure bed door each beyond.\r\nLate run notice course ahead forget war protect.','{\"rows\": [{\"seats\": [{\"status\": \"available\", \"seat_number\": 1}, {\"status\": \"available\", \"seat_number\": 2}, {\"status\": \"available\", \"seat_number\": 3}], \"row_number\": 1}, {\"seats\": [{\"status\": \"available\", \"seat_number\": 1}, {\"status\": \"available\", \"seat_number\": 2}, {\"status\": \"available\", \"seat_number\": 3}], \"row_number\": 2}]}','2024-09-03 15:09:04.678283',559,2621,2622,549,'mention-clearly','Learn beat his mean. True structure sure bed door each beyond.\r\nLate run notice course ahead forget war protect.','Learn beat his mean. True structure sure bed door each beyond.\r\nLate run notice course ahead forget war protect.','Mention clearly.','Mention clearly.');
/*!40000 ALTER TABLE `cinemas_hall` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_gallery`
--

DROP TABLE IF EXISTS `core_gallery`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_gallery` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=605 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_gallery`
--

LOCK TABLES `core_gallery` WRITE;
/*!40000 ALTER TABLE `core_gallery` DISABLE KEYS */;
INSERT INTO `core_gallery` VALUES (549),(550),(551),(552),(553),(554),(555),(556),(557),(558),(559),(560),(561),(562),(563),(564),(565),(566),(567),(568),(569),(570),(571),(572),(573),(574),(575),(576),(577),(578),(579),(580),(581),(582),(583),(584),(585),(586),(587),(588),(589),(590),(591),(592),(593),(594),(595),(596),(597),(598),(599),(600),(601),(602),(603),(604);
/*!40000 ALTER TABLE `core_gallery` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_galleryimage`
--

DROP TABLE IF EXISTS `core_galleryimage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_galleryimage` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `alt_text` varchar(20) NOT NULL,
  `gallery_id` bigint DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `core_galleryimage_gallery_id_a3830510_fk_core_gallery_id` (`gallery_id`),
  CONSTRAINT `core_galleryimage_gallery_id_a3830510_fk_core_gallery_id` FOREIGN KEY (`gallery_id`) REFERENCES `core_gallery` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2836 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_galleryimage`
--

LOCK TABLES `core_galleryimage` WRITE;
/*!40000 ALTER TABLE `core_galleryimage` DISABLE KEYS */;
INSERT INTO `core_galleryimage` VALUES (2576,'hall_banner2',NULL,'images/hall_banner2_gicOToS.webp'),(2580,'interstallarbanner',NULL,'images/interstallarbanner_MJlhoSO.jpg'),(2584,'hall_banner3',NULL,'images/hall_banner3_Mpl3vgP.jpg'),(2588,'images (4)',NULL,'images/images_4_CH4L9rt.jpeg'),(2589,'.DS_Store',553,'images/.DS_Store_WEVQ4qY'),(2590,'Kalki--705x750-5c0e8',553,'images/Kalki--705x750-5c0e8f80-2f97-11ef-99b5-d35223c98590_wIDMhB7.avif'),(2591,'Interstellar-Poster',553,'images/Interstellar-Poster_uAhbohC.jpg'),(2592,'images',NULL,'images/images_amOdGk1.jpeg'),(2596,'movies-in-2019',NULL,'images/movies-in-2019_ZEjDUn1.webp'),(2597,'spider poster',NULL,'images/spider_poster_rmulQHy.jpeg'),(2601,'images (3)',NULL,'images/images_3_Hbkl2Mx.jpeg'),(2602,'ella-purnell-wildlik',NULL,'images/ella-purnell-wildlike-featured-1_AfxEsMU.avif'),(2603,'duna1',556,'images/duna1_s6NhHI4.jpeg'),(2604,'news baner',556,'images/news_baner_3NDBT8l.jpeg'),(2605,'realistic-webinar-te',556,'images/realistic-webinar-template-movie-premiere-event_23-2149496022_IOTPu24.jpg'),(2606,'harry-potter-movies',NULL,'images/harry-potter-movies_rdF19Lg.avif'),(2607,'matrix',NULL,'images/matrix_4z0XVvU.png'),(2611,'harry-potter-movies-',NULL,'images/harry-potter-movies-in-order-1-1677691321964_mbIIDdY.jpg'),(2612,'multiplex_logo',NULL,'images/multiplex_logo_QMQekh7.png'),(2616,'prom_banner',NULL,'images/prom_banner_ru8hKtt.png'),(2617,'logo',NULL,'images/logo_GYSxrIZ.png'),(2618,'deadpoolandwolverine',559,'images/deadpoolandwolverine_lob_crd_03_o8NLtNJ.jpg'),(2619,'the_fall_guy',559,'images/the_fall_guy_UgkmFmX.webp'),(2620,'cinema-movie-film-fe',559,'images/cinema-movie-film-festival-background_1017-23458_1_3hZSv6N.avif'),(2621,'logan_584x800_9a5af3',NULL,'images/logan_584x800_9a5af33a_HIjTPl4.jpeg'),(2622,'duna3',NULL,'images/duna3_hd5RJ5l.jpeg'),(2626,'Copy-of-800-x-500-Bl',NULL,'images/Copy-of-800-x-500-Blog-Post-13_OSXEUam.jpg'),(2627,'hall_gallery3',561,'images/hall_gallery3_QZ2WvF7.jpg'),(2628,'cinema people',561,'images/cinema_people_dn2A8ir.jpeg'),(2629,'barbi3',561,'images/barbi3_M2g3Slr.png'),(2630,'inter',NULL,'images/inter_SpvxugC.jpeg'),(2631,'news',562,'images/news_LrUNtA4.jpeg'),(2632,'godzilla1',562,'images/godzilla1_jYUpEKP.jpeg'),(2633,'cinema_banner',562,'images/cinema_banner_ryx7g5Q.jpeg'),(2634,'harry-potter',NULL,'images/harry-potter_sNpO4FR.webp'),(2635,'spider2',563,'images/spider2_CGTCdXT.jpg'),(2636,'sputnik',563,'images/sputnik_QxwFSF8.jpeg'),(2637,'cinema-movie-film-fe',563,'images/cinema-movie-film-festival-background_1017-23458_p8FCPjR.avif'),(2638,'intro-1637362771',NULL,'images/intro-1637362771_jVRe4ev.webp'),(2641,'e997ec64-07d1-45e6-a',564,'images/e997ec64-07d1-45e6-a9ae-ec644adbdbe8-theboys_rU7HOn5.jpg'),(2642,'hall_banner',NULL,'images/hall_banner_kS22yBD.webp'),(2643,'multi',565,'images/multi_SxSB4Y3.jpeg'),(2644,'MV5BNmQ0ODBhMjUtNDRh',565,'images/MV5BNmQ0ODBhMjUtNDRhOC00MGQzLTk5MTAtZDliODg5NmU5MjZhXkEyXkFqcGdeQXVyNDUyOTg3Njg.__f7xnIU4.jpg'),(2645,'gall_guy',565,'images/gall_guy_mY2cTS2.jpeg'),(2646,'hall_schema1',NULL,'images/hall_schema1_mZEWwtF.png'),(2647,'barbi',NULL,'images/barbi_jk91rhT.jpeg'),(2648,'thenewsminute_2024-0',NULL,'images/thenewsminute_2024-02_86a005d0-9e21-44bb-afc2-629758fd6e08_Razakar_movie_poster__VwM5DHo.avif'),(2649,'kinoman',NULL,'images/kinoman_LsMXKyA.jpeg'),(2650,'hall_schema3',NULL,'images/hall_schema3_YBKxvZ7.png'),(2651,'movie-trivia',NULL,'images/movie-trivia_toqW4RJ.jpg'),(2652,'inter_poster',NULL,'images/inter_poster_tyi8wEc.png'),(2653,'inter_poster',NULL,'images/inter_poster_7lcoszO.jpg'),(2654,'hall_schema2',NULL,'images/hall_schema2_1J4hTK1.png'),(2655,'duna',NULL,'images/duna_p5upqsl.jpg'),(2658,'duna3',551,'images/duna3_hd5RJ5l_HvWVaRc.jpeg'),(2659,'duna',551,'images/duna_p5upqsl_Q7mMUX5.jpg'),(2660,'hall_banner2',557,'images/hall_banner2_gicOToS_OfdmV1J.webp'),(2661,'hall_banner3',557,'images/hall_banner3_Mpl3vgP_g0x5aJv.jpg'),(2662,'hall_banner',557,'images/hall_banner_kS22yBD_YDJDlj5.webp'),(2664,'kinoman',555,'images/kinoman_LsMXKyA_cI9Zmxv.jpeg'),(2665,'hall_banner2',558,'images/hall_banner2_gicOToS_qxaKBfg.webp'),(2666,'hall_banner3',558,'images/hall_banner3_Mpl3vgP_fhNNXj7.jpg'),(2667,'hall_banner',558,'images/hall_banner_kS22yBD_ZapQCWO.webp'),(2668,'images (3)',566,'images/images_3_Hbkl2Mx_6pCIgfP.jpeg'),(2669,'prom_banner',566,'images/prom_banner_ru8hKtt_3Pz8vLl.png'),(2670,'movies-in-2019',567,''),(2671,'prom_banner',567,''),(2672,'multiplex_logo',567,'images/multiplex_logo_QMQekh7_dmj8T6o.png'),(2673,'barbi1',NULL,'images/barbi1_EeQa4Do.webp'),(2674,'barbi3',NULL,'images/barbi3_qTn2IWt.png'),(2675,'barbi2',NULL,'images/barbi2.jpg'),(2676,'barbi1',549,'images/barbi1_EeQa4Do_U5Z4cpa.webp'),(2677,'barbi3',549,'images/barbi3_qTn2IWt_lQZw8pE.png'),(2678,'barbi2',549,'images/barbi2_smMrLcZ.jpg'),(2679,'duna1',NULL,'images/duna1_wwctbPo.jpeg'),(2680,'duna3',NULL,'images/duna3_8q6IZEL.jpeg'),(2681,'Interstellar-Poster',NULL,'images/Interstellar-Poster_AoROin9.jpg'),(2682,'sputnik',NULL,'images/sputnik_U8iIz7o.jpeg'),(2683,'inter',NULL,'images/inter_oqbZFOU.jpeg'),(2684,'interstallarbanner',550,'images/interstallarbanner_MJlhoSO_mr8CXxp.jpg'),(2685,'Interstellar-Poster',550,'images/Interstellar-Poster_AoROin9_qG4PoVM.jpg'),(2686,'inter',550,'images/inter_oqbZFOU_G8cP9Y7.jpeg'),(2687,'duna1',551,'images/duna1_wwctbPo_mUWymkZ.jpeg'),(2688,'duna_main',NULL,'images/duna_BTfWIzm.jpeg'),(2690,'spider poster',NULL,'images/spider_poster_HtosIkV.jpeg'),(2691,'spider2',NULL,'images/spider2_uKNaHUg.jpg'),(2692,'spider man 1',NULL,'images/spider_man_1_sfKsTfl.png'),(2693,'SpideyHomecoming (1)',NULL,'images/SpideyHomecoming_1_z99qvYo.jpg'),(2694,'spider2',552,'images/spider2_uKNaHUg_5zSYMf1.jpg'),(2695,'spider man 1',552,'images/spider_man_1_sfKsTfl_he8KjD4.png'),(2696,'SpideyHomecoming (1)',552,'images/SpideyHomecoming_1_z99qvYo_UkCsCRx.jpg'),(2697,'back_yellow',NULL,'images/back_yellow.jpg'),(2698,'images (4)',560,'images/images_4_CH4L9rt_5H8P79K.jpeg'),(2699,'ella-purnell-wildlik',564,''),(2701,'suputnik1',NULL,'images/suputnik1.jpg'),(2702,'suputnik2',NULL,'images/suputnik2.jpg'),(2703,'suputnik3',NULL,'images/suputnik3.jpg'),(2704,'suputnik_logo',NULL,'images/suputnik_logo_V2Cje9r.png'),(2705,'suputnik1',554,'images/suputnik1_kqPOeKg.jpg'),(2706,'suputnik2',554,'images/suputnik2_V8CA23G.jpg'),(2707,'suputnik3',554,'images/suputnik3_MI9LLpS.jpg'),(2708,'kinoman_logo_5geFulh',NULL,'images/kinoman_logo_5geFulh_PzPwoPh.png'),(2709,'kinoman',NULL,'images/kinoman_ia44v8y.jpeg'),(2710,'kinoman1',NULL,'images/kinoman1.jpg'),(2711,'kinoman1',555,'images/kinoman1_XkPc1xB.jpg'),(2712,'movies-in-2019',568,'images/movies-in-2019_ZEjDUn1_0AJtCXT.webp'),(2713,'duna3',568,'images/duna3_hd5RJ5l_SO5Kpwr.jpeg'),(2714,'harry-potter-movies-',569,'images/harry-potter-movies-in-order-1-1677691321964_mbIIDdY_WX8VBAJ.jpg'),(2715,'intro-1637362771',569,'images/intro-1637362771_jVRe4ev_GAWFUie.webp'),(2716,'logo',570,'images/logo_GYSxrIZ_GXyM7xF.png'),(2717,'hall_banner2',571,'images/hall_banner2_gicOToS_MzwuBDd.webp'),(2718,'movies-in-2019',572,'images/movies-in-2019_ZEjDUn1_hjZSDbV.webp'),(2719,'harry-potter-movies-',573,'images/harry-potter-movies-in-order-1-1677691321964_mbIIDdY_lcivIny.jpg'),(2720,'logan_584x800_9a5af3',574,'images/logan_584x800_9a5af33a_HIjTPl4_XFabhNi.jpeg'),(2721,'multiplex_logo',575,''),(2722,'barbi',575,''),(2723,'prom_banner',575,'images/prom_banner_ru8hKtt_QFIbKWJ.png'),(2724,'matrix',576,'images/matrix_4z0XVvU_f3qv2c0.png'),(2725,'harry-potter-movies-',577,'images/harry-potter-movies-in-order-1-1677691321964_mbIIDdY_o0PgpXS.jpg'),(2726,'images (3)',578,'images/images_3_Hbkl2Mx_sfQmNRq.jpeg'),(2727,'matrix',579,'images/matrix_4z0XVvU_WmGbUng.png'),(2728,'hall_banner2',580,'images/hall_banner2_gicOToS_bi7U3MC.webp'),(2729,'images',581,'images/images_amOdGk1_QmCL3no.jpeg'),(2730,'logan_584x800_9a5af3',582,'images/logan_584x800_9a5af33a_HIjTPl4_Pg0uGdI.jpeg'),(2732,'hall_banner2',584,'images/hall_banner2_gicOToS_BqtLjdC.webp'),(2735,'hall_banner2',586,''),(2736,'matrix',587,'images/matrix_4z0XVvU_lW4lzZr.png'),(2737,'news',588,'images/news_1GiIVJd.png'),(2738,'images (2)',588,'images/images_2_yMq0lFE.jpeg'),(2739,'arrival',588,'images/arrival_T0Rjj3q.jpeg'),(2740,'hall_banner2',NULL,'images/hall_banner2_f03h2FP.webp'),(2741,'SpideyHomecoming (1)',589,'images/SpideyHomecoming_1_1c90sjL.jpg'),(2742,'how-to-make-a-movie_',589,'images/how-to-make-a-movie_P1_900x420_Ofo2QlI.avif'),(2743,'batman',589,'images/batman_j2KYSGo.png'),(2744,'interstallarbanner',NULL,'images/interstallarbanner_4CkagER.jpg'),(2745,'cinema-background-co',590,'images/cinema-background-concept-movie-theater-object-on-red-curtain-background-and-movi_UTPTnj0.jpg'),(2746,'arrival_vertical',590,'images/arrival_vertical_t01Sa8s.jpeg'),(2747,'movie-series-1652898',590,'images/movie-series-1652898795_O2tTF7E.jpg'),(2748,'hall_banner3',NULL,'images/hall_banner3_bIeRdwS.jpg'),(2749,'suputnik_logo',591,'images/suputnik_logo_WHqFmu1.png'),(2750,'challengers-movie-me',591,'images/challengers-movie-metro-goldwyn-mayer-ftr_qKKqcBr.webp'),(2751,'multi_gallery',591,'images/multi_gallery.avif'),(2752,'images (4)',NULL,'images/images_4_Zh32yla.jpeg'),(2753,'.DS_Store',592,'images/.DS_Store_f8bFwV3'),(2754,'Kalki--705x750-5c0e8',592,'images/Kalki--705x750-5c0e8f80-2f97-11ef-99b5-d35223c98590_60O4p8r.avif'),(2755,'Interstellar-Poster',592,'images/Interstellar-Poster_I5jtpaG.jpg'),(2756,'images',NULL,'images/images_xVc4zcV.jpeg'),(2757,'godzilla',593,'images/godzilla_WD8hIZN.jpeg'),(2758,'prom',593,'images/prom_2kILV3O.jpeg'),(2759,'godzilla benner',593,'images/godzilla_benner_KoSqwVA.png'),(2760,'movies-in-2019',NULL,'images/movies-in-2019_oSuUVZs.webp'),(2761,'spider poster',NULL,'images/spider_poster_5sWgLA2.jpeg'),(2762,'images (1)',594,'images/images_1_iM9Ps1s.jpeg'),(2763,'kinoman-banner',594,'images/kinoman-banner.jpg'),(2764,'hall_gallery',594,'images/hall_gallery_ey2ytGX.webp'),(2765,'fall_guy_poster',NULL,'images/fall_guy_poster_eu0og7u.jpeg'),(2766,'images (3)',NULL,'images/images_3_L62Pzuf.jpeg'),(2767,'ella-purnell-wildlik',595,'images/ella-purnell-wildlike-featured-1_TBcXSyd.avif'),(2768,'duna1',595,'images/duna1_EGe6zNa.jpeg'),(2769,'news baner',595,'images/news_baner_EPgG4S7.jpeg'),(2770,'realistic-webinar-te',NULL,'images/realistic-webinar-template-movie-premiere-event_23-2149496022_yRdTzqF.jpg'),(2771,'harry-potter-movies',NULL,'images/harry-potter-movies_cTWBA4G.avif'),(2772,'matrix',596,'images/matrix_UXythLT.png'),(2773,'news1_main',596,'images/news1_main.jpg'),(2774,'barbi1',596,'images/barbi1_YmpUmQc.webp'),(2775,'back_yellow',NULL,'images/back_yellow_lI6a2jZ.jpg'),(2776,'spider man 1',NULL,'images/spider_man_1_4Rt3Fr1.png'),(2777,'kinoman_logo',597,'images/kinoman_logo_qhHrUjg.png'),(2778,'suputnik3',597,'images/suputnik3_6Vka3F7.jpg'),(2779,'harry-potter-movies-',597,'images/harry-potter-movies-in-order-1-1677691321964_mpJH3rQ.jpg'),(2780,'suputnik2',NULL,'images/suputnik2_HWNZsEx.jpg'),(2781,'multiplex_logo',NULL,'images/multiplex_logo_p0sgkVB.png'),(2782,'island_di',598,'images/island_di_tSwm37o.jpeg'),(2783,'marvels-spiderman-2-',598,'images/marvels-spiderman-2-banner-e1690742326962_0VrCyZL.jpg'),(2784,'suputnik1',598,'images/suputnik1_BkufYv7.jpg'),(2785,'duna',NULL,'images/duna_gccN0Ha.jpeg'),(2786,'prom_banner',NULL,'images/prom_banner_x4f67Yq.png'),(2787,'logo',599,'images/logo_T3etgTU.png'),(2788,'deadpoolandwolverine',599,'images/deadpoolandwolverine_lob_crd_03_BTyRbAh.jpg'),(2789,'the_fall_guy',599,'images/the_fall_guy_Iw31aLw.webp'),(2790,'logan_584x800_9a5af3',NULL,'images/logan_584x800_9a5af33a_aEQpv2n.jpeg'),(2791,'duna3',600,'images/duna3_gsXRQ3l.jpeg'),(2792,'hall_gallery1',600,'images/hall_gallery1_i56G1w2.jpg'),(2793,'inerbanner',600,'images/inerbanner_MIDKrYM.webp'),(2794,'NgKvu8G2coskQXj74MoK',NULL,'images/NgKvu8G2coskQXj74MoKcE_Vh7bc8a.jpg'),(2795,'Copy-of-800-x-500-Bl',601,'images/Copy-of-800-x-500-Blog-Post-13_UOuT24Q.jpg'),(2796,'hall_gallery3',601,'images/hall_gallery3_rhkbwK7.jpg'),(2797,'kinoman1',601,'images/kinoman1_ftmePUd.jpg'),(2798,'cinema people',NULL,'images/cinema_people_wLcVOAs.jpeg'),(2799,'barbi3',602,'images/barbi3_myhbAFV.png'),(2800,'inter',602,'images/inter_ntWKvYw.jpeg'),(2801,'barbi2',602,'images/barbi2_a08mKnE.jpg'),(2802,'news',NULL,'images/news_OmWQQaa.jpeg'),(2803,'godzilla1',603,'images/godzilla1_XGwXCko.jpeg'),(2804,'cinema_banner',603,'images/cinema_banner_K5DTQaJ.jpeg'),(2805,'harry-potter',603,'images/harry-potter_3GTVkKU.webp'),(2806,'spider2',NULL,'images/spider2_6lVmUCw.jpg'),(2807,'sputnik',604,'images/sputnik_MhR9OEh.jpeg'),(2808,'intro-1637362771',604,'images/intro-1637362771_OEbdp6f.webp'),(2809,'MV5BZDdlNTIwNjYtNzVh',604,'images/MV5BZDdlNTIwNjYtNzVhNS00MGVmLTk1ZGYtZmZiMjhiMmQ1ZjkwXkEyXkFqcGdeQXVyMTY3ODkyNDkz._wCb4GGA.jpg'),(2810,'Interstellar_2014',NULL,'images/Interstellar_2014_jIIO180.jpg'),(2811,'e997ec64-07d1-45e6-a',NULL,'images/e997ec64-07d1-45e6-a9ae-ec644adbdbe8-theboys_0iBrok3.jpg'),(2812,'hall_banner',NULL,'images/hall_banner_LPYlsGg.webp'),(2813,'multi',NULL,'images/multi_3rD9Kzf.jpeg'),(2814,'MV5BNmQ0ODBhMjUtNDRh',NULL,'images/MV5BNmQ0ODBhMjUtNDRhOC00MGQzLTk5MTAtZDliODg5NmU5MjZhXkEyXkFqcGdeQXVyNDUyOTg3Njg.__nVT3uI9.jpg'),(2815,'gall_guy',NULL,'images/gall_guy_hRei3hZ.jpeg'),(2816,'hall_schema1',NULL,'images/hall_schema1_7DtRN73.png'),(2817,'barbi',NULL,'images/barbi_kkMlNDu.jpeg'),(2818,'thenewsminute_2024-0',NULL,'images/thenewsminute_2024-02_86a005d0-9e21-44bb-afc2-629758fd6e08_Razakar_movie_poster__RgFxHxS.avif'),(2819,'kinoman',NULL,'images/kinoman_zsJ3xou.jpeg'),(2820,'hall_schema3',NULL,'images/hall_schema3_hW0C7w9.png'),(2821,'movie-trivia',NULL,'images/movie-trivia_R5PzTcW.jpg'),(2822,'inter_poster',NULL,'images/inter_poster_FeSber1.png'),(2823,'inter_poster',NULL,'images/inter_poster_3uFWbcn.jpg'),(2824,'hall_schema2',NULL,'images/hall_schema2_uVqyEny.png'),(2825,'duna',NULL,'images/duna_56Pwoz6.jpg'),(2826,'barbi1',583,'images/barbi1_EeQa4Do_ep2S44a.webp'),(2827,'barbi3',583,'images/barbi3_qTn2IWt_eP9Fst9.png'),(2828,'barbi2',583,'images/barbi2_m78i8nb.jpg'),(2829,'challengers-movie-me',NULL,'images/challengers-movie-metro-goldwyn-mayer-ftr_MIo5lCO.webp'),(2830,'arrival_vertical',NULL,'images/arrival_vertical_VbCjJ3P.jpeg'),(2831,'arrival_vertical',NULL,'images/arrival_vertical_z3DVgFI.jpeg'),(2832,'duna1',585,'images/duna1_wwctbPo_CSskLbs.jpeg'),(2833,'duna3',585,'images/duna3_8q6IZEL_uhpfiAI.jpeg'),(2834,'duna',585,'images/duna_p5upqsl_4vceUqZ.jpg');
/*!40000 ALTER TABLE `core_galleryimage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_seomixin`
--

DROP TABLE IF EXISTS `core_seomixin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_seomixin` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `url_seo` varchar(200) NOT NULL,
  `title_seo` varchar(20) NOT NULL,
  `keywords_seo` varchar(20) NOT NULL,
  `description_seo` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=603 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_seomixin`
--

LOCK TABLES `core_seomixin` WRITE;
/*!40000 ALTER TABLE `core_seomixin` DISABLE KEYS */;
INSERT INTO `core_seomixin` VALUES (1,'','','',''),(542,'https://www.youtube.com/watch?v=K9cibjqbcBQ','Барбі','барбі, лялька, кен','У Барбіленді, матріархальному суспільстві з різними Барбі, Кенами та вигнанцями, Кен прагне тіснішого зв\'язку з Барбі, яка зосереджена на своїй кар\'єрі. Коли Барбі стикається з екзистенційною кризою, вона розуміє, що для зцілення їй необхідно знайти свого реального власника. Кен приєднується до неї, і їхня подорож приводить їх до Саші, дівчини, яка критично ставиться до стандартів краси Барбі.'),(543,'https://www.youtube.com/watch?v=I9fucTH5xWw','Інтерстеллар','космос, любов, плане','У далекому майбутньому Земля виявляється занадто виснажена та змучена різними катаклізмами. Вона вже майже непридатна для життя і людство шукає новий будинок для продовження свого існування. Фільм «Інтерстеллар» - це історія про групу мандрівників крізь просторово-часові тунелі, які виконують важливу місію для Землі та її мешканців. На створення фільму режисера було натхнено теоріями астрофізика Каліфорнійського технологічного інституту Кіпа Торна. Теорія ця цікава тим, що дозволяє можливість подорожей у просторі, а й у часі. Крім того, Нолан згадував, що картина «Інтерстеллар» стане своєрідним триб\'ютом фільмам Стенлі Кубріка. Сюжет картини, незважаючи на те, що він розроблявся, починаючи з 2006 року, тривалий час тримався у найсуворішій таємниці.'),(544,'https://www.youtube.com/watch?v=Ljzu52GMytk','Дюна','планета, пісок','\"Дюна\" розповідає міфічну й емоційну історію про юного аристократа Пола Атрейдеса (Тімоті Шаламе), блискучу й обдаровану молоду людину, народжену для великих звершень. Пол має вирушити на Арракіс - найнебезпечнішу планету у всесвіті, щоб забезпечити майбутнє своєї сім\'ї та свого народу. На Арракісі видобувають унікальну речовину - \"спеції\", або спайс, або меланж, що допомагає вести космічні кораблі крізь простір без допомоги комп\'ютерів, які перебувають у світі \"Дюни\" під забороною після повстання машин. Сім\'я Атрейдісів отримує планету в управління за наказом імператора, але незабаром майже вся вона гине внаслідок нападу військ сім\'ї Харконненів. Полу і його матері (Ребекка Фергюсон) вдається сховатися в пустелі, де він стає членом спільноти людей пустелі - фременів. Фремени розуміють, що юнак - Обраний з їхніх легенд, Муад`Діб, і підтримують Пола в боротьбі проти дому Гарконненів та імперії. Доки злісні сили вступають у конфлікт через постачання з планети найціннішого з наявних ресурсів - товару, здатного розкрити найбільший потенціал людства, - виживуть лише ті, хто зможе перемогти власний страх.'),(545,'https://www.youtube.com/watch?v=-3K6REi8TkI','Людина-Павук','людина, павук, марве','Весь світ дізнався, що під маскою Людини-павука ховається звичайний підліток Пітер Паркер. З цього моменту він остаточно позбавляється спокою та нормального життя. Щоб усе виправити, Пітер звертається за допомогою до Доктора Стренджа та його магії. Але потужне заклинання доктора порушує стабільність просторово-часового континууму, і кілька альтернативних реальностей перетинаються в одній точці, ставлячи під загрозу весь світ..'),(547,'https://www.kino-sputnik.com.ua/cinema/','Супутник','кіно генератор','Супутник - сучасний 6-тизальний мультиплекс, що поєднує в собі все найкраще, що є сьогодні в галузі кіно в світі.\r\n\r\nНайвища якість кінопоказу в нашому кінотеатрі досягається завдяки новітньому обладнанню, з можливістю показу кіно у форматах 2D і популярному сьогодні 3D, із застосуванням спеціальних окулярів зі стереоскопічним ефектом.\r\n\r\nКінозали відрізняються високим рівнем комфорту, а також відповідають найвищим вимогам дизайну. Унікальні екрани підвищеної яскравості забезпечують кращу якість зображення. Зручні м\'які крісла з ортопедичним ефектом забезпечені підставками для попкорну та напоїв, а також в залі Альфа можна піднімати підлокітники, що особливо  зручно для закоханих парочок. Величезною перевагою є велика відстань між рядами в залах.'),(548,'https://kinoman.ua/about','кіноман','кіноман','Кінотеатр оснащений високоякісним устаткуванням: звуковою системою JBL, цифровими проекторами BARCO та CHRISTIE, процесорами Dolby. Спеціальне акустичне покриття дозволяє максимально передати звукові спецефекти новітніх блокбастерів, це звук, який пронизує все тіло.'),(549,'http://brown-ali.com/','Prepare explain.','Risk career ability.','Kid official year resource short draw. Republican kid model get until.'),(550,'https://www.kino-sputnik.com.ua/cinema/','Зал Альфв','Зал, комфорт','В залі Альфа можна піднімати підлокітники, що особливо  зручно для закоханих парочок. Величезною перевагою є велика відстань між рядами в залах.'),(551,'https://kinoman.ua/about','Віп','віп зал','Справжні кіномани неодмінно оцінять наші VIP-зали, які обладнані зручними і м’якими кріслами-реклайнерами. Вони розкладаються, як крісла в салоні першого класу авіалайнера, – так само можна не лише сидіти, але й лежати.'),(552,'https://daugherty-bryant.info/','Will bring mission.','Fill drop hundred.','All couple picture nor less without. Economic less enough simply or.\r\nSuccessful little mother report.'),(553,'https://www.google.com/','Акція','акція квиток','Акція: 2 квитки за ціною одного!\r\n\r\nЗапрошуємо вас скористатися неймовірною пропозицією у нашому кінотеатрі! Тільки зараз у вас є унікальна можливість придбати два квитки за ціною одного. Відвідайте найкращі фільми разом з другом, родичем або коханою людиною і насолоджуйтеся кінопоказами за половину ціни!\r\n\r\nУмови акції:\r\n\r\n	•	Пропозиція діє на всі сеанси в будні дні.\r\n	•	Акція розповсюджується на всі доступні місця в залі.\r\n	•	Придбайте квитки онлайн або в касі кінотеатру.\r\n	•	Один квиток даруємо вам у подарунок при покупці одного за стандартною ціною.\r\n\r\nНе пропустіть свій шанс! Приходьте до нашого кінотеатру та отримайте подвійне задоволення від перегляду улюблених фільмів разом із близькими. Акція діє обмежений час, тож поспішайте забронювати свої квитки вже сьогодні!\r\n\r\nБронюйте зараз і побачте більше за меншу ціну!'),(554,'http://anthony.com/','новина','новина кіно','Наш кінотеатр з радістю повідомляє про відкриття нового сезону прем’єр! Цієї осені на вас чекає цілий калейдоскоп захоплюючих фільмів, які подарують незабутні враження та емоції. Ми підготували для вас найсвіжіші блокбастери, інтригуючі трилери, зворушливі драми та веселі комедії.\r\n\r\nЩо нового:\r\n\r\n	•	Світові прем’єри: Ми перші показуємо найочікуваніші фільми сезону. Відкрийте для себе нові історії разом з нашими героями на великому екрані.\r\n	•	Спеціальні покази: На вас чекають тематичні вечори з ретроспективами культових стрічок та ексклюзивні покази авторських фільмів.\r\n	•	Дитячі сеанси: Маленьким глядачам ми приготували улюблені анімації та веселі пригоди на великому екрані.'),(556,'https://butler-moon.info/','Campaign write.','Hair television.','Кафе в нашому кінотеатрі: смачно і зручно\r\n\r\nЗапрошуємо вас завітати до нашого затишного кафе, яке розташоване прямо в кінотеатрі. Тут ви зможете насолодитися ароматною кавою, свіжою випічкою та смачними снеками перед сеансом або під час перерви. Ми пропонуємо різноманітні напої, легкі закуски, попкорн та солодощі, щоб зробити ваш кіноперегляд ще приємнішим.\r\n\r\nПриходьте до нас, щоб смачно підкріпитися і налаштуватися на захоплюючий фільм!'),(558,'https://www.banks.com/','Detail break east.','Never carry someone.','Product keep minute against. Determine use head fear population. Behavior role debate agreement could.'),(581,'https://www.youtube.com/watch?v=pBk4NYhWNMM&ab_channel=WarnerBros.Pictures','berb','bdbrr','berbr'),(583,'https://www.youtube.com/watch?v=zSWdZVtXT7E&ab_channel=WarnerBros.UK%26Ireland','basm','vek','knoj');
/*!40000 ALTER TABLE `core_seomixin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_users_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=142 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (131,'admin_pages','contacts'),(129,'admin_pages','mainpage'),(130,'admin_pages','page'),(120,'auth','group'),(119,'auth','permission'),(132,'banners','backgroundbanner'),(135,'banners','bannerimage'),(133,'banners','mainpagebanners'),(134,'banners','mainpagenewsbanners'),(124,'cinemas','cinema'),(125,'cinemas','hall'),(121,'contenttypes','contenttype'),(126,'core','gallery'),(128,'core','galleryimage'),(127,'core','seomixin'),(136,'movies','movie'),(138,'newsletter','emailcampaign'),(137,'newsletter','emailtemplate'),(139,'promotion','post'),(122,'sessions','session'),(140,'showtimes','showtime'),(141,'showtimes','ticket'),(123,'users','user');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=99 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-07-30 20:37:13.206122'),(2,'contenttypes','0002_remove_content_type_name','2024-07-30 20:37:13.220947'),(3,'auth','0001_initial','2024-07-30 20:37:13.266689'),(4,'auth','0002_alter_permission_name_max_length','2024-07-30 20:37:13.279018'),(5,'auth','0003_alter_user_email_max_length','2024-07-30 20:37:13.282067'),(6,'auth','0004_alter_user_username_opts','2024-07-30 20:37:13.284636'),(7,'auth','0005_alter_user_last_login_null','2024-07-30 20:37:13.286880'),(8,'auth','0006_require_contenttypes_0002','2024-07-30 20:37:13.287336'),(9,'auth','0007_alter_validators_add_error_messages','2024-07-30 20:37:13.289715'),(10,'auth','0008_alter_user_username_max_length','2024-07-30 20:37:13.291891'),(11,'auth','0009_alter_user_last_name_max_length','2024-07-30 20:37:13.294911'),(12,'auth','0010_alter_group_name_max_length','2024-07-30 20:37:13.300464'),(13,'auth','0011_update_proxy_permissions','2024-07-30 20:37:13.303602'),(14,'auth','0012_alter_user_first_name_max_length','2024-07-30 20:37:13.305879'),(15,'users','0001_initial','2024-07-30 20:37:13.366137'),(16,'admin','0001_initial','2024-07-30 20:37:13.396300'),(17,'admin','0002_logentry_remove_auto_add','2024-07-30 20:37:13.399399'),(18,'admin','0003_logentry_add_action_flag_choices','2024-07-30 20:37:13.402161'),(19,'core','0001_initial','2024-07-30 20:37:13.436531'),(20,'core','0002_remove_galleryimage_picture','2024-07-30 20:37:13.440377'),(21,'core','0003_rename_url_galleryimage_image','2024-07-30 20:37:13.444197'),(22,'core','0004_rename_image_galleryimage_image_url','2024-07-30 20:37:13.448030'),(23,'core','0005_galleryimage_image_alter_galleryimage_gallery_and_more','2024-07-30 20:37:13.478847'),(24,'core','0006_remove_galleryimage_image_url','2024-07-30 20:37:13.482517'),(25,'admin_pages','0001_initial','2024-07-30 20:37:13.529750'),(26,'admin_pages','0002_contacts','2024-07-30 20:37:13.545484'),(27,'banners','0001_initial','2024-07-30 20:37:13.562624'),(28,'banners','0002_mainpagebanners_mainpagenewsbanners_and_more','2024-07-30 20:37:13.593330'),(29,'banners','0003_mainpagebanners_status_mainpagenewsbanners_status','2024-07-30 20:37:13.606217'),(30,'banners','0004_backgroundbanner_background_color_and_more','2024-07-30 20:37:13.620589'),(31,'banners','0005_alter_backgroundbanner_back','2024-07-30 20:37:13.623147'),(32,'cinemas','0001_initial','2024-07-30 20:37:13.716884'),(33,'cinemas','0002_remove_hall_type','2024-07-30 20:37:13.723569'),(34,'cinemas','0003_hall_cinema_hall','2024-07-30 20:37:13.736793'),(35,'cinemas','0004_rename_schema_hall_schema_json','2024-07-30 20:37:13.745427'),(39,'newsletter','0001_initial','2024-07-30 20:37:13.940977'),(40,'promotion','0001_initial','2024-07-30 20:37:13.972700'),(41,'promotion','0002_post_delete_newspromotion','2024-07-30 20:37:14.009242'),(42,'promotion','0003_remove_post_created_at_post_published_date','2024-07-30 20:37:14.027376'),(43,'sessions','0001_initial','2024-07-30 20:37:14.034492'),(45,'users','0002_alter_user_gender_alter_user_language','2024-07-30 20:37:14.082350'),(46,'admin_pages','0003_contacts_seo','2024-07-31 12:24:21.212079'),(47,'users','0003_alter_user_is_active_alter_user_is_staff','2024-08-04 16:03:23.242082'),(48,'users','0004_remove_user_role','2024-08-04 18:00:02.744989'),(49,'users','0005_alter_user_phone','2024-08-06 12:31:13.557493'),(50,'newsletter','0002_rename_email_campaign_id_useremailcampaign_email_campaign_and_more','2024-08-07 17:28:16.303604'),(51,'newsletter','0003_emailcampaign_send_to_all_emailcampaign_users_and_more','2024-08-15 12:07:01.391175'),(52,'newsletter','0004_remove_emailcampaign_users_and_more','2024-08-16 10:37:49.177347'),(53,'newsletter','0005_remove_emailcampaign_created_at_and_more','2024-08-16 14:46:03.473191'),(54,'newsletter','0006_emailcampaign_created_at_alter_emailcampaign_name_and_more','2024-08-16 14:50:22.963543'),(55,'cinemas','0005_cinema_slug_hall_slug','2024-08-22 12:55:48.926785'),(57,'promotion','0004_post_slug','2024-08-22 12:55:48.965251'),(59,'admin_pages','0004_page_slug','2024-08-22 16:13:21.140795'),(60,'banners','0006_mainpagebanners_url_mainpagenewsbanners_url','2024-08-22 18:04:30.911726'),(63,'banners','0007_remove_mainpagebanners_gallery_and_more','2024-08-26 11:28:46.737587'),(64,'banners','0008_remove_bannerimage_alt_text','2024-08-26 14:54:23.779092'),(65,'admin_pages','0005_page_description_en_page_description_uk_page_name_en_and_more','2024-09-09 12:51:40.747514'),(66,'cinemas','0006_cinema_name_en_cinema_name_uk_cinema_title_en_and_more','2024-09-09 12:51:40.916125'),(68,'promotion','0005_post_description_en_post_description_uk_post_name_en_and_more','2024-09-09 20:43:50.846920'),(69,'admin_pages','0006_rename_description_uk_page_description_ua_and_more','2024-09-10 08:41:01.809271'),(70,'cinemas','0007_rename_name_uk_cinema_name_ua_and_more','2024-09-10 08:41:01.865924'),(72,'promotion','0006_rename_description_uk_post_description_ua_and_more','2024-09-10 08:41:01.907955'),(73,'admin_pages','0007_rename_description_ua_page_description_uk_and_more','2024-09-10 08:42:16.152908'),(74,'cinemas','0008_rename_name_ua_cinema_name_uk_and_more','2024-09-10 08:42:16.211781'),(76,'promotion','0007_rename_description_ua_post_description_uk_and_more','2024-09-10 08:42:16.254213'),(81,'movies','0001_initial','2024-09-11 09:59:03.993913'),(82,'movies','0002_movie_type','2024-09-11 09:59:04.010198'),(83,'movies','0003_rename_title_movie_description_remove_movie_age_and_more','2024-09-11 09:59:04.125146'),(84,'movies','0004_movie_slug','2024-09-11 09:59:04.141904'),(85,'movies','0005_movie_description_en_movie_description_uk_and_more','2024-09-11 09:59:04.201817'),(86,'movies','0006_rename_description_uk_movie_description_ua_and_more','2024-09-11 09:59:04.240354'),(87,'movies','0007_rename_description_ua_movie_description_uk_and_more','2024-09-11 09:59:04.263182'),(88,'movies','0008_alter_movie_name_alter_movie_name_en_and_more','2024-09-11 09:59:04.303716'),(89,'movies','0009_remove_movie_description_en_and_more','2024-09-11 09:59:04.342078'),(90,'movies','0010_movie_description_en_movie_description_uk_and_more','2024-09-11 09:59:04.379268'),(91,'movies','0011_alter_movie_gallery','2024-09-11 09:59:04.410453'),(92,'showtimes','0001_initial','2024-09-11 09:59:04.459086'),(93,'showtimes','0002_showtime_movie_type','2024-09-11 09:59:04.470381'),(94,'showtimes','0003_remove_ticket_price_showtime_price','2024-09-11 09:59:04.487184'),(95,'showtimes','0004_ticket_user','2024-09-11 09:59:04.505596'),(96,'admin_pages','0008_alter_page_gallery','2024-09-11 16:03:25.665872'),(97,'cinemas','0009_rename_title_cinema_description_and_more','2024-09-11 16:03:25.820931'),(98,'promotion','0008_alter_post_gallery','2024-09-11 16:03:25.862865');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('gqkib1hl1ig5o9hdt459gkscb5nry6vo','.eJxVjEEOwiAQRe_C2hCgMDgu3fcMZBhAqoYmpV0Z765NutDtf-_9lwi0rTVsPS9hSuIitB3E6XeNxI_cdpTu1G6z5LmtyxTlrsiDdjnOKT-vh_t3UKnXb82JMljLyhgsYMlrMIyFvfPprFUBcIaHWBSCY61AIYIiYM4anEMv3h8j3TeF:1sqqIr:SNiVxrwO3XLkEC8ygON7zRFGWUVGknE-lA96ho1_Avo','2024-10-02 08:44:49.557708'),('t7tydvzvxkedazrwmm8rsy7sglg6v83v','.eJxVjEEOwiAQRe_C2hCgMDgu3fcMZBhAqoYmpV0Z765NutDtf-_9lwi0rTVsPS9hSuIitB3E6XeNxI_cdpTu1G6z5LmtyxTlrsiDdjnOKT-vh_t3UKnXb82JMljLyhgsYMlrMIyFvfPprFUBcIaHWBSCY61AIYIiYM4anEMv3h8j3TeF:1so707:dKzr8YHMYnqBYSz3xR_DA4vAqEEItrlMV8lUk_YD-NQ','2024-09-24 19:58:11.207860');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movies_movie`
--

DROP TABLE IF EXISTS `movies_movie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movies_movie` (
  `seomixin_ptr_id` bigint NOT NULL,
  `name` varchar(20) NOT NULL,
  `description` longtext NOT NULL,
  `trailer` varchar(200) NOT NULL,
  `gallery_id` bigint DEFAULT NULL,
  `main_image_id` bigint DEFAULT NULL,
  `type` varchar(10) NOT NULL,
  `slug` varchar(255) NOT NULL,
  `description_en` longtext,
  `description_uk` longtext,
  `name_en` varchar(20) DEFAULT NULL,
  `name_uk` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`seomixin_ptr_id`),
  UNIQUE KEY `slug` (`slug`),
  UNIQUE KEY `main_image_id` (`main_image_id`),
  KEY `movies_movie_gallery_id_cdedf093_fk_core_gallery_id` (`gallery_id`),
  CONSTRAINT `movies_movie_gallery_id_cdedf093_fk_core_gallery_id` FOREIGN KEY (`gallery_id`) REFERENCES `core_gallery` (`id`),
  CONSTRAINT `movies_movie_main_image_id_5e05bc27_fk_core_galleryimage_id` FOREIGN KEY (`main_image_id`) REFERENCES `core_galleryimage` (`id`),
  CONSTRAINT `movies_movie_seomixin_ptr_id_248fd5a5_fk_core_seomixin_id` FOREIGN KEY (`seomixin_ptr_id`) REFERENCES `core_seomixin` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movies_movie`
--

LOCK TABLES `movies_movie` WRITE;
/*!40000 ALTER TABLE `movies_movie` DISABLE KEYS */;
INSERT INTO `movies_movie` VALUES (581,'Barbi','Barbie embarks on a journey with Ken to discover the real world.','https://www.youtube.com/watch?v=pBk4NYhWNMM&t=3s&ab_channel=WarnerBros.Pictures',583,2647,'IMAX','barbi','Barbie embarks on a journey with Ken to discover the real world.','Барбі вирушає у подорож із Кеном, щоб відкрити справжній світ.','Barbi','Барбі'),(583,'Duna','The main character, the future heir of a renowned house, sets off on a long and unknown journey with his family. Upon arriving at their destination, an unexpected, mysterious, and sometimes terrifying and dangerous event occurs, forcing the young man to continue this newly begun adventure on his own. Whether the hero will succeed, and most importantly, escape this trap in time, only time will tell.','https://www.youtube.com/watch?v=n_L2cmZtZxw&ab_channel=planetakino',585,2688,'IMAX','duna','The main character, the future heir of a renowned house, sets off on a long and unknown journey with his family. Upon arriving at their destination, an unexpected, mysterious, and sometimes terrifying and dangerous event occurs, forcing the young man to continue this newly begun adventure on his own. Whether the hero will succeed, and most importantly, escape this trap in time, only time will tell.','Головний герой, майбутній спадкоємець відомого дому, разом із сім’єю вирушає у далеку незвідану подорож. Прибувши на місце призначення, за несподіваних обставин відбувається загадкова, часом страшна і небезпечна подія, котра змушує хлопця самотужки продовжувати цю нещодавно розпочату пригоду. Чи вдасться герою успішно, а головне вчасно вибратись із цієї пастки, покаже лише час.','Duna','Дюна');
/*!40000 ALTER TABLE `movies_movie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `newsletter_emailcampaign`
--

DROP TABLE IF EXISTS `newsletter_emailcampaign`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `newsletter_emailcampaign` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `email_template_id` bigint NOT NULL,
  `status` varchar(30) NOT NULL,
  `send_to_all` tinyint(1) NOT NULL,
  `selected_users_ids` json DEFAULT NULL,
  `progress` int NOT NULL,
  `sent_count` int NOT NULL,
  `created_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `newsletter_emailcamp_email_template_id_933e5deb_fk_newslette` (`email_template_id`),
  CONSTRAINT `newsletter_emailcamp_email_template_id_933e5deb_fk_newslette` FOREIGN KEY (`email_template_id`) REFERENCES `newsletter_emailtemplate` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=76 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `newsletter_emailcampaign`
--

LOCK TABLES `newsletter_emailcampaign` WRITE;
/*!40000 ALTER TABLE `newsletter_emailcampaign` DISABLE KEYS */;
/*!40000 ALTER TABLE `newsletter_emailcampaign` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `newsletter_emailtemplate`
--

DROP TABLE IF EXISTS `newsletter_emailtemplate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `newsletter_emailtemplate` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `description` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `newsletter_emailtemplate`
--

LOCK TABLES `newsletter_emailtemplate` WRITE;
/*!40000 ALTER TABLE `newsletter_emailtemplate` DISABLE KEYS */;
/*!40000 ALTER TABLE `newsletter_emailtemplate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `promotion_post`
--

DROP TABLE IF EXISTS `promotion_post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `promotion_post` (
  `seomixin_ptr_id` bigint NOT NULL,
  `name` varchar(40) NOT NULL,
  `description` longtext NOT NULL,
  `status` tinyint(1) NOT NULL,
  `link` varchar(200) NOT NULL,
  `type` varchar(4) NOT NULL,
  `gallery_id` bigint DEFAULT NULL,
  `main_image_id` bigint DEFAULT NULL,
  `published_date` date NOT NULL,
  `slug` varchar(255) NOT NULL,
  `description_en` longtext,
  `description_uk` longtext,
  `name_en` varchar(40) DEFAULT NULL,
  `name_uk` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`seomixin_ptr_id`),
  UNIQUE KEY `slug` (`slug`),
  UNIQUE KEY `main_image_id` (`main_image_id`),
  KEY `promotion_post_gallery_id_92e67878_fk_core_gallery_id` (`gallery_id`),
  CONSTRAINT `promotion_post_gallery_id_92e67878_fk_core_gallery_id` FOREIGN KEY (`gallery_id`) REFERENCES `core_gallery` (`id`),
  CONSTRAINT `promotion_post_main_image_id_38055fd4_fk_core_galleryimage_id` FOREIGN KEY (`main_image_id`) REFERENCES `core_galleryimage` (`id`),
  CONSTRAINT `promotion_post_seomixin_ptr_id_3a108cbc_fk_core_seomixin_id` FOREIGN KEY (`seomixin_ptr_id`) REFERENCES `core_seomixin` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `promotion_post`
--

LOCK TABLES `promotion_post` WRITE;
/*!40000 ALTER TABLE `promotion_post` DISABLE KEYS */;
INSERT INTO `promotion_post` VALUES (553,'2 квитка за ціною одного','Акція: 2 квитки за ціною одного!\r\n\r\nЗапрошуємо вас скористатися неймовірною пропозицією у нашому кінотеатрі! Тільки зараз у вас є унікальна можливість придбати два квитки за ціною одного. Відвідайте найкращі фільми разом з другом, родичем або коханою людиною і насолоджуйтеся кінопоказами за половину ціни!\r\n\r\nУмови акції:\r\n\r\n	•	Пропозиція діє на всі сеанси в будні дні.\r\n	•	Акція розповсюджується на всі доступні місця в залі.\r\n	•	Придбайте квитки онлайн або в касі кінотеатру.\r\n	•	Один квиток даруємо вам у подарунок при покупці одного за стандартною ціною.\r\n\r\nНе пропустіть свій шанс! Приходьте до нашого кінотеатру та отримайте подвійне задоволення від перегляду улюблених фільмів разом із близькими. Акція діє обмежений час, тож поспішайте забронювати свої квитки вже сьогодні!\r\n\r\nБронюйте зараз і побачте більше за меншу ціну!',1,'https://www.google.com/','prom',560,2616,'2024-09-13','2','Promotion: 2 tickets for the price of 1!\r\n\r\nWe invite you to take advantage of an incredible offer at our cinema! Right now, you have a unique opportunity to buy two tickets for the price of one. Enjoy the best movies with a friend, relative, or loved one and experience screenings at half the price!\r\n\r\nPromotion conditions:\r\n\r\n• The offer is valid for all weekday showings.\r\n• The promotion applies to all available seats in the hall.\r\n• Purchase tickets online or at the cinema box office.\r\n• One ticket is free when you purchase one at the standard price.\r\n\r\nDon\'t miss your chance! Come to our cinema and get double the enjoyment of your favorite films with your loved ones. The promotion is available for a limited time, so hurry and book your tickets today!\r\n\r\nBook now and see more for less!','Акція: 2 квитки за ціною одного!\r\n\r\nЗапрошуємо вас скористатися неймовірною пропозицією у нашому кінотеатрі! Тільки зараз у вас є унікальна можливість придбати два квитки за ціною одного. Відвідайте найкращі фільми разом з другом, родичем або коханою людиною і насолоджуйтеся кінопоказами за половину ціни!\r\n\r\nУмови акції:\r\n\r\n	•	Пропозиція діє на всі сеанси в будні дні.\r\n	•	Акція розповсюджується на всі доступні місця в залі.\r\n	•	Придбайте квитки онлайн або в касі кінотеатру.\r\n	•	Один квиток даруємо вам у подарунок при покупці одного за стандартною ціною.\r\n\r\nНе пропустіть свій шанс! Приходьте до нашого кінотеатру та отримайте подвійне задоволення від перегляду улюблених фільмів разом із близькими. Акція діє обмежений час, тож поспішайте забронювати свої квитки вже сьогодні!\r\n\r\nБронюйте зараз і побачте більше за меншу ціну!','2 tickets for the price of 1','2 квитка за ціною одного'),(554,'Кінотеатр відкриває новий сезон прем’єр:','Наш кінотеатр з радістю повідомляє про відкриття нового сезону прем’єр! Цієї осені на вас чекає цілий калейдоскоп захоплюючих фільмів, які подарують незабутні враження та емоції. Ми підготували для вас найсвіжіші блокбастери, інтригуючі трилери, зворушливі драми та веселі комедії.\r\n\r\nЩо нового:\r\n\r\n	•	Світові прем’єри: Ми перші показуємо найочікуваніші фільми сезону. Відкрийте для себе нові історії разом з нашими героями на великому екрані.\r\n	•	Спеціальні покази: На вас чекають тематичні вечори з ретроспективами культових стрічок та ексклюзивні покази авторських фільмів.\r\n	•	Дитячі сеанси: Маленьким глядачам ми приготували улюблені анімації та веселі пригоди на великому екрані.',1,'http://pena.com/','news',561,2630,'2024-09-14','post-554','Our cinema is delighted to announce the opening of a new season of premieres! This fall, get ready for a kaleidoscope of exciting films that will bring unforgettable experiences and emotions. We\'ve prepared the latest blockbusters, thrilling thrillers, touching dramas, and hilarious comedies for you.\r\n\r\nWhat\'s new:\r\n\r\n• World premieres: Be the first to watch the most anticipated films of the season. Discover new stories alongside our heroes on the big screen.\r\n• Special screenings: Enjoy themed evenings with retrospectives of iconic films and exclusive screenings of indie films.\r\n• Kids\' sessions: For our young viewers, we’ve prepared their favorite animations and fun adventures on the big screen.','Наш кінотеатр з радістю повідомляє про відкриття нового сезону прем’єр! Цієї осені на вас чекає цілий калейдоскоп захоплюючих фільмів, які подарують незабутні враження та емоції. Ми підготували для вас найсвіжіші блокбастери, інтригуючі трилери, зворушливі драми та веселі комедії.\r\n\r\nЩо нового:\r\n\r\n	•	Світові прем’єри: Ми перші показуємо найочікуваніші фільми сезону. Відкрийте для себе нові історії разом з нашими героями на великому екрані.\r\n	•	Спеціальні покази: На вас чекають тематичні вечори з ретроспективами культових стрічок та ексклюзивні покази авторських фільмів.\r\n	•	Дитячі сеанси: Маленьким глядачам ми приготували улюблені анімації та веселі пригоди на великому екрані.','The cinema is launching a new season of','Кінотеатр відкриває новий сезон прем’єр:');
/*!40000 ALTER TABLE `promotion_post` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `showtimes_showtime`
--

DROP TABLE IF EXISTS `showtimes_showtime`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `showtimes_showtime` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `show_time` datetime(6) NOT NULL,
  `hall_id_id` bigint NOT NULL,
  `movie_id_id` bigint NOT NULL,
  `movie_type` varchar(4) NOT NULL,
  `price` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `showtimes_showtime_hall_id_id_203bed45_fk_cinemas_h` (`hall_id_id`),
  KEY `showtimes_showtime_movie_id_id_ee9ff028_fk_movies_mo` (`movie_id_id`),
  KEY `showtimes_showtime_show_time_9e042e6e` (`show_time`),
  CONSTRAINT `showtimes_showtime_hall_id_id_203bed45_fk_cinemas_h` FOREIGN KEY (`hall_id_id`) REFERENCES `cinemas_hall` (`seomixin_ptr_id`),
  CONSTRAINT `showtimes_showtime_movie_id_id_ee9ff028_fk_movies_mo` FOREIGN KEY (`movie_id_id`) REFERENCES `movies_movie` (`seomixin_ptr_id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `showtimes_showtime`
--

LOCK TABLES `showtimes_showtime` WRITE;
/*!40000 ALTER TABLE `showtimes_showtime` DISABLE KEYS */;
INSERT INTO `showtimes_showtime` VALUES (6,'2024-09-18 18:59:28.073556',552,581,'3D',108),(7,'2024-09-13 02:40:54.760230',550,581,'IMAX',103),(9,'2024-09-23 21:10:56.396954',550,581,'3D',89),(27,'2024-09-28 04:05:46.549171',550,583,'IMAX',105),(45,'2024-10-01 19:35:36.567620',552,583,'2D',61),(50,'2024-10-01 22:07:14.599153',551,583,'3D',134),(57,'2024-09-11 23:41:18.163499',552,581,'3D',108),(67,'2024-10-03 17:11:16.060069',551,581,'3D',68),(73,'2024-09-14 18:43:30.230587',550,581,'3D',120),(78,'2024-10-10 21:40:57.346650',550,581,'2D',126),(83,'2024-09-12 09:46:05.542487',551,583,'3D',122),(87,'2024-10-10 05:28:29.664849',552,583,'IMAX',69),(88,'2024-09-18 10:06:59.387810',550,583,'3D',77);
/*!40000 ALTER TABLE `showtimes_showtime` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `showtimes_ticket`
--

DROP TABLE IF EXISTS `showtimes_ticket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `showtimes_ticket` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `row` int NOT NULL,
  `seat` int NOT NULL,
  `show_time_id_id` bigint NOT NULL,
  `user_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `showtimes_ticket_show_time_id_id_59372d70_fk_showtimes` (`show_time_id_id`),
  KEY `showtimes_ticket_user_id_1107f735_fk_users_user_id` (`user_id`),
  CONSTRAINT `showtimes_ticket_show_time_id_id_59372d70_fk_showtimes` FOREIGN KEY (`show_time_id_id`) REFERENCES `showtimes_showtime` (`id`),
  CONSTRAINT `showtimes_ticket_user_id_1107f735_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `showtimes_ticket`
--

LOCK TABLES `showtimes_ticket` WRITE;
/*!40000 ALTER TABLE `showtimes_ticket` DISABLE KEYS */;
INSERT INTO `showtimes_ticket` VALUES (1,3,1,73,143),(2,3,3,73,143),(3,3,2,88,143),(4,3,3,88,143),(5,3,4,88,143);
/*!40000 ALTER TABLE `showtimes_ticket` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_user`
--

DROP TABLE IF EXISTS `users_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `name` varchar(10) NOT NULL,
  `last_name` varchar(12) NOT NULL,
  `nickname` varchar(10) NOT NULL,
  `email` varchar(254) NOT NULL,
  `address` varchar(30) NOT NULL,
  `num_card` varchar(12) NOT NULL,
  `language` varchar(3) NOT NULL,
  `gender` varchar(1) NOT NULL,
  `phone` varchar(128) NOT NULL,
  `date_birthday` date DEFAULT NULL,
  `city` varchar(12) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nickname` (`nickname`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=149 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_user`
--

LOCK TABLES `users_user` WRITE;
/*!40000 ALTER TABLE `users_user` DISABLE KEYS */;
INSERT INTO `users_user` VALUES (138,'',NULL,0,'Lisa','Oconnor','hermantama','williamsscott@example.org','PSC 0153, Bo','180088804283','ru','M','+380502460725','1965-07-10','Львів',0,0,'2024-09-03 15:09:04.680106'),(139,'',NULL,0,'Carlos','Rios','wlopez','hjones@example.com','2623 Kevin C','352043217394','ua','F','+380638021447','2018-12-28','Київ',0,0,'2024-09-03 15:09:04.693680'),(140,'',NULL,0,'Rebecca','Roberson','robin87','higginsmichelle@example.net','83063 Shanno','303358552896','ua','F','+380638023456','1937-07-03','Київ',0,0,'2024-09-03 15:09:04.694870'),(141,'',NULL,0,'Ashley','Boone','jeffery97','thompsongina@example.org','005 James Ra','601198151673','ua','M','+15778483291','1980-03-07','Leslietown',0,1,'2024-09-03 15:09:04.696062'),(142,'',NULL,0,'Steven','Thomas','staceyhine','kenneth66@example.org','27333 Camero','354197630639','ru','F','635.852.3773x6555','1920-02-15','Kellerside',0,1,'2024-09-03 15:09:04.697225'),(143,'pbkdf2_sha256$720000$Jp58WXpmcJkGfX9mawLhmq$XbYVA9t2WuRQZ9O00LaAMRRzvvJbqiS1wG6/OziQX8E=','2024-09-18 08:44:49.555793',1,'','','','admin_kinicms@gmail.com','','','ua','','',NULL,'',1,1,'2024-09-03 15:12:00.727486'),(144,'',NULL,0,'Brian','Brooks','ljones','tiffany74@example.com','52681 Mills ','558102020854','ru','F','(486)908-6456x0369','1959-07-05','Andersonboro',0,1,'2024-09-11 15:00:09.016487'),(145,'',NULL,0,'Robert','Garcia','fernandezc','kristingonzalez@example.org','320 Thompson','558716663210','ua','F','(573)447-0110','2023-04-24','Robertsfurt',0,1,'2024-09-11 15:00:09.018097'),(146,'',NULL,0,'Angel','Cunningham','russellchr','andersonarthur@example.org','309 Vega Por','355288994821','ua','F','+16229583216','1963-10-18','Edwardsborou',0,1,'2024-09-11 15:00:09.019809'),(147,'',NULL,0,'Jillian','Myers','anthony65','gonzalezmicheal@example.com','USCGC Price\n','496999920922','ua','F','989.712.4223x34248','1969-12-12','Port Jeffrey',0,1,'2024-09-11 15:00:09.026037'),(148,'',NULL,0,'Heather','Parker','mdavis','seth54@example.org','457 Campbell','354815478235','ua','M','630.246.8804','1929-06-23','West Rodney',0,1,'2024-09-11 15:00:09.027621');
/*!40000 ALTER TABLE `users_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_user_groups`
--

DROP TABLE IF EXISTS `users_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_user_groups_user_id_group_id_b88eab82_uniq` (`user_id`,`group_id`),
  KEY `users_user_groups_group_id_9afc8d0e_fk_auth_group_id` (`group_id`),
  CONSTRAINT `users_user_groups_group_id_9afc8d0e_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `users_user_groups_user_id_5f6f5a90_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_user_groups`
--

LOCK TABLES `users_user_groups` WRITE;
/*!40000 ALTER TABLE `users_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_user_user_permissions`
--

DROP TABLE IF EXISTS `users_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_user_user_permissions_user_id_permission_id_43338c45_uniq` (`user_id`,`permission_id`),
  KEY `users_user_user_perm_permission_id_0b93982e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `users_user_user_perm_permission_id_0b93982e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `users_user_user_permissions_user_id_20aca447_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_user_user_permissions`
--

LOCK TABLES `users_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `users_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-23 21:41:50
