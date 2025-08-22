from mlforkidsimages import MLforKidsImageProject

# treat this key like a password and keep it secret!
key = "d4955a40-6cba-11f0-b691-19ad30a6c5908e7ad7bc-5f71-405f-8693-3cd4a05d9508"

# this will train your model and might take a little while
myproject = MLforKidsImageProject(key)
myproject.train_model()

# CHANGE THIS to the image file you want to recognize
demo = myproject.prediction("ml/testingData/test1.png")

label = demo["class_name"]
confidence = demo["confidence"]

# CHANGE THIS to do something different with the result
print ("result: '%s' with %d%% confidence" % (label, confidence))