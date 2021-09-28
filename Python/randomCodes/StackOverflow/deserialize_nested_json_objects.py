import json


class Generic:
    @classmethod
    def from_dict(cls, dict):
        obj = cls()
        obj.__dict__.update(dict)
        return obj


# data = '{"product": "name", "read_logs": {"log_type": "failure", "log_url": "123"}}'
data = r'{"content":"{\"userProfile\":{\"deviceId\":\"11b84b24a6d644a35f8e684323df0ae4\",\"userName\":\"Player123\",\"playerId\":46209000,\"deviceNotifToken\":\"N/A\",\"loginFacebook\":false,\"loginGoogle\":false},\"userStatus\":{\"userCoins\":2060,\"userEnergy\":5,\"nextEnergyTime\":\"7/24/2021 6:47:19 PM\",\"lastAddedTime\":\"7/23/2021 2:41:54 PM\",\"userBoosters\":[{\"tileValue\":9,\"amount\":0},{\"tileValue\":10,\"amount\":0},{\"tileValue\":11,\"amount\":0},{\"tileValue\":12,\"amount\":0},{\"tileValue\":13,\"amount\":0},{\"tileValue\":14,\"amount\":0},{\"tileValue\":15,\"amount\":0}]},\"userStatistics\":{\"totalSpatulas\":0,\"totalStars\":0,\"spatulaSpend\":0,\"levelsCompleted\":3,\"taskComplete\":0,\"tutorialStatus\":[false,false,false,false,false,false]},\"userSettings\":{\"language\":\"en\",\"musicLevel\":true,\"sfxLevel\":true},\"userLevels\":[{\"nameLevel\":\"Level1_Tutorial\",\"id\":1,\"leveScore\":17185,\"levelStars\":3,\"attemptsPlayed\":1,\"fullStars\":true,\"isCompleted\":true,\"isAvailable\":true,\"isBanned\":false},{\"nameLevel\":\"Level2_Tutorial\",\"id\":2,\"leveScore\":20350,\"levelStars\":3,\"attemptsPlayed\":1,\"fullStars\":true,\"isCompleted\":true,\"isAvailable\":true,\"isBanned\":false},{\"nameLevel\":\"Level3_Tutorial\",\"id\":3,\"leveScore\":29690,\"levelStars\":3,\"attemptsPlayed\":1,\"fullStars\":true,\"isCompleted\":true,\"isAvailable\":true,\"isBanned\":false},{\"nameLevel\":\"Level 3\",\"id\":4,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":true,\"isBanned\":false},{\"nameLevel\":\"Level 4\",\"id\":5,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 5\",\"id\":6,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 6\",\"id\":7,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 7\",\"id\":8,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 8\",\"id\":9,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 9\",\"id\":10,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 10\",\"id\":11,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 11\",\"id\":12,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 12\",\"id\":13,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 13\",\"id\":14,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 14\",\"id\":15,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 15\",\"id\":16,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 16\",\"id\":17,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 17\",\"id\":18,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 18\",\"id\":19,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 19\",\"id\":20,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 20\",\"id\":21,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 21\",\"id\":22,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 22\",\"id\":23,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 23\",\"id\":24,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 24\",\"id\":25,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 25\",\"id\":26,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 26\",\"id\":27,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 27\",\"id\":28,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 28\",\"id\":29,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 29\",\"id\":30,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 30\",\"id\":31,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 31\",\"id\":32,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 32\",\"id\":33,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 33\",\"id\":34,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 34\",\"id\":35,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 35\",\"id\":36,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 36\",\"id\":37,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 37\",\"id\":38,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 38\",\"id\":39,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 39\",\"id\":40,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 40\",\"id\":41,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 41\",\"id\":42,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 42\",\"id\":43,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 43\",\"id\":44,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 44\",\"id\":45,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 45\",\"id\":46,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 46\",\"id\":47,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 47\",\"id\":48,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 48\",\"id\":49,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 49\",\"id\":50,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 50\",\"id\":51,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 51\",\"id\":52,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 52\",\"id\":53,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 53\",\"id\":54,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 54\",\"id\":55,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 55\",\"id\":56,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 56\",\"id\":57,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 57\",\"id\":58,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 58\",\"id\":59,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 59\",\"id\":60,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 60\",\"id\":61,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 61\",\"id\":62,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 62\",\"id\":63,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 63\",\"id\":64,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 64\",\"id\":65,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 65\",\"id\":66,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 66\",\"id\":67,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 67\",\"id\":68,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 68\",\"id\":69,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 69\",\"id\":70,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 70\",\"id\":71,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 71\",\"id\":72,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 72\",\"id\":73,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 73\",\"id\":74,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 74\",\"id\":75,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 75\",\"id\":76,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 76\",\"id\":77,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 77\",\"id\":78,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 78\",\"id\":79,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 79\",\"id\":80,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 80\",\"id\":81,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 81\",\"id\":82,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 82\",\"id\":83,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 83\",\"id\":84,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 84\",\"id\":85,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 85\",\"id\":86,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 86\",\"id\":87,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 87\",\"id\":88,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 88\",\"id\":89,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 89\",\"id\":90,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 90\",\"id\":91,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 91\",\"id\":92,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 92\",\"id\":93,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 93\",\"id\":94,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 94\",\"id\":95,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 95\",\"id\":96,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 96\",\"id\":97,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 97\",\"id\":98,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 98\",\"id\":99,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 99\",\"id\":100,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 100\",\"id\":101,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 101\",\"id\":102,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 102\",\"id\":103,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 103\",\"id\":104,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 104\",\"id\":105,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 105\",\"id\":106,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 106\",\"id\":107,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 107\",\"id\":108,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 108\",\"id\":109,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 109\",\"id\":110,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 110\",\"id\":111,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 111\",\"id\":112,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 112\",\"id\":113,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 113\",\"id\":114,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 114\",\"id\":115,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 115\",\"id\":116,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 116\",\"id\":117,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 117\",\"id\":118,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 118\",\"id\":119,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 119\",\"id\":120,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 120\",\"id\":121,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 121\",\"id\":122,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 122\",\"id\":123,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 123\",\"id\":124,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 124\",\"id\":125,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 125\",\"id\":126,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 126\",\"id\":127,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 127\",\"id\":128,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 128\",\"id\":129,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 129\",\"id\":130,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 130\",\"id\":131,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 131\",\"id\":132,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 132\",\"id\":133,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 133\",\"id\":134,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 134\",\"id\":135,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 135\",\"id\":136,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 136\",\"id\":137,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 137\",\"id\":138,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 138\",\"id\":139,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 139\",\"id\":140,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 140\",\"id\":141,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 141\",\"id\":142,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 142\",\"id\":143,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 143\",\"id\":144,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 144\",\"id\":145,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 145\",\"id\":146,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 146\",\"id\":147,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 147\",\"id\":148,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 148\",\"id\":149,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false},{\"nameLevel\":\"Level 149\",\"id\":150,\"leveScore\":0,\"levelStars\":0,\"attemptsPlayed\":0,\"fullStars\":false,\"isCompleted\":false,\"isAvailable\":false,\"isBanned\":false}],\"userTutorial\":[],\"userID\":\"\"}"}'

x = json.loads(data, object_hook=Generic.from_dict)
# print(x.product, x.read_logs.log_type, x.read_logs.log_url)
print(x.content[0])