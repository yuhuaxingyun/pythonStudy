
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tensorflow as tf

message = tf.constant('Welcome to the exciting world of Deep Neural Networks!')

with tf.Session() as sess:
    print(sess.run(message).decode())



