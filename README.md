# DataWizard
It is written to generate data from real-time camera images or video frames for computer vision projects. 


Parameters of the dataWizard class:
  - path : file path to save images
  - cam : video path or camera number to take image
  - camBrightness: brightness adjustment

Parameters of the saveData function:
  - w: width (for the image to be saved)
  - h: height
  - per: one out of every per images taken is saved
  - grayImage: gray(True) or colored(False)
  - showImage : image display (Boolean)
  - minBlur: to avoid blurry images.
