import streamlit as st
from Audio import text_to_speech, get_audio
import cv2
import tempfile
import ExerciseAiTrainer as exercise


def main():

    # Define App Title and Structure
    st.title('Your AI Personal Trainer')

    st.write("""
        ## Welcome to your personal AI trainer
        """)

    # 2 Options: Video, WebCam
    options = st.sidebar.selectbox('Select Option', ('Video', 'WebCam'))

    #  Define Operations if Video Option is selected
    if options == 'Video':

        st.write('## Import your video and select the correct type of Exercise')

        st.set_option('deprecation.showfileUploaderEncoding', False)

        # User can select different types of exercise
        exercise_options = st.sidebar.selectbox(
            'Select Exercise', ('Bicept Curl', 'Push Up', 'Squat', 'Shoulder Press')
        )

        st.sidebar.markdown('-------')

        # User can upload a video:
        video_file_buffer = st.sidebar.file_uploader("Upload a video", type=["mp4", "mov", 'avi', 'asf', 'm4v'])
        tfflie = tempfile.NamedTemporaryFile(delete=False)

        # if no video uploaded the use a demo
        if not video_file_buffer:
            DEMO_VIDEO = 'demo.mp4'
            cap = cv2.VideoCapture(DEMO_VIDEO)
            tfflie.name = DEMO_VIDEO

        # if video is uploaded then analyze the video
        else:
            tfflie.write(video_file_buffer.read())
            cap = cv2.VideoCapture(tfflie.name)

        # Visualize Video before analysis
        st.sidebar.text('Input Video')
        st.sidebar.video(tfflie.name)

        st.markdown('## Input Video')
        st.video(tfflie.name)

        # Visualize Video after analysis (analysis based on the selected exercise)
        st.markdown(' ## Output Video')
        if exercise_options == 'Bicept Curl':
            exer = exercise.Exercise()
            exer.bicept_curl(cap)

        elif exercise_options == 'Push Up':
            exer = exercise.Exercise()
            exer.push_up(cap)

        elif exercise_options == 'Squat':
            exer = exercise.Exercise()
            exer.squat(cap)

        elif exercise_options == 'Shoulder Press':
            exer = exercise.Exercise()
            exer.shoulder_press(cap)

    # Define Operation if webcam option is selected
    elif options == 'WebCam':

        # User can select different exercises
        exercise_general = st.sidebar.selectbox(
            'Select Exercise', ('Bicept Curl', 'Push Up', 'Squat', 'Shoulder Press')
        )

        # Define a button for start the analysis (pose estimation) on the webcam
        st.write(' ## Click button to activate AI Trainer')
        st.write("Say 'Ready' to get started")
        button = st.button('Activate AI Trainer')

        # Visualize video that exlpain the correct forms for the exercises
        if exercise_general == 'Bicept Curl':
            st.write('## Bicept Curl Execution')
            st.video('curl_form.mp4')

        elif exercise_general == 'Push Up':
            st.write('## Push Up Execution')
            st.video('push_up_form.mp4')

        elif exercise_general == 'Squat':
            st.write('## Squat Execution')
            st.video('squat_form.mp4')

        elif exercise_general == 'Shoulder Press':
            st.write('## Shoulder Press Execution')
            st.video('shoulder_press_form.mp4')

        # if the button is selected, after a Vocal command, start the webcam analysis (pose estimation)
        if button:
            # Ask user if want to start the training (using text to speech)
            text_to_speech('Are you Ready to start Training?')
            # get the audio of the user
            text = get_audio()

            # if user is ready (say 'yes' or 'ready') then start the webcam analysis
            if 'ready' or 'yes' in text:

                text_to_speech("Ok, Let's get started")
                st.write(str('READY'))
                ready = True

                # for each type of exercise call the method that analyze that exercise
                if exercise_general == 'Bicept Curl':
                    while ready:
                        cap = cv2.VideoCapture(0)
                        exer = exercise.Exercise()
                        exer.bicept_curl(cap)

                elif exercise_general == 'Push Up':
                    while ready:
                        cap = cv2.VideoCapture(0)
                        exer = exercise.Exercise()
                        exer.push_up(cap)

                elif exercise_general == 'Squat':
                    while ready:
                        cap = cv2.VideoCapture(0)
                        exer = exercise.Exercise()
                        exer.squat(cap)

                elif exercise_general == 'Shoulder Press':
                    while ready:
                        cap = cv2.VideoCapture(0)
                        exer = exercise.Exercise()
                        exer.shoulder_press(cap)


if __name__ == '__main__':
    main()