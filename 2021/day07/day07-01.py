#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 01:38:18 2021

@author: ricardovieira
"""

crab_pos=[1101,1,29,67,1102,0,1,65,1008,65,35,66,1005,66,28,1,67,65,20,4,0,1001,65,1,65,1106,0,8,99,35,67,101,99,105,32,110,39,101,115,116,32,112,97,115,32,117,110,101,32,105,110,116,99,111,100,101,32,112,114,111,103,114,97,109,10,1174,360,173,61,168,663,15,245,841,35,476,467,1202,235,427,399,230,649,168,1222,444,577,486,877,643,325,22,558,135,1259,917,672,1429,290,592,793,148,272,1654,187,48,120,721,833,298,752,381,45,630,252,706,270,14,132,576,326,908,331,562,207,935,348,1178,1299,33,33,463,4,230,26,289,961,77,306,910,252,1433,14,396,1013,70,18,1066,55,100,627,680,1101,135,443,307,1027,254,1298,48,248,414,416,551,596,407,516,36,39,3,853,1120,257,178,136,5,703,609,595,50,724,1260,266,108,508,287,105,21,188,529,58,429,801,641,689,300,114,1218,603,418,140,73,14,268,1029,767,0,1533,1207,8,396,106,375,602,1,1326,43,94,1097,1,158,717,183,200,36,39,585,727,43,314,468,1011,530,213,1532,242,396,780,204,107,533,1274,250,182,208,145,146,12,511,1091,337,1448,515,603,506,664,37,385,1053,212,1487,151,181,403,1386,803,564,214,93,1072,1140,79,929,798,211,355,197,1056,392,341,515,848,931,70,337,383,1520,780,621,984,1420,439,744,527,1199,65,24,44,1621,202,1468,473,1449,12,446,50,143,36,1133,4,121,62,662,590,655,714,95,203,36,214,90,494,1142,592,978,11,330,734,429,2,5,611,1676,180,11,12,399,410,882,78,177,269,20,820,1122,153,248,929,17,99,149,391,90,168,453,453,87,156,390,44,252,117,739,918,15,1172,1186,80,621,128,1384,47,76,317,55,8,517,608,48,812,156,855,542,374,266,719,276,383,560,106,307,809,900,1706,573,396,92,131,193,90,244,73,65,879,605,289,835,596,471,1277,27,732,103,210,519,623,273,153,157,571,230,341,1289,42,601,448,201,214,225,199,46,266,64,342,673,411,466,77,24,112,180,1144,8,0,415,1099,875,44,703,427,1083,521,132,1598,91,335,1163,262,520,110,465,306,61,354,1159,1251,268,151,143,691,313,5,1533,1287,536,138,75,1147,303,256,163,733,465,551,1437,232,244,64,1132,986,17,591,676,169,318,797,410,96,993,737,88,941,67,1066,543,4,10,569,74,828,296,169,949,145,31,26,274,302,782,568,803,370,76,226,1537,550,461,648,114,738,1025,0,130,1141,50,1056,1332,714,36,27,669,191,216,344,550,104,11,924,6,35,62,391,89,473,146,158,151,74,10,479,65,1,50,35,545,140,1499,109,842,31,223,328,361,15,1021,4,1726,706,89,90,29,599,103,235,10,203,727,1151,14,421,596,134,235,60,1273,2,1693,1263,399,306,928,552,1370,192,451,1478,217,527,1442,32,474,116,1631,495,250,1091,115,1408,123,897,185,1664,127,95,65,1053,677,648,99,1503,488,976,1040,628,1353,1417,190,1303,700,283,11,803,1552,555,1248,179,131,195,580,213,271,224,416,688,33,64,1690,985,214,895,977,29,31,85,177,734,686,1271,72,1012,911,730,758,243,25,1423,492,1202,9,118,14,1553,899,946,1474,352,269,65,28,90,262,137,77,364,607,700,827,716,9,56,1419,998,14,716,397,1425,114,428,838,39,1012,92,259,482,369,62,1080,243,226,1190,844,822,26,800,732,1345,1223,577,1130,120,1152,1522,166,54,19,506,105,436,1110,524,474,1351,643,377,154,473,116,492,537,208,625,47,1415,516,736,1376,772,22,645,112,989,24,1179,935,822,47,203,1432,623,375,153,758,1061,433,86,652,378,49,254,250,665,1248,228,228,616,709,960,1548,465,127,666,254,422,580,419,403,190,677,804,852,1425,638,263,710,7,354,880,1338,42,71,869,276,331,17,785,439,305,122,162,340,1236,163,1214,437,553,200,1121,513,863,253,48,1288,87,225,259,111,426,35,260,433,830,207,184,1788,952,62,647,14,687,679,14,24,693,294,1004,681,66,287,49,152,416,825,175,1307,123,470,393,850,705,10,41,209,328,185,593,148,1312,354,67,189,334,638,1509,302,248,406,1148,537,460,646,661,279,326,1581,959,442,282,48,572,104,450,242,3,703,296,177,217,119,63,354,29,550,889,729,1438,588,371,363,504,5,783,227,61,479,175,227,1331,280,116,79,420,512,46,480,1198,752,19,314,155,635,1326,121,1480,207,1579,597,1147,806,267,67,341,1460,1121,743,597,1004,0,55,1727,127,11,1001,224,31,220,269,173,32,35,818,1049,249,812,62,393,461,414,243,489,512,2,390,121,1106,594,335,665,962,134,255,44,479,1180,351,188,13,732,1116,113,671]

def cost_pos(pos):
    value = 0
    for i in range(len(crab_pos)):
        value += abs(crab_pos[i]-pos)
    return value

min_cost = cost_pos(0)
for i in range(1,len(crab_pos)):
    if cost_pos(i)<min_cost:
        min_cost=cost_pos(i)
print(min_cost)        