File :PASCAL Classification.ipynb
	Task : Classification:
	
	This file performs classification for multi label object classifciation(this is before the updated  problem statement)

	Required files:
		1. dataset.csv
		2. annotate.pickle
		3. labels.pickle
----------------------------------------------------------------------------------------------------------
File: PASCAL-Classifaction-Transfer-Learning-Final.ipynb	
	Task : Classification using Transfer Learning(updated problem statement-15 classes)
	
	This file performs classification for single object(s) using VGGnet
	
	Required files:
		1. localization_dataset2.csv
		2. image_labelEncoded.pickle
---------------------------------------------------------------------------------------------------------
File: PASCAL-Localisation.ipynb
	Task: Localisation
	
	This file predicts the bounding boxes for each object(single object in image) and performs localisation

	Required files:
	1. localization_dataset.csv
	2. image_bounds.pickle
	3. image_labelEncoded.pickle
---------------------------------------------------------------------------------------------------------
File: preprocess.py
	Task: Pre proecess the images resizing them to 100 * 100 * 1 and writing the pixel values into a csv
---------------------------------------------------------------------------------------------------------
File: localization_preprocess.py
	Task: Resizes the image into 0.25 times its height * 0.25 times its width and padding them to 128 * 128
--------------------------------------------------------------------------------------------------------
File: hackathon.ipynb
	Task: Using the annotations provided to extract the labels and bounds of the objects, Discard the images with more than one objects in them and create one hot vectors for classification.
--------------------------------------------------------------------------------------------------------
