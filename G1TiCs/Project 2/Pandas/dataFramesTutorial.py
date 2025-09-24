import pandas as pd
import gapminder as gap
bNames =["Noah", "Liam", "Jacob", "William",
         "Mason", "Ethan", "Michael",
         "Alexander", "James", "Elijah"]

gNames = ["Emma", "Olivia", "Sophia", 
          "Isabella", "Ava", "Mia", 
          "Abigail", "Emily", "Charlotte", "Madison"]

bFreq = [183330,173981,163266,159945,
         157875,149082,145171,
         142142,139652,137093]

gFreq= [195028,184528,181132,
        170559,155844,129088,118713,
        117626,102470,98419
        ]

df = pd.DataFrame(
    {
        'Boys Names':bNames, 
        'bFreq':bFreq, 
        'Girls Names':gNames,
        'gFreq': gFreq
    }
)

print(df)

print(df.describe())