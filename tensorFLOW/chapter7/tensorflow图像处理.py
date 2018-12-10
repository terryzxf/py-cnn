import sys
import tensorflow as tf
import matplotlib.pyplot as plt

pic_path = sys.path[1]
image_raw_data = tf.gfile.FastGFile(pic_path+'/path/picture/', 'r').read()

with tf.Session as sess:
    img_data = tf.image.decode_jpeg(image_raw_data)

    print(img_data)

    plt.imshow(img_data)
    plt.show()

    encoded_image = tf.image.encode_jpeg(img_data)

with tf.gfile.GFile('/path/output/', 'wb') as f:
    f.write(encoded_image.eval())