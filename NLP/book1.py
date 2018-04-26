from __future__ import division
from nltk.book import *
# text1.concordance("monstrous")
# print("\n--monstorus similar---\n")
# text1.similar("monstrous")


# print("\n-- similar to sense---\n")
# text2.similar("sense")

# print("\n-- common contexts---\n")
# text2.common_contexts(["sense","sister"])

#text4.dispersion_plot(["citizens","democracy","freedom","duties","America"])

# print(len(text2))
# print(set(text2))
# print(sorted(set(text2)))
# print(len(set(text2)))


pprichness = len(text2)/len(set(text2))
print(pprichness)

print(text5.count("lol"))
print(100*text5.count("lol")/len(text5))