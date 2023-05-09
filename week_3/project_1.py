gals = ("Samantha ", "Jada     ", "Jane     ", "Claire   ", "Elizabeth", "Mary     ", "Susan    ", "Waje     ", "Taibat   ", "Lilian   "
)
gals_age = ("17", "16", "17", "18", "16", "18", "17", "20", "19", "20")
gals_height = ("5.6", "6.0", "5.4", "5.9", "5.6", "5.5", "6.1", "6.0", "5.7", "5.5")
gals_scores = ("80", "85", "70", "60", "76", "66", "87", "95", "50", "49")

print("|", "Names      |Age |Height|Score")
for i in range(len(gals_age)):
    print("|",gals[i],  "|", gals_age[i], "|" ,gals_height[i],  "|" ,gals_scores[i], "|")
print("\n")

boys = ("Charles", "Jude   ", "James  ", "Kelvin ", "Biodun ", "wale   ", "Kunle  ", "Matthew", "Tom    ", "Kayode ")
boys_age = ("19", "16", "18", "17", "20", "19", "16", "18", "17", "19",)
boys_height = ("5.7", "5.9", "5.8", "6.1", "5.9", "5.5", "6.1", "5.4", "5.8", "5.7",)
boys_score = ("74", "87", "75", "68", "66", "78", "87", "98", "54", "60")

print("|","Names     |Age|Height|Score")
for i in range(len(boys_age)):
    print("|",boys[i],  "|", boys_age[i], "|" ,boys_height[i],  "|" ,boys_score[i], "|")


