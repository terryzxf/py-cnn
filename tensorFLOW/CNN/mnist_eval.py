import  time,sys
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import  mnist_inference
import  mnist_train

EVAL_INTERVAL_SECS = 10

def evaluate(mnist):
    with tf.Graph().as_default() as g:
        x = tf.placeholder(tf.float32, [mnist_train.BATCH_SIZE, mnist_inference.IMAGE_SIZE, mnist_inference.IMAGE_SIZE,
                                        mnist_inference.NUM_CHANNELS], name='x-input')
        y_ = tf.placeholder(
            tf.float32, [None, mnist_inference.OUTPUT_NODE], name='y-input'
        )

        y = mnist_inference.inference(x, None, None)

        correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))

        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

        variable_averages = tf.train.ExponentialMovingAverage(
            mnist_train.MOVING_AVERAGE_DECAY
        )

        variable_to_restore = variable_averages.variables_to_restore()

        saver = tf.train.Saver(variable_to_restore)

        while True:
            with tf.Session() as sess:
                print(mnist_train.MODEL_SAVE_PATH)
                ckpt = tf.train.get_checkpoint_state(
                    mnist_train.MODEL_SAVE_PATH
                )
                if ckpt and ckpt.model_checkpoint_path:
                    saver.restore(sess, ckpt.model_checkpoint_path)

                    global_step = ckpt.model_checkpoint_path.split('/')[-1].split('-')[-1]

                    validate_feed = {x: mnist.validation.images, y_: mnist.validation.labels}

                    accuracy_score =sess.run(accuracy, feed_dict=validate_feed)

                    print("After %s training steps, validation" "accuracy = %g " % (global_step, accuracy_score))
                else:
                    print("No checkpoint file found")

                    return
            time.sleep(EVAL_INTERVAL_SECS)
def main(argv=None):

    mnist = input_data.read_data_sets(sys.path[0]+'/MNIST_data/', one_hot=True)
    evaluate(mnist)

if __name__ == '__main__':
    tf.app.run()