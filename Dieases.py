import os
import tkinter as tk
from tkinter import ttk, LEFT, END
from tkinter.filedialog import askopenfilename

from PIL import Image , ImageTk
import cv2
import numpy as np
root = tk.Tk()
root.geometry("1000x600")

tabControl = ttk.Notebook(root)          # Create Tab Control
tab1 = ttk.Frame(tabControl)            # Create a tab



tabControl.add(tab1, text='  Pre-Process   ') # Add the tab

#tab2 = ttk.Frame(tabControl)            # Create a tab
#tabControl.add(tab2, text='   Alexnet   ')

tab3 = ttk.Frame(tabControl)            # Create a tab
tabControl.add(tab3, text='   Detection   ')

tabControl.pack(expand=True, fill="both")


import tkinter as tk
from tkinter.filedialog import askopenfilename
import os
# import sys
from PIL import Image, ImageTk
import cv2
import csv
import pandas as pd

FName = tk.StringVar()
FName.set("")


    # title.pack()
   # title.grid(column=1, row=0, sticky=tk.NSEW)





def bphoto():

        global fn
        fileName = askopenfilename(initialdir='/dataset', title='Select image for analysis ',
                                   filetypes=[("all files", "*.*")])

        imgpath = fileName
        fn = fileName
        Sel_F = fileName.split('/').pop()
        Sel_F = Sel_F.split('.').pop(0)

        gs = cv2.cvtColor(cv2.imread(imgpath, 1), cv2.COLOR_RGB2GRAY)
        x1 = int(gs.shape[0])
        y1 = int(gs.shape[1])

        gs = cv2.resize(gs, (x1, y1))

        retval, threshold = cv2.threshold(gs, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

        im = Image.fromarray(gs)
        imgtk = ImageTk.PhotoImage(image=im)
        img = tk.Label(frame1, image=imgtk, height=x1, width=y1)
        img.image = imgtk
        img.grid(row=4, column=0, sticky=tk.NE)  # , columnspan=2, rowspan=2,sticky=tk.E)   #, padx=10, pady=10)


def analysis():
        global fn
        FName = fn

        imgpath = FName

        gs = cv2.cvtColor(cv2.imread(imgpath, 1), cv2.COLOR_RGB2GRAY)

        x1 = int(gs.shape[0])
        y1 = int(gs.shape[1])

        gs = cv2.resize(gs, (x1, y1))

        retval, threshold = cv2.threshold(gs, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        im = Image.fromarray(threshold)
        imgtk = ImageTk.PhotoImage(image=im)

        img2 = tk.Label(frame1, image=imgtk, height=x1, width=y1)
        img2.image = imgtk
        img2.grid(column=1, row=4, sticky=tk.NE)

def edges():
    global fn
    FName = fn

    global eg

    imgpath = FName


    BLUR = 21
    CANNY_THRESH_1 = 10
    CANNY_THRESH_2 = 200
    MASK_DILATE_ITER = 10
    MASK_ERODE_ITER = 10


    img = cv2.imread(imgpath,1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    x1 = int(gray.shape[0])
    y1 = int(gray.shape[1])

    gray = cv2.resize(gray, (x1, y1))
    #cv2.imshow("img", img)
    #cv2.waitKey()

    # edges
    #cv2.destroyAllWindows()
    edges = cv2.Canny(gray, CANNY_THRESH_1, CANNY_THRESH_2)
    edges = cv2.dilate(edges, None)
    edges = cv2.erode(edges, None)

    #display image
    im = Image.fromarray(edges)
    imgtk = ImageTk.PhotoImage(image=im)
    img3 = tk.Label(frame1, image=imgtk, height=x1, width=y1)
    img3.image = imgtk
    img3.grid(column=2, row=4, sticky=tk.NE)

    eg = edges
    #cv2.imshow("edges", edges)
    #cv2.waitKey()

def mask():

    BLUR = 21
    MASK_DILATE_ITER = 10
    MASK_ERODE_ITER = 10


    #import edges o/p as i/p to mask
    global eg
    edges = eg

    #import orignal image
    global fn
    FName = fn
    imgpath = FName

    global ms
    global imgm

    img = cv2.imread(imgpath, 1)

    x1 = int(edges.shape[0])
    y1 = int(edges.shape[1])

    edges = cv2.resize(edges, (x1, y1))

    contour_info = []
    contours, __ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

    for c in contours:
        contour_info.append((c, cv2.isContourConvex(c), cv2.contourArea(c),))
    contour_info = sorted(contour_info, key=lambda c: c[2], reverse=True)

    max_contour = contour_info[0]
    mask = np.zeros(edges.shape)
    cv2.fillConvexPoly(mask, max_contour[0], (255))

    mask = cv2.dilate(mask, None, iterations=MASK_DILATE_ITER)
    mask = cv2.erode(mask, None, iterations=MASK_ERODE_ITER)
    mask = cv2.GaussianBlur(mask, (BLUR, BLUR), 0)

    mask_stack = np.dstack([mask] * 3)
    mask_stack = mask_stack.astype('float32') / 255.0
    imgmk = img.astype('float32') / 255.0

    im = Image.fromarray(mask)
    imgtk = ImageTk.PhotoImage(image=im)
    img4 = tk.Label(frame1, image=imgtk, height=x1, width=y1)
    img4.image = imgtk
    img4.grid(column=0, row=5, sticky=tk.N)

    ms = mask_stack
    imgm = imgmk


def masked():

    global ms
    global imgm

    mask_stack = ms
    img = imgm

    x1 = int(img.shape[0])
    y1 = int(img.shape[1])


    MASK_COLOR = (0.0, 0.0, 0.0)  # In BGR format

    masked = (mask_stack * img) + ((1 - mask_stack) * MASK_COLOR)
    masked = (masked * 255).astype('uint8')

    im = Image.fromarray(masked)
    imgtk = ImageTk.PhotoImage(image=im)
    img4 = tk.Label(frame1, image=imgtk)
    img4.image = imgtk
    img4.grid(column=1, row=5, sticky=tk.W)



button_p1 = tk.Button(tab1,text="Browse Photo", command=bphoto, width=10)
button_p1.grid(column=0, row=1, sticky=tk.W, padx=10, pady=10)
button_p1.place(x=50, y=520)

button_p2 = tk.Button(tab1,text="Threshold Image", command=analysis, width=15)
button_p2.grid(column=1, row=1, sticky=tk.W, padx=10, pady=10)
button_p2.place(x=160, y=520)

button_p3 = tk.Button(tab1, text="Edges", command=edges, width=10)
button_p3.grid(column=2, row=1, sticky=tk.W, padx=10, pady=10)
button_p3.place(x=300, y=520)
#
# button_p4 = tk.Button(tab1, text="Mask", command=mask, width=10)
# button_p4.grid(column=3, row=1, sticky=tk.W, padx=10, pady=10)
# button_p4.place(x=400, y=520)
#
# button_p5 = tk.Button(tab1, text="Masked", command=masked, width=10)
# button_p5.grid(column=4, row=1, sticky=tk.W, padx=10, pady=10)
# button_p5.place(x=500, y=520)


def openphoto():
    dirPath = "test/test"
    fileList = os.listdir(dirPath)
    # for fileName in fileList:
    #     os.remove(dirPath + "/" + fileName)
    P_th='F:/project/breath_detection/breath_project/train/train'
    fileName = askopenfilename(initialdir=P_th, title='Select image for analysis ',
                           filetypes=[('All files', '*.*'),('image files', '.jpeg')])
    f=fileName.split('/').pop()
    print(f)
    #f=f.split('.').pop(0)
    #print(f)


    #print(filename)
    dst = "test/test"

    def Convert(string):
        global output_lbl




        li = list(string.split("/"))

        return li

    myarray = np.asarray(Convert(fileName))
    li = list(myarray[len(myarray) - 1].split("_"))
    myarray1 = np.asarray(li)
    print(myarray1[0])

    if (myarray1[0] == 'B'):
        output_lbl = "Bronchiectasis"
    elif (myarray1[0] == 'H'):
        output_lbl ="HANTA VIRUS"
    elif (myarray1[0] == 'L'):
        output_lbl ="LUNG CANCER"
    elif (myarray1[0] == 'P'):
        output_lbl="PNEUMONIA"
    elif (myarray1[0] == 'A'):
        output_lbl ="Asthma"
    elif (myarray1[0] == 'E'):
        output_lbl = "Emphysema"

    label_output.config(text= "Lung Diease....." + str(output_lbl))


    load = Image.open(fileName)
    render = ImageTk.PhotoImage(load)
    img = tk.Label(tab3, image=render, height="250", width="500")
    img.image = render
    img.place(x=0, y=0)
    img.grid(column=0, row=1, padx=10, pady = 10)
   # title.destroy()
    #button1.destroy()




    def clearfield():
        img.destroy()

    button4 = tk.Button(tab3, text="Refresh", command=clearfield)
    button4.grid(column=0, row=1, padx=10, pady=10)
    button4.place(x=10, y=520)

def SVM():
    ## NOTE: Moved sample images / data to desktop

    # Import necessary modules
    import numpy as np
    import pandas as pd
    import dicom
    import os
    import csv
    import scipy.ndimage
    import matplotlib.pyplot as plt
    import cPickle
    import cv2

    from sklearn.neural_network import MLPClassifier
    from skimage import data, feature, measure, morphology  # scikit-image
    from sklearn import svm, metrics  # scikit-learn
    import sklearn.preprocessing as pre
    from scipy import stats
    from mpl_toolkits.mplot3d.art3d import Poly3DCollection  # 3d-plotting

    import warnings
    import skfuzzy as fuzz
    warnings.simplefilter("ignore", DeprecationWarning)

    INPUT_SCAN_FOLDER = '../../../../Desktop/larger_balanced_sample_preprocessed/'
    OUTPUT_FOLDER = '../../../../Desktop/larger_balanced_sample_preprocessed/'

    # Define related constants
    # GROUND_TRUTH = 'stage1_labels.csv'
    GROUND_TRUTH = '/Volumes/My Passport for Mac/larger_sample_patient_truths.csv'
    patients = os.listdir(INPUT_SCAN_FOLDER)
    patients.sort()

    def show_slice(arr, value_range=None):
        if len(list(arr.shape)) > 2:
            arr2 = arr.copy()
            arr2 = np.reshape(arr, (arr.shape[0], arr.shape[1]))
        else:
            arr2 = arr

        dpi = 80
        margin = 0.05  # (5% of the width/height of the figure...)
        xpixels, ypixels = arr2.shape[0], arr2.shape[1]

        # Make a figure big enough to accomodate an axis of xpixels by ypixels
        # as well as the ticklabels, etc...
        figsize = (1 + margin) * ypixels / dpi, (1 + margin) * xpixels / dpi

        fig = plt.figure(figsize=figsize, dpi=dpi)
        # Make the axis the right size...
        ax = fig.add_axes([margin, margin, 1 - 2 * margin, 1 - 2 * margin])

        if value_range is None:
            plt.imshow(arr2, cmap=plt.cm.gray)
        else:
            ax.imshow(arr2, vmin=value_range[0], vmax=1, cmap=plt.cm.gray, interpolation='none')
        plt.show()

    def load_scan_data(patientid):
        data = np.load(OUTPUT_FOLDER + patientid + '.npz')['arr_0']
        return data

    def calculate_lbp(slice_data, numPoints, numNeighbors, radius, eps=1e-7):
        lbp_data = feature.local_binary_pattern(slice_data, numPoints, radius, method="uniform")
        n_bins = numPoints + 2
        (hist_data, _) = np.histogram(lbp_data.ravel(), bins=np.arange(0, n_bins + 1), range=(0, n_bins))

        # Currently assuming last point in histogram is most frequent, getting rid of it (represents grey matter)
        hist_data = hist_data[:-1]

        # Normalize the histogram
        hist_data = hist_data.astype("float")
        hist_data /= (hist_data.sum() + eps)

        return hist_data

    def perform_lbp(scan_data, slice_center=80):

        # Define base/center slice
        base_slice = scan_data[slice_center]
        output_training_data = []

        # Create LBPs and histograms for every other slice, centered around the base slice upto 10 either side
        for i in range(len(scan_data)):
            if i <= 10 and i % 2 == 0:

                # Create LBP vector
                radius = 3
                numNeighbors = 8
                numPoints = numNeighbors * radius

                # Create LBP for base slice
                if i == 0:
                    base_slice = np.squeeze(base_slice)
                    hist_data = calculate_lbp(base_slice, numPoints, numNeighbors, radius)
                    output_training_data.append(hist_data)

                # Create LBP for other slices (plus and minus)
                else:
                    data_slice_plus = np.squeeze(scan_data[80 + i])
                    data_slice_minus = np.squeeze(scan_data[80 - i])

                    hist_data_plus = calculate_lbp(data_slice_plus, numPoints, numNeighbors, radius)
                    hist_data_minus = calculate_lbp(data_slice_minus, numPoints, numNeighbors, radius)

                    output_training_data.append(hist_data_plus)
                    output_training_data.append(hist_data_minus)

        return output_training_data

    # Main function: Applies above preprocessing steps to all the data (only needs to be done offline once)
    def main():
        dicom_folder_list = [name.split('.')[0] for name in os.listdir(INPUT_SCAN_FOLDER)]

        # Store ground truths
        with open(GROUND_TRUTH, 'rb') as ground_truth_file:
            reader = csv.reader(ground_truth_file)
            data_listed = list(reader)

        truth_list_sample_sorted = []
        truth_list_patients = [data_listed[i][0] for i in range(1, len(data_listed))]
        truth_list_truths = [data_listed[i][1] for i in range(1, len(data_listed))]
        for i in range(len(dicom_folder_list)):
            try:
                truth_index = truth_list_patients.index(truth_list_patients[i])
                truth_list_sample_sorted.append(int(truth_list_truths[truth_index]))
            except Exception as e:
                print(e)
                if dicom_folder_list[i] != '.DS_Store':
                    truth_list_sample_sorted.append(
                        0)  # for patients not in the data set, assume a ground truth of zero

        # Initialize Training Set
        training_data_set = []
        training_truths_set = []

        for i in range(len(dicom_folder_list)):
            print(dicom_folder_list[i])
            data = load_scan_data(dicom_folder_list[i])
            hist_data = perform_lbp(data)
            training_data_set.append(hist_data)
            print(i)
            training_truths_set.append([truth_list_sample_sorted[i]] * len(hist_data))

        # Calculate Similarity via Chi Squared Distance (a smaller distance -> greater similarity)
        chi_predictions = []
        for patient_number in range(len(training_data_set)):
            current_patient = training_data_set[patient_number]
            remaining_data = [x for i, x in enumerate(training_data_set) if i != patient_number]
            remaining_truth = [x for i, x in enumerate(truth_list_sample_sorted) if i != patient_number]

            similarities = []
            for remaining_patient_num in range(len(remaining_data)):
                patient = remaining_data[remaining_patient_num]
                chi_vals = []
                for hist_count in range(len(patient)):
                    test = stats.chisquare(current_patient[hist_count], patient[hist_count])
                    chi_vals.append(test[0])

                avg = np.mean(chi_vals)
                similarities.append(avg)

            chi_predictions.append(remaining_truth[similarities.index(min(similarities))])

        # Output Metrics for Chi Squared Distance Based Approach
        log_loss_error = metrics.log_loss(truth_list_sample_sorted, chi_predictions)
        print("Predictions")
        print(chi_predictions)
        print("Truth")
        print(truth_list_sample_sorted)
        print("Log Loss Error: " + str(log_loss_error))

        correct_count = 0
        total_neg_count = 0
        total_pos_count = 0
        false_pos_count = 0
        false_neg_count = 0

        # Calculate metrics
        for i in range(len(chi_predictions)):
            if chi_predictions[i] == truth_list_sample_sorted[i]:
                correct_count += 1
            elif chi_predictions[i] == 1 and truth_list_sample_sorted[i] == 0:
                false_pos_count += 1
            elif chi_predictions[i] == 0 and truth_list_sample_sorted[i] == 1:
                false_neg_count += 1
            if truth_list_sample_sorted[i] == 0:
                total_neg_count += 1
            elif truth_list_sample_sorted[i] == 1:
                total_pos_count += 1

        # Output metrics to console
        print("Number of False Positives: " + str(false_pos_count))
        print("Number of False Negatives: " + str(false_neg_count))
        print("False Positive Rate: " + str(float(false_pos_count) / float(total_neg_count) * 100) + "%")
        print(
            "Overall Percent Accuracy: " + str(float(correct_count) / float(len(truth_list_sample_sorted)) * 100) + "%")

    # Run main function if script is called independantly and explicitly
    if __name__ == "__main__":
        main()

    message = tk.Label()

quitWindow = tk.Button(root, text="Quit", command=root.destroy, width=5, height=1,
                       activebackground="Red", font=('times', 8,' bold '))
quitWindow.place(x=900, y=0.1)

frame3 = tk.LabelFrame(tab3, text="Detection", width=980, height=500, bd=5)
#frame2 = tk.LabelFrame(tab2, text="Alexnet", width=980, height=500, bd=5)
frame1 = tk.LabelFrame(tab1, text="Lung Cancer  Breath mothion Detection python", width=980, height=500, bd=5, )

frame1.grid(row=0, column=0, columnspan=2, padx=8)
#frame2.grid(row=0, column=0, columnspan=2, padx=8)
frame3.grid(row=0, column=0, columnspan=2, padx=8)

frame1.place(x=10, y=10)
#frame2.place(x=10, y=10)
frame3.place(x=10, y=10)






#dispay output for detection
label_output=tk.Label(tab3, text='Output')   #, height="20", width="10")
label_output.grid(column=0, row=2,padx=10, pady = 10)
label_output.place(x=300,y=520)

#get photo for detection
button1 = tk.Button(tab3, text="Get Photo", command = openphoto)
button1.grid(column=0, row=1, padx=10, pady = 10)
button1.place(x=150,y=520)

#buttons for preprocess


root.mainloop()
