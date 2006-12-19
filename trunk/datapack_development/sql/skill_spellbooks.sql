--
-- Table structure for table `skill_spellbooks`
--
DROP TABLE IF EXISTS skill_spellbooks;
CREATE TABLE `skill_spellbooks` (
  `skill_id` int(11) NOT NULL default '-1',
  `item_id` int(11) NOT NULL default '-1',
  KEY `skill_id` (`skill_id`,`item_id`)
) TYPE=MyISAM;

--
-- Dumping data for table `skill_spellbooks`
--

-- NOTES:
-- (0,1393),
-- Spellbook: Quickness unable to find a matching skill_id possibly never used
INSERT INTO `skill_spellbooks` VALUES 
(2,1512),
(10,3039),
(13,3940),
(15,1513),
(21,1377),
(22,3040),
(25,3038),
(33,3041),
(44,3432),
(45,1378),
(46,3042),
(49,3043),
(58,1096),
(61,1379),
(65,3044),
(67,3045),
(69,3046),
(70,1097),
(72,3047),
(77,1095),
(86,3048),
(91,1294),
(102,1380),
(103,3049),
(105,1381),
(115,1382),
(122,3050),
(123,3051),
(127,3052),
(129,1383),
(230,1384),
(262,3053),
(278,3054),
(279,3055),
(283,3056),
(289,4203),
(301,4921),
(1002,1518),
(1003,1519),
(1004,3103),
(1005,1520),
(1006,1521),
(1007,1522),
(1008,3104),
(1009,1523),
(1010,1524),
(1011,1152),
(1012,1053),
(1013,1385),
(1015,1050),
(1016,1514),
(1018,3072),
(1020,3068),
(1027,1054),
(1028,3073),
(1031,1386),
(1032,3094),
(1033,1387),
(1034,3069),
(1035,1388),
(1036,3095),
(1040,1058),
(1042,3070),
(1043,1389),
(1044,1390),
(1045,3096),
(1047,4207),
(1048,3097),
(1049,3071),
(1050,3098),
(1056,3079),
(1059,1391),
(1062,1392),
(1064,3064),
(1068,1048),
(1069,1394),
(1071,3082),
(1072,3080),
(1073,1515),
(1074,3074),
(1075,1397),
(1077,1398),
(1078,1399),
(1085,1401),
(1086,3099),
(1087,1402),
(1090,1525),
(1092,1526),
(1095,1527),
(1096,1528),
(1097,1529),
(1099,1530),
(1100,1531),
(1101,1532),
(1102,1533),
(1104,3105),
(1105,1534),
(1107,1535),
(1108,3106),
(1111,1403),
(1126,1404),
(1127,1405),
(1128,1667),
(1129,3057),
(1139,3091),
(1140,3092),
(1141,3093),
(1144,1406),
(1145,1407),
(1146,1408),
(1147,1051),
(1148,3065),
(1151,1516),
(1154,3058),
(1155,3059),
(1156,3060),
(1157,1517),
(1159,3066),
(1160,1409),
(1163,3061),
(1164,1056),
(1167,1410),
(1168,1055),
(1169,3062),
(1170,3063),
(1171,3075),
(1172,1411),
(1174,3083),
(1175,1370),
(1176,3089),
(1178,1371),
(1181,1052),
(1182,1412),
(1183,3084),
(1184,1049),
(1189,1413),
(1191,1414),
(1201,1415),
(1204,1098),
(1206,1099),
(1208,1536),
(1209,1537),
(1210,3107),
(1213,3108),
(1217,3429),
(1218,3430),
(1219,3431),
(1220,1372),
(1222,1416),
(1223,1417),
(1224,1418),
(1225,1668),
(1226,1669),
(1227,1670),
(1228,1671),
(1229,1856),
(1230,3076),
(1231,3081),
(1232,3077),
(1233,3078),
(1234,3067),
(1235,3085),
(1236,3086),
(1237,3087),
(1238,3088),
(1239,3090),
(1240,3100),
(1242,3101),
(1243,3102),
(1244,3115),
(1245,3114),
(1246,3109),
(1247,3110),
(1248,3111),
(1249,3112),
(1250,3113),
(1251,3116),
(1252,3117),
(1253,3118),
(1254,3941),
(1256,3943),
(1257,3944),
(1258,4200),
(1259,4201),
(1260,4204),
(1261,4205),
(1262,4206),
(1263,4208),

/* c3 skill spellbooks (most of them anyway - thx Luno) */

(1264,4906),
(1265,4907),
(1266,4908),
(1267,4909),
(1268,4910),
(1269,4911),
(1271,4912),
(1272,4913),
(1273,4914),
(1274,4916),
(1275,4917),
(1276,4918),
(1277,4919),
(1278,4920),
(1279,4922),
(1280,4923),
(1281,4924),
(1282,4925),
(1283,4926),
(1284,4927),
(1285,4928),
(1286,4929),
(1287,4930),
(1288,4931),
(1289,4932),
(1290,4933),
(1291,4934),
(1292,5013),
(1293,5014),
(1294,5015),
(1295,5809),
(1296,5810),
(1298,5811),
(1299,5812),
(1300,5813),
(1301,5814),
(1303,5815),
(1304,5816),
(1305,6350),
(1306,6351),
(1307,6352),
(1308,6395),
(1309,6396),
(1310,6397),
(1311,6398),

/* C4 Spellbooks and Amulets */

(1328,7638),
(1329,7639),
(1330,7640),
(1331,7641),
(1332,7642),
(1333,7643),
(1334,7644),
(1335,7645),
(1336,7646),
(1337,7647),
(1338,7648),
(1339,7649),
(1340,7650),
(1341,7651),
(1342,7652),
(1343,7653),
(1344,7654),
(1345,7655),
(1346,7656),
(1347,7657),
(1348,7658),
(1349,7659),
(1350,7660),
(1351,7661),
(1352,7662),
(1353,7663),
(1354,7664),
(1355,7665),
(1356,7666),
(1357,7667),
(1358,7668),
(1359,7669),
(1360,7670),
(1361,7671),
(1362,7672),
(1363,7673),
(1364,7674),
(1365,7675),
(1366,7676),
(1367,7835);

/* C5 Spellbooks and Amulets (tnx ThePhoenixBird) */

INSERT INTO `skill_spellbooks` VALUES
(1380,8380),
(1381,8381),
(1382,8382),
(1383,8383),
(1384,8384),
(1385,8385),
(1386,8386),
(1387,8387),
(1388,8388),
(1389,8389),
(1390,8390),
(1391,8391),
(1392,8392),
(1393,8393),
(1394,8394),
(1395,8395),
(1396,8396),
(1397,8397),
(1398,8398),
(1399,8399),
(1400,8400),
(1401,8401),
(1402,8402);