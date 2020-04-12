# Fatigue-Detection_using-Pose-Estimation
To detection fatigue based on body joint positions (skeletal features)

Fatigue is a major cause of road accidents and has important affect on road safety measures.Several deadly accidents can be prevented if the drowsy drivers are warned in time. There has been a lot of work done using different drowsiness detection techniques to monitor the driver’s fatigue statewhiledrivingandalarmdriversiftheyarenotconcentrating on driving.In a survey conducted by National Safety Council,it is found that chances of accidents are three time more , if driver is fatigued. Another survey conducted by National Highway Trafﬁc Safety Administration shows that approximately one million crashes are due to drowsiness while driving.In this paper ,we are going to discuss fatigue detection using pose estimation. 

We are currently using self labelled dataset consists of six videos. We have created artiﬁcial environment similar to person driving the vehicle.We did this by sitting in the classroom and then artiﬁcially behaving as if person is feeling drowsy. 

In this project, we are planning to implement pose estimation technique either by using wrnchAI which is a real time AI software platform or using open-source algorithm,OpenPose [3],to detect human skeleton from each video frame and then utilize the skeleton to extract features and make classiﬁcation by using machine learning algorithm.In this,the recognition of human action is based on human skeleton data.The features of human skeleton are concise and are easy for differentiating different human actions.Thus, we chose human skeleton as the base feature for our project.After extracting the joint positions,we will focus mainly on three joint locations - left shoulder,right shoulder and head.In our ﬁrst approach, we calculated eucledian distance 1 between left shoulder and right shoulder.We took the ratio of fatigued pose and normal pose and determined a thresholding point to calculate fatigue.We were able to detect fatigue in four out of six videos of our dataset. 

To improve accuracy, we then considered nose coordinates as well. We calculated the area of triangle 2 formed by these three coordinates.The ratio of area of normal posture and fatigued posture is then calculated.The thresholding point for fatigue was chosen and based on that we were detecting fatigue.We were able to detect fatigue in ﬁve out of six videos of our dataset.

For improving our results , we are now implementing a new approach using bezier curves What we have done till now is that we have analysed the pattern of curves and distinguished curves for fatigue and non-fatigue posture.We are generalising our threshold to distinguish between both the postures and we are getting quite good results


