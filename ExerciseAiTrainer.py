import cv2
import PoseModule2 as pm
import numpy as np
import streamlit as st
from AiTrainer_utils import *


# Define the class that handle the analysis of the exercises
class Exercise:
    def __init__(self):
        pass

    # Visualize the angle between 3 point on screen
    def visualize_angle(self,img, angle, landmark):
            cv2.putText(img, str(angle),
                        tuple(np.multiply(landmark, [640, 480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                        )

    # Visualize repetitions of the exercise on screen
    def repetiotions_counter(self, img, counter):
        cv2.rectangle(img, (0, 0), (225, 73), (245, 117, 16), -1)

        # Rep data
        cv2.putText(img, 'REPS', (15, 12),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
        cv2.putText(img, str(counter),
                    (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

    # define a push up counter
    def push_up(self, cap):

        # create a empty space in streamlit for latar visualize the webcam
        stframe = st.empty()

        cap = cap

        # define repetitions counter
        pushUpStart = 0
        pushUpCount = 0

        # find person position and landmarks
        detector = pm.posture_detector()
        while cap.isOpened():
            # take the webcam as input
            ret, frame = cap.read()
            img = detector.find_person(frame)
            landmark_list = detector.find_landmarks(img, False)
            # check if landmark are detected
            if len(landmark_list) != 0:

                # find angle of relevant point (arm, shoulder, wrist)
                right_arm_angle = detector.find_angle(img, 12, 14, 16)
                right_shoulder = landmark_list[12][1:]
                right_wrist = landmark_list[16][1:]

                # Visualize angle on screen
                right_elbow = landmark_list[14][1:]
                self.visualize_angle(img, right_arm_angle, right_elbow)

                # calculate distance between shoulder and wrist and use it as threshold for a repetition
                if distanceCalculate(right_shoulder, right_wrist) < 130:
                    pushUpStart = 1
                elif pushUpStart and distanceCalculate(right_shoulder, right_wrist) > 250:
                    pushUpCount = pushUpCount + 1
                    pushUpStart = 0

            # Visualize the repetitions
            self.repetiotions_counter(img, pushUpCount)

            # resize frames of the webcam and visualize it on webapp
            img = cv2.resize(img, (0, 0), fx=0.8, fy=0.8)
            img = image_resize(image=img, width=640)
            stframe.image(img, channels='BGR', use_column_width=True)

            # close webcam
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        # close webcam
        cap.release()
        cv2.destroyAllWindows()

    # define squat methods
    def squat(self, cap):
        stframe = st.empty()

        cap = cap

        counter = 0
        stage = None

        detector = pm.posture_detector()
        while cap.isOpened():
            ret, frame = cap.read()
            img = detector.find_person(frame)
            landmark_list = detector.find_landmarks(img, False)
            if len(landmark_list) != 0:

                right_leg_angle = detector.find_angle(img, 24, 26, 28)
                left_leg_angle = detector.find_angle(img, 23, 25, 27)

                # Visualize angle
                right_leg = landmark_list[26][1:]

                self.visualize_angle(img, right_leg_angle, right_leg)

                # define the threshold for the angle in order to count a valid repetition of the squat
                if right_leg_angle > 140 and left_leg_angle < 240:
                    stage = "down"
                if right_leg_angle < 80 and left_leg_angle > 270 and stage == 'down':
                    stage = "up"
                    counter += 1

            self.repetiotions_counter(img, counter)

            img = cv2.resize(img, (0, 0), fx=0.8, fy=0.8)
            img = image_resize(image=img, width=640)
            stframe.image(img, channels='BGR', use_column_width=True)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break


        cap.release()
        cv2.destroyAllWindows()

    # define bicep curl method
    def bicept_curl(self, cap):
        stframe = st.empty()
        cap = cap

        # initialize repetition counter
        counter = 0
        stage = None

        detector = pm.posture_detector()
        while cap.isOpened():
            ret, frame = cap.read()
            img = detector.find_person(frame)
            landmark_list = detector.find_landmarks(img, False)
            if len(landmark_list) != 0:

                right_arm_angle = detector.find_angle(img, 12, 14, 16)
                left_arm_angle = detector.find_angle(img, 11, 13, 15)

                # Visualize angle
                right_elbow = landmark_list[14][1:]

                self.visualize_angle(img, right_arm_angle, right_elbow)

                # define the threshold of the angle for a valid repetition of the exercise
                if left_arm_angle <230:
                    stage = "down"
                if left_arm_angle > 310 and stage == 'down':
                    stage = "up"
                    counter += 1

            self.repetiotions_counter(img, counter)

            img = cv2.resize(img, (0, 0), fx=0.8, fy=0.8)
            img = image_resize(image=img, width=640)
            stframe.image(img, channels='BGR', use_column_width=True)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    # define shoulder press method
    def shoulder_press(self, cap):
        stframe = st.empty()

        cap = cap

        counter = 0
        stage = None

        detector = pm.posture_detector()
        while cap.isOpened():
            ret, frame = cap.read()
            img = detector.find_person(frame)
            landmark_list = detector.find_landmarks(img, False)
            if len(landmark_list) != 0:

                right_arm_angle = detector.find_angle(img, 12, 14, 16)
                left_arm_angle = detector.find_angle(img, 11, 13, 15)

                # Visualize angle
                right_elbow = landmark_list[14][1:]

                self.visualize_angle(img, right_arm_angle, right_elbow)

                if right_arm_angle > 315 and left_arm_angle < 40:
                    stage = "down"
                if right_arm_angle < 240 and left_arm_angle > 130 and stage == 'down':
                    stage = "up"
                    counter += 1

            self.repetiotions_counter(img, counter)

            img = cv2.resize(img, (0, 0), fx=0.8, fy=0.8)
            img = image_resize(image=img, width=640)
            stframe.image(img, channels='BGR', use_column_width=True)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()


