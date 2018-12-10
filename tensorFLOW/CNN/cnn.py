"""
for i in range(TRAINING_STEPS):

    xs, ys = mnist.train.next_batch(BATCH_SIZE)
    reshaped_xs = np.reshape(xs, (BATCH_SIZE,
                                  mnist_inference.IMAGE_SIZE,
                                  mnist_inference.IMAGE_SIZE,
                                  mnist_inference.NUM_CHANNELS))

    _, loss_value, step = sess.run([train_op, loss, global_step], feed_dict={x: reshaped_xs, y_: ys})

    if i % 1000 == 0:
        print("After %d training steps, loss on training" "batch is %g." % (step, loss_value))
"""
import os,sys


a= os.path.abspath(".")
print(type(a),"\n",a,'\n',sys.path)