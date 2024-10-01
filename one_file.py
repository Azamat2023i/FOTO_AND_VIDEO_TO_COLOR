import numpy as np
import cv2
from cv2 import dnn


def transformation(img_input_path, img_output_path):
    proto_file = 'Model/colorization_deploy_v2.prototxt'
    model_file = 'Model/colorization_release_v2.caffemodel'
    hull_pts = 'Model\pts_in_hull.npy'

    net = dnn.readNetFromCaffe(proto_file, model_file)
    kernel = np.load(hull_pts)

    img = cv2.imread(img_input_path)
    scaled = img.astype("float32") / 255.0
    lab_img = cv2.cvtColor(scaled, cv2.COLOR_BGR2LAB)

    class8 = net.getLayerId("class8_ab")
    conv8 = net.getLayerId("conv8_313_rh")
    pts = kernel.transpose().reshape(2, 313, 1, 1)
    net.getLayer(class8).blobs = [pts.astype("float32")]
    net.getLayer(conv8).blobs = [np.full([1, 313], 2.606, dtype="float32")]

    resized = cv2.resize(lab_img, (224, 224))
    L = cv2.split(resized)[0]
    L -= 50

    net.setInput(cv2.dnn.blobFromImage(L))
    ab_channel = net.forward()[0, :, :, :].transpose((1, 2, 0))
    ab_channel = cv2.resize(ab_channel, (img.shape[1], img.shape[0]))

    L = cv2.split(lab_img)[0]
    colorized = np.concatenate((L[:, :, np.newaxis], ab_channel), axis=2)

    colorized = cv2.cvtColor(colorized, cv2.COLOR_LAB2BGR)
    colorized = np.clip(colorized, 0, 1)

    colorized = (255 * colorized).astype("uint8")

    cv2.imwrite(img_output_path, colorized)
    cv2.waitKey(0)