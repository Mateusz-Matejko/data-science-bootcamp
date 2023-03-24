# import pprint
from random import randint

# forbidden_words = []
#
# with open("reduta.txt", "r", encoding="utf-8") as txt_file:
#     res = {}
#     for line in txt_file:
#         for word in line.strip().replace("!", "").replace(",", "").replace("-","").lower().split(" "):
#             if word == "":
#                 continue
#             if word in res.keys():
#                 res[word] += 1
#             else:
#                 res[word] = 1
#     res = sorted(res.items(), key=lambda x: x[1], reverse=True)
#     pprint.pprint(res)

with open("../fileIO/lotto.txt", "w") as f:
    amount_of_games = int(input("How many games result you want? "))
    for game in range(amount_of_games):
        result_of_game = set()
        while len(result_of_game) != 6:
            result_of_game.add(randint(1, 49))
        for item in result_of_game:
            f.write(str(item) + " ")
        f.write("\n")

"""
 ******
********
"""