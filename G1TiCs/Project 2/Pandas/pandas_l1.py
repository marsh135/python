import pandas as pd


gNames = ["Emma", "Olivia", "Ava", "Isabella", "Sophia", 
          "Mia", "Charlotte", "Amelia", "Harper", "Evelyn"]
gFreq = [18688, 17921, 14924, 13084, 12903, 12345, 11903, 11575, 11286, 10898]


bNames = ["Noah", "Liam", "William", "James", "Oliver", 
          "Benjamin", "Elijah", "Lucas", "Mason", "Logan"]
bFreq = [19144, 18267, 14516, 13011, 12803, 12160, 11951, 11538, 11297, 10875]


df = pd.DataFrame({
    "bNames": bNames,
    "bFreqs": bFreq,
    "gNames": gNames,
    "gFreqs": gFreq
})

print(round(df.describe()))
