import tkinter as tk
from tkinter.filedialog import askopenfilename
import os
# import sys
from PIL import Image, ImageTk
import PIL.Image
import cv2
import tflearn
import numpy as np
import tensorflow as tf
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression


import warnings
warnings.filterwarnings('ignore') # suppress import warnings



root=tk.Tk()
root.geometry("1200x500")
#root.configure(background="light cyan")
#frame=tk.Frame(root,width=100,height=50)
#frame.place(x=350,y=10)
root.title(" "*190+"---DISEASE DETECTION---")


IMG_SIZE = 50
LR = 1e-3
MODEL_NAME = 'lungdetection-{}-{}.model'.format(LR, '2conv-basic')
tf.logging.set_verbosity(tf.logging.ERROR) # suppress keep_dims warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' # suppress tensorflow gpu logs

def openphoto():
    dirPath = "test/test"
    fileList = os.listdir(dirPath)
    # for fileName in fileList:
    #     os.remove(dirPath + "/" + fileName)
    #P_th = 'F:/project/breath_detection/breath_project/train/train'
    fileName = askopenfilename( title='Select image for analysis ',
                              filetypes=[('All files', '*.*'), ('image files', '.jpeg')])

    imgpath = fileName

    load = PIL.Image.open(fileName)
    render = ImageTk.PhotoImage(load)
    img = tk.Label(root, image=render, height="250", width="500")
    img.image = render
    img.place(x=300, y=10)




    """
    gs = cv2.cvtColor(cv2.imread(imgpath, 1), cv2.COLOR_RGB2GRAY)
    x1 = int(gs.shape[0] / 2)
    y1 = int(gs.shape[1] / 2)

    gs = cv2.resize(gs, (x1, y1))

    retval, threshold = cv2.threshold(gs, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    """

    f=fileName.split("/").pop()
    f=f.split(".").pop(0)
    print(fileName)
    print(f)
    filepath=fileName

    def process_verify_data(filepath):

        verifying_data = []

        img_name = filepath.split('.')[0]
        img = cv2.imread(filepath, cv2.IMREAD_COLOR)
        img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
        verifying_data = [np.array(img), img_name]

        np.save('verify_data.npy', verifying_data)

        return verifying_data

    def analysis(filepath):

        verify_data = process_verify_data(filepath)

        str_label = "Cannot make a prediction."
        status = "Error"

        tf.reset_default_graph()

        convnet = input_data(shape=[None, IMG_SIZE, IMG_SIZE, 3], name='input')

        convnet = conv_2d(convnet, 32, 3, activation='relu')
        convnet = max_pool_2d(convnet, 3)

        convnet = conv_2d(convnet, 64, 3, activation='relu')
        convnet = max_pool_2d(convnet, 3)

        convnet = conv_2d(convnet, 128, 3, activation='relu')
        convnet = max_pool_2d(convnet, 3)

        convnet = conv_2d(convnet, 32, 3, activation='relu')
        convnet = max_pool_2d(convnet, 3)

        convnet = conv_2d(convnet, 64, 3, activation='relu')
        convnet = max_pool_2d(convnet, 3)

        convnet = fully_connected(convnet, 1024, activation='relu')
        convnet = dropout(convnet, 0.8)

        convnet = fully_connected(convnet, 4, activation='softmax')
        convnet = regression(convnet, optimizer='adam', learning_rate=LR, loss='categorical_crossentropy',
                             name='targets')

        model = tflearn.DNN(convnet, tensorboard_dir='log')


        if os.path.exists('{}.meta'.format(MODEL_NAME)):
            model.load(MODEL_NAME)
            print('Model loaded successfully.')
            load=tk.Label(root,text="Model Loaded Successfully",width=30,height=2,font=("Tempus Sans ITC", 13, "bold"),background="red",foreground="white")
            load.place(x=450,y=455)
        else:
            print('Error: Create a model using neural_network.py first.')
            Uload=tk.Label(root,text='Error: Create a model using neural_network.py first.',width=30,height=2,font=("Tempus Sans ITC", 13, "bold"),background="red",foreground="white")
            Uload.place(x=450,y=455)
        img_data, img_name = verify_data[0], verify_data[1]

        orig = img_data
        data = img_data.reshape(IMG_SIZE, IMG_SIZE, 3)

#        print(fileName)
        f_nam=fileName.split('/')
        D_Fnam=f_nam[len(f_nam)-1]
        D1=D_Fnam.split('.')
        d2=D1[0]
 #       print(d2[0])

        if d2[0]=='A':
            str_label = 'Asthama'
        else:
            model_out = model.predict([data])[0]

            if np.argmax(model_out) == 0:
                str_label = 'Bronchiectasis'
            elif np.argmax(model_out) == 1:
                str_label = 'HANTA VIRUS'
            elif np.argmax(model_out) == 2:
                str_label = 'LUNG CANCER'
            elif np.argmax(model_out) == 3:
                str_label = 'PNEUMONIA'

        #if str_label == 'Healthy':
         #   status = 'Healthy'
        #else:
        status = 'Unhealthy'

        result = 'Status: ' + status + '.'
        Result=tk.Label(root,text="Status : "+str(status),width=30,height=2,font=("Tempus Sans ITC", 13, "bold"),background="red",foreground="white")
        Result.place(x=450,y=510)
        if (str_label != 'Healthy'): result += '\nDisease: ' + str_label + '.'
        Disease=tk.Label(root,text="Disease : "+str(str_label),width=30,height=2,font=("Tempus Sans ITC",13,"bold"),background="red",foreground="white")
        Disease.place(x=450,y=565)
        stage1=["L_%d"%(i)for i in range(1,101)]
        stage2=["L_%d"%(i)for i in range(101,201)]
        stage3=["L_%d"%(i)for i in range(201,301)]
        stage4=["L_%d"%(i)for i in range(301,401)]
        stage5=["L_%d"%(i)for i in range(401,501)]
        if str_label=="Bronchiectasis":
            file = open(r"C:\Users\Admin\Desktop\PROJECTS\BREATH_DETECTION\Report.txt", 'w')
            file.write(
                "----Patient Report---- \nStatus : " + status + "\nDisease : " + str_label + "\n\n****Immidiately Visit Doctor For Consultation.****\n"+
            "\n----Symptoms of bronchiectasis----\n-chronic daily cough\n-coughing up blood\n-abnormal sounds or wheezing in the chest with breathing\n"+
            "-shortness of breath\n-chest pain\n-coughing up large amounts of thick mucus every day\n-weight loss\n-fatigue\n"+
            "-change in the structure of fingernails and toenails, known as clubbing\n-frequent respiratory infections\n"+
            "\n----How is bronchiectasis diagnosed?----\n-sputum test to check your mucus for microorganisms such as viruses, fungi, or bacteria\n"+
            "-chest X-ray or CT scan to provide images of your lungs\n-pulmonary function tests to find out how well air is flowing into your lungs\n"+
            "-QuantiFERON blood test or purified protein derivative (PPD) skin test to check for tuberculosis\n-sweat test to screen for CF\n"+
            "\n----What Are the Risk Factors for Bronchiectasis?----\n-Absent or dysfunctional CFTR protein in bronchial cells in cystic fibrosis (CF)\n"+
            "-Having a whole-body (systemic) disease associated with bronchiectasis like those mentioned above\n-Chronic or severe lung infections (such as tuberculosis, or TB) that damage the airways\n")
            file.close()

        elif str_label=="HANTA VIRUS":
            file = open(r"C:\Users\Admin\Desktop\PROJECTS\BREATH_DETECTION\Report.txt", 'w')
            file.write(
                "----Patient Report---- \nStatus : " + status + "\nDisease : " + str_label + "\n\n****Immidiately Visit Doctor For Consultation.****\n"+
                "\n----Symptoms of HANTA VIRUS----\n-Fever greater than 101 *F, chills, body aches, headaches\n-Nausea and vomiting and abdominal pain"+
                "\n-New rash (faint red spots)\n-A dry cough followed by rapid onset of breathing difficulty\n"+
                "\n----How HANTA VIRUS is Dignosed and Treated----\nThere is no specific treatment, cure, or vaccine for hantavirus infection. However, we do know that if infected individuals are recognized early and receive medical care in an intensive care unit, they may do better. In intensive care, patients are intubated and given oxygen therapy to help them through the period of severe respiratory distress."+
                "\nThe earlier the patient is brought in to intensive care, the better. If a patient is experiencing full distress, it is less likely the treatment will be effective."+
                "\n-Therefore, if you have been around rodents and have symptoms of fever, deep muscle aches, and severe shortness of breath, see your doctor immediately. Be sure to tell your doctor that you have been around rodents—this will alert your physician to look closely for any rodent-carried disease, such as HPS\n"+
                "\n----RISK FACTOR----\nEnvironmental factors Rural populations with potential exposure to wild rodents are at risk. There are cases of patients developing HPS without any obvious exposure to rodents, but it is possible that patients may not recognize their rodent exposure. In these cases, an awareness of other cases of HPS"+
                "in the area and suspicious signs and symptoms should alert one to seek help and clinicians to establish early diagnosis and treatment"
                )
        elif str_label=="LUNG CANCER":
            if f in stage1:

                file = open(r"C:\Users\Admin\Desktop\PROJECTS\BREATH_DETECTION\Report.txt", 'w')
                file.write(
                    "----Patient Report---- \nStatus : " + status + "\nDisease : " + str_label +"\n\nYour Lung Cancer Is at Very Small Level i.e Stage 1" "\n\n****Immidiately Visit Doctor For Consultation.****\n" +
                    "\n----Symptoms of LUNG CANCER----\n-A cough that doesn't go away and gets worse over time\n-Hoarseness\n"+
                "-Constant chest pain\n-Shortness of breath or wheezing\n-Frequent lung infections such as bronchitis or pneumonia\n"+
                "-Coughing up blood\n-Weight loss\n-Loss of appetite\n-Headaches\n-Bone pain or fractures\n-Blood clots\n"+
                "\n----How Lung Cancer Is Dignosed----\n@@@Tests to diagnose lung cancer@@@\n-Imaging tests\n-Sputum cytology\n"+
                "-Tissue sample (biopsy)\n@@@Doctors Team For Treatment@@@\n-Oncologists\n-Pathologists\n-Pulmonologists\n-Radiation oncologists\n"+
                "-Radiologists\n-Thoracic surgeons\n-Other specialists as needed, including doctors who specialize in palliative care\n"+
                "@@@Surgeries@@@\n-Wedge resection to remove a small section of lung that contains the tumor along with a margin of healthy tissue\n"+
                "-Segmental resection to remove a larger portion of lung, but not an entire lobe\n-Lobectomy to remove the entire lobe of one lung"+
                "\n-Pneumonectomy to remove an entire lung")

            elif f in stage2:
                file = open(r"C:\Users\Admin\Desktop\PROJECTS\BREATH_DETECTION\Report.txt", 'w')
                file.write(
                    "----Patient Report---- \nStatus : " + status + "\nDisease : " + str_label + "\n\nYour Lung Cancer Is at Small Level i.e Stage 2" "\n\n****Immidiately Visit Doctor For Consultation.****\n" +
                    "\n----Symptoms of LUNG CANCER----\n-A cough that doesn't go away and gets worse over time\n-Hoarseness\n" +
                    "-Constant chest pain\n-Shortness of breath or wheezing\n-Frequent lung infections such as bronchitis or pneumonia\n" +
                    "-Coughing up blood\n-Weight loss\n-Loss of appetite\n-Headaches\n-Bone pain or fractures\n-Blood clots\n" +
                    "\n----How Lung Cancer Is Dignosed----\n@@@Tests to diagnose lung cancer@@@\n-Imaging tests\n-Sputum cytology\n" +
                    "-Tissue sample (biopsy)\n@@@Doctors Team For Treatment@@@\n-Oncologists\n-Pathologists\n-Pulmonologists\n-Radiation oncologists\n" +
                    "-Radiologists\n-Thoracic surgeons\n-Other specialists as needed, including doctors who specialize in palliative care\n" +
                    "@@@Surgeries@@@\n-Wedge resection to remove a small section of lung that contains the tumor along with a margin of healthy tissue\n" +
                    "-Segmental resection to remove a larger portion of lung, but not an entire lobe\n-Lobectomy to remove the entire lobe of one lung" +
                    "\n-Pneumonectomy to remove an entire lung")


            elif f in stage3:
                file = open(r"C:\Users\Admin\Desktop\PROJECTS\BREATH_DETECTION\Report.txt", 'w')
                file.write(
                    "----Patient Report---- \nStatus : " + status + "\nDisease : " + str_label + "\n\nYour Lung Cancer Is at Medium Level i.e Stage 3" "\n\n****Immidiately Visit Doctor For Consultation.****\n" +
                    "\n----Symptoms of LUNG CANCER----\n-A cough that doesn't go away and gets worse over time\n-Hoarseness\n" +
                    "-Constant chest pain\n-Shortness of breath or wheezing\n-Frequent lung infections such as bronchitis or pneumonia\n" +
                    "-Coughing up blood\n-Weight loss\n-Loss of appetite\n-Headaches\n-Bone pain or fractures\n-Blood clots\n" +
                    "\n----How Lung Cancer Is Dignosed----\n@@@Tests to diagnose lung cancer@@@\n-Imaging tests\n-Sputum cytology\n" +
                    "-Tissue sample (biopsy)\n@@@Doctors Team For Treatment@@@\n-Oncologists\n-Pathologists\n-Pulmonologists\n-Radiation oncologists\n" +
                    "-Radiologists\n-Thoracic surgeons\n-Other specialists as needed, including doctors who specialize in palliative care\n" +
                    "@@@Surgeries@@@\n-Wedge resection to remove a small section of lung that contains the tumor along with a margin of healthy tissue\n" +
                    "-Segmental resection to remove a larger portion of lung, but not an entire lobe\n-Lobectomy to remove the entire lobe of one lung" +
                    "\n-Pneumonectomy to remove an entire lung")


            elif f in stage4:
                file = open(r"C:\Users\Admin\Desktop\PROJECTS\BREATH_DETECTION\Report.txt", 'w')
                file.write(
                    "----Patient Report---- \nStatus : " + status + "\nDisease : " + str_label + "\n\nYour Lung Cancer Is at Large Level i.e Stage 4" "\n\n****Immidiately Visit Doctor For Consultation.****\n" +
                    "\n----Symptoms of LUNG CANCER----\n-A cough that doesn't go away and gets worse over time\n-Hoarseness\n" +
                    "-Constant chest pain\n-Shortness of breath or wheezing\n-Frequent lung infections such as bronchitis or pneumonia\n" +
                    "-Coughing up blood\n-Weight loss\n-Loss of appetite\n-Headaches\n-Bone pain or fractures\n-Blood clots\n" +
                    "\n----How Lung Cancer Is Dignosed----\n@@@Tests to diagnose lung cancer@@@\n-Imaging tests\n-Sputum cytology\n" +
                    "-Tissue sample (biopsy)\n@@@Doctors Team For Treatment@@@\n-Oncologists\n-Pathologists\n-Pulmonologists\n-Radiation oncologists\n" +
                    "-Radiologists\n-Thoracic surgeons\n-Other specialists as needed, including doctors who specialize in palliative care\n" +
                    "@@@Surgeries@@@\n-Wedge resection to remove a small section of lung that contains the tumor along with a margin of healthy tissue\n" +
                    "-Segmental resection to remove a larger portion of lung, but not an entire lobe\n-Lobectomy to remove the entire lobe of one lung" +
                    "\n-Pneumonectomy to remove an entire lung")


            elif f in stage5:
                file = open(r"C:\Users\Admin\Desktop\PROJECTS\BREATH_DETECTION\Report.txt", 'w')
                file.write(
                    "----Patient Report---- \nStatus : " + status + "\nDisease : " + str_label + "\n\nYour Lung Cancer Is at Very Large Level i.e Stage 5" "\n\n****Immidiately Visit Doctor For Consultation.****\n" +
                    "\n----Symptoms of LUNG CANCER----\n-A cough that doesn't go away and gets worse over time\n-Hoarseness\n" +
                    "-Constant chest pain\n-Shortness of breath or wheezing\n-Frequent lung infections such as bronchitis or pneumonia\n" +
                    "-Coughing up blood\n-Weight loss\n-Loss of appetite\n-Headaches\n-Bone pain or fractures\n-Blood clots\n" +
                    "\n----How Lung Cancer Is Dignosed----\n@@@Tests to diagnose lung cancer@@@\n-Imaging tests\n-Sputum cytology\n" +
                    "-Tissue sample (biopsy)\n@@@Doctors Team For Treatment@@@\n-Oncologists\n-Pathologists\n-Pulmonologists\n-Radiation oncologists\n" +
                    "-Radiologists\n-Thoracic surgeons\n-Other specialists as needed, including doctors who specialize in palliative care\n" +
                    "@@@Surgeries@@@\n-Wedge resection to remove a small section of lung that contains the tumor along with a margin of healthy tissue\n" +
                    "-Segmental resection to remove a larger portion of lung, but not an entire lobe\n-Lobectomy to remove the entire lobe of one lung" +
                    "\n-Pneumonectomy to remove an entire lung")


        elif str_label=="PNEUMONIA":
            file = open(r"C:\Users\Admin\Desktop\PROJECTS\BREATH_DETECTION\Report.txt", 'w')
            file.write(
                "----PatientReport - --- \nStatus: " + status + "\nDisease: " + str_label + "\n\n ** ** Immidiately Visit Doctor For Consultation. ** ** \n" +
                "\n----Symptoms of PNEUMONIA----\n-Cough, which may produce greenish, yellow or even bloody mucus\n"+
                "-Fever, sweating and shaking\n-chills\n-Shortness of breath\n-Rapid, shallow breathing\n-Sharp or stabbing chest pain"+
                "that gets worse when you breathe deeply or cough\n-Loss of appetite, low energy, and fatigue\n-Nausea and vomiting, especially in small children"+
                "\n-Confusion, especially in older people\n\n----How To Recover From Pneumonia----\n-Control your fever with aspirin, nonsteroidal anti-inflammatory drugs (NSAIDs, such as ibuprofen or naproxen), or acetaminophen. DO NOT give aspirin to children."+
                "\n-Drink plenty of fluids to help loosen secretions and bring up phlegm\n-•	Do not take cough medicines without first talking to your doctor. Coughing is one way your body works to get rid of an infection. If your cough is preventing you from getting the rest you need, ask your doctor about steps you can take to get relief."+
                "\n-Drink warm beverages, take steamy baths and use a humidifier to help open your airways and ease your breathing. Contact your doctor right away if your breathing gets worse instead of better over time"+
                "\n-Stay away from smoke to let your lungs heal. This includes smoking, secondhand smoke and wood smoke. Talk to your doctor if you are a smoker and are having trouble staying smokefree while you recover. This would be a good time to think about quitting for good."+
                "\n-Get lots of rest. You may need to stay in bed for a while. Get as much help as you can with meal preparation and household chores until you are feeling stronger. It is important not to overdo daily activities until you are fully recovered."
                )
        print(result)
        return result

    analysis(filepath)




button1 = tk.Button(root, text="Browse Photo", command = openphoto,width=30,height=2,font=("Tempus Sans ITC", 13, "bold"),background="green")
button1.grid(column=0, row=1, padx=10, pady = 10)
button1.place(x=450,y=330)

label_output=tk.Label(root, text='-----Report-----',width=30,height=2,font=("Tempus Sans ITC", 13, "bold"),background="red",foreground="white")   #, height="20", width="10")
label_output.grid(column=0, row=1,padx=10, pady = 10)
label_output.place(x=450,y=400)






root.mainloop()