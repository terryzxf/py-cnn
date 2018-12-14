# 在前面的小节中已经介绍了图7-14中展示的流程图中的所有步骤。在这一小节将把这些步骤穿成一个完整的
# tensorflow来处理输入数据。一下代码给出了这个完成的程序。
import tensorflow as tf


# 创建文件列表，通过文件列表创建文件输入队列。在调研输入数据处理流程，需要同意所以原始数据的格式并将它们存储到
# TFRecord文件中，下面给出了文件列表应该包含所有提供训练数据的TFRecord。

def distort_color(image, color_ordering=0):

    if color_ordering == 0:
        image = tf.image.random_brightness(image, max_delta=32./255.)
        image = tf.image.random_saturation(image, lower=0.5, upper=1.5)
        image = tf.image.random_hue(image,max_delta=0.2)
        image = tf.image.random_contrast(image, lower=0.5, upper=1.5)

    elif color_ordering == 1:
        image = tf.image.random_saturation(image, lower=0.5, upper=1.5)
        image = tf.image.random_contrast(image, lower=0.5, upper=1.5)
        image = tf.image.random_brightness(image, max_delta=32. / 255.)
        image = tf.image.random_hue(image, max_delta=0.2)

    elif color_ordering == 2:

        image = tf.image.random_hue(image, max_delta=0.2)
        image = tf.image.random_contrast(image, lower=0.5, upper=1.5)
        image = tf.image.random_brightness(image, max_delta=32. / 255.)
        image = tf.image.random_saturation(image, lower=0.5, upper=1.5)

    elif color_ordering == 3:

        image = tf.image.random_contrast(image, lower=0.5, upper=1.5)
        image = tf.image.random_saturation(image, lower=0.5, upper=1.5)
        image = tf.image.random_hue(image, max_delta=0.2)
        image = tf.image.random_brightness(image, max_delta=32. / 255.)

    elif color_ordering == 4:

        image = tf.image.random_contrast(image, lower=0.5, upper=1.5)
        image = tf.image.random_brightness(image, max_delta=32. / 255.)

        image = tf.image.random_hue(image, max_delta=0.2)
        image = tf.image.random_saturation(image, lower=0.5, upper=1.5)

    elif color_ordering == 5:

        image = tf.image.random_contrast(image, lower=0.5, upper=1.5)
        image = tf.image.random_brightness(image, max_delta=32. / 255.)
        image = tf.image.random_hue(image, max_delta=0.2)
        image = tf.image.random_saturation(image, lower=0.5, upper=1.5)

    elif color_ordering == 6:

        image = tf.image.random_contrast(image, lower=0.5, upper=1.5)
        image = tf.image.random_hue(image, max_delta=0.2)
        image = tf.image.random_brightness(image, max_delta=32. / 255.)
        image = tf.image.random_saturation(image, lower=0.5, upper=1.5)

    return tf.clip_by_value(image, 0.0, 1.0)

def preprocess_for_train(image, height, width, bbox):

    if bbox is None:
        bbox = tf.constant([0.0, 0.0, 1.0, 1.0], dtype=tf.float32, shape=[1, 1, 4])

    if image.dtype != tf.float32:
        image = tf.image.convert_image_dtype(image, dtype=tf.float32)
    # print(image.shape,'*****\n', bbox.shape)
    bbox_begin, bbox_size, _ = tf.image.sample_distorted_bounding_box(tf.shape(image), bounding_boxes=bbox,
                                                                      min_object_covered=0)
    distorted_image = tf.slice(image, bbox_begin, bbox_size)

    distorted_image = tf.image.resize_images(
        distorted_image, [height, width], method=np.random.randint(4)
    )

    distorted_image = tf.image.random_flip_left_right(distorted_image)
    distorted_image = distort_color(distorted_image, np.random.randint(2))

    return distorted_image


files = tf.train.match_filenames_once('/path/to/file_pattern-*')
filename_queue = tf.train.string_input_producer(files, shyffle=False)

reader = tf.TFRecordReader()
_, serialized_example = reader.read(filename_queue)
features = tf.parse_single_example(
    serialized_example,
    features={
        'image':tf.FixedLenFeature([], tf.string),
        'label':tf.FixedLenFeature([], tf.int64),
        'height':tf.FixedLenFeature([], tf.int64),
        'width':tf.FixedLenFeature([], tf.int64),
        'channels':tf.FixedLenFeature([], tf.int64)
    }
)

image, label = features['image'],features['label']
height, width = features['height'],features['width']
channels = features['channels']

decoded_image = tf.decode_raw(image,tf.uint8)
decoded_image.set_shape([height,width,channels])

image_size =299

distortde_imge = preprocess_for_train(decoded_image, image_size, image_size, None)


min_after_dequeue = 10000
batch_size = 100
capacity = min_after_dequeue+3*batch_size
image_batch, label_batch = tf.train.shuffle_batch([distorted_image, label],
                                                  batch_size=batch_size, capacity=capacity,
                                                  min_after_dequeue=min_after_dequeue)

logit = inference(image_batch)
loss = calc_loss(logit, label_batch)
train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)

with tf.Session() as sess:
    tf.initialize_all_variables().run()
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)

    for i in range(TRAINING_ROUDNS):
        sess.run(train_step)
    coord.request_stop()
    coord.join(threads)