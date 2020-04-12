from imutils.video import VideoStream
from imutils.video import FPS
import numpy as np
import argparse
import imutils
import time
import cv2
import wrnchAI
import argparse
import matplotlib.pyplot as plt

import sys
from visualizer import Visualizer
from utils import videocapture_context
import math
import bezier
from geopy.distance import geodesic
ap = argparse.ArgumentParser()

ap.add_argument("-i", "--input", type=str, help="path to  input video file")
ap.add_argument('--models', '-m', type=str, required=True)
ap.add_argument('--license', '-k', type=str, default=None)

args = vars(ap.parse_args())

print("[INFO] opening video file...")
#Count the frames you are processing right now .So we can skip the
totalFrames = 0
flag=0

params = wrnchAI.PoseParams()
params.bone_sensitivity = wrnchAI.Sensitivity.high
params.joint_sensitivity = wrnchAI.Sensitivity.high
params.enable_tracking = True
params.preferred_net_width = 328
params.preferred_net_height = 184
frame_count=0

options = wrnchAI.PoseEstimatorOptions()
#Options maybe something
output_format = wrnchAI.JointDefinitionRegistry.get('j23')

print('Initializing networks...')
estimator = wrnchAI.PoseEstimator(models_path=args["models"],
                                    license_string=args["license"],
                                    params=params,
                                    gpu_id=0,
                                    output_format=output_format)

visualizer = Visualizer()
joint_definition = estimator.human_2d_output_format()
bone_pairs = joint_definition.bone_pairs()
with videocapture_context(args["input"]) as cap:
    visualizer = Visualizer()
    array_area=np.array([])
    joint_definition = estimator.human_2d_output_format()
    #print(joint_definition.joint_names())
    bone_pairs = joint_definition.bone_pairs()
    print (joint_definition.print_joint_definition())
    while True:
        _, frame = cap.read()
        frame_count=frame_count+1
        
        

        if frame is not None:

            estimator.process_frame(frame, options)

            humans2d = estimator.humans_2d()
            rshoulder = joint_definition.get_joint_index("RSHOULDER")# getting right shoulder defination
            lshoulder = joint_definition.get_joint_index("LSHOULDER")# getting left shoulder defination
            head = joint_definition.get_joint_index("HEAD")# getting  head defination
            nose = joint_definition.get_joint_index("NOSE")# getting  nose defination
            # print(rshoulder,lshoulder,head)
            visualizer.draw_image(frame)
            for human in humans2d:
                joints = np.double(human.joints())
                
                nodes = np.asfortranarray([   [joints[lshoulder*2] * 500 ,joints[nose*2] * 500,joints[rshoulder*2]*500],
                    [joints[lshoulder*2+1] * 500,joints[nose*2+1] * 500,joints[rshoulder*2+1] * 500] ])
                
                print(joints[lshoulder * 2 +1])
                print(joints[rshoulder * 2 +1])
                print(joints[nose * 2 +1])
                print("---------------------------------------------------------------------------")
                curve = bezier.Curve(nodes,degree=2) 
                left, right = curve.subdivide()
                # curve.evaluate(0.50)
                
                if joints[nose * 2 +1]>0.45:
                    if abs(joints[rshoulder * 2 +1]-joints[lshoulder * 2 +1])>=.025:    
                        curve.plot(num_pts=256)
                        plt.show()
                        
                        cv2.putText(frame,"Fatigue Detected", (100,50),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)        
                	
                visualizer.draw_points(joints)
                visualizer.draw_lines(joints, bone_pairs)

            
            visualizer.show()
            key = cv2.waitKey(1)
        else:

            cap.release()
            cv2.destroyAllWindows() 
            exit()

       