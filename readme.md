# **Single Fingerprint Deep Classification**
### **JCE - Software Engineering Final Project** 
##### ***By Kobi Amsellem & Zohar Kedem***

<br />

##### In this study we want to discovare if Deep Convolutional Neural Network can classify single fingerprint image to find the owner: 
* ##### **1. Gender** - 2 classes (male/female).
* ##### **2. Finger name** - 10 classes (right-thumb, ..., right-thumb, ...)
* ##### **3. Fingerprint type** - 5 classes (left loop, whirl, right loop, tented arch, arch)
* ##### **4. Same Person** - 2 classes (Same, Different) *(whether or not two fingerprints belong to the same personperson)* 

#### **Model Search** 

we define the ````researchBestModel````, a method to search and compare between several different models and hyperparameters to choose the best one for dataset.

##### **Stages of** ````researchBestModel````:
* ##### **1.** Backbone Transfer Learning mode comparison - (a) Pretraind wheights and Untrainable, (b) Pretraind wheights and Trainable, (c) Initialize wheight and Trainable.
* ##### **2.** Loss function comparison. 
* ##### **3.** Learning rates comparison. 
* ##### **4.** Optimizers comparison. 
* ##### **5.** Backbone comparison. 
* ##### **6.** Train best configuration for extra epochs on train+validation datasets

<br />
<br />

## **Studies we search on this project:**
<br />

### **1. Gender Study** 
* #### **Datasets**
    * ***SOCOFing***
    * ***NIST Special Database 4***

* #### **Hyperparameters**
    * Optimizers: *Adam, Nadam, RMSprop*
    * Loss Functions: *binary-crossentropy, binary-focal-crossentropy, hinge*
    * Learning Rates: *0.1, 0.01, 0.001, 0.0001, 0.00001*
    * Backbones: *MobileNetV2, ResNet50, EfficientNetB2, InceptionV3, Xception*
<br />

### **2. Finger Name** 
* #### **Datasets:**
    * ***SOCOFing***
    * ***NIST Special Database 4***
    * ***NIST Special Database 300a Roll***
    * ***NIST Special Database 300b - All Scanners***

* #### **Hyperparameters**
    * Optimizers: *Adam, Nadam, RMSprop*
    * Loss Functions: *categorical-crossentropy, mean-squared-error, categorical-hinge*
    * Learning Rates: *0.1, 0.01, 0.001, 0.0001, 0.00001*
    * Backbones: *MobileNetV2, ResNet50, EfficientNetB2, InceptionV3, Xception*