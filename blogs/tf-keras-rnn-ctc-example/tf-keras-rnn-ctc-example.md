# Cách thực hiện loss ctc bằng cách sử dụng tensorflow keras (Ví dụ CRNN)
Code: sử dụng tensorflow 1.14

```python
# train.py
model, label_length_ts, pred_length_ts, y_true_input_ts= build_model_v1(config["model_input_w"], config["model_input_h"], config["model_input_ch"], class_size, max_str_len)
ctc_loss_prepare_fn = functools.partial(ctc_loss, input_length=pred_length_ts, label_length=label_length_ts, real_y_true_ts=y_true_input_ts)
model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.0001), loss=ctc_loss_prepare_fn)
```

<details>
  <summary>build_model.py, Xem Code:</summary>
  
```python
# build_model.py

def build_model_v1(input_width, input_height, input_channels, class_size, max_str_len):
    """
    :param input_width:
    :param input_height:
    :param input_channels:
    :param class_size: including pseudo blank
    :return:
    """
    input = tf.keras.layers.Input((input_height, input_width, input_channels),name="img_input")
    label_length_input = tf.keras.layers.Input((1,),name="label_length_input")
    pred_length_input = tf.keras.layers.Input((1,),name="pred_length_input")
    y_true_input = tf.keras.layers.Input((max_str_len,), name="y_true_input")
    output = conv_bn_actv(input, 8, (5,5), 1, name="down_0")
    output = tf.keras.layers.MaxPooling2D(name="pool_0")(output)
    output = conv_bn_actv(output, 16, (5,5), 1, name="down_1")
    output = tf.keras.layers.MaxPooling2D(name="pool_1")(output)
    output = conv_bn_actv(output, 32, (3,3), 1, name="down_2")
    output = conv_bn_actv(output, 64, (3,1), 1, name="down_3")
    print(output.shape)
    conv_out_flatten = tf.keras.layers.Reshape((output.shape[2], output.shape[3]))(output)
    output = conv_out_flatten

    # create rnn
    output = tf.keras.layers.CuDNNLSTM(100, return_sequences=True, name="lstm_0")(output)
    output = tf.keras.layers.CuDNNLSTM(100, return_sequences=True, name="lstm_1")(output)
    output = tf.keras.layers.TimeDistributed(tf.keras.layers.Dense(class_size, activation="linear"), input_shape=output.shape, name="timedist_dense")(output)
    y_pred = tf.keras.layers.Softmax()(output)
    model = tf.keras.Model(inputs=[input, pred_length_input, label_length_input, y_true_input],outputs=y_pred)
    return model, label_length_input, pred_length_input, y_true_input
```

</details>

<details>
  <summary>ctc_loss.py, Xem Code:</summary>
  

```python
# ctc_loss.py
import tensorflow as tf
def ctc_loss(y_true, y_pred, input_length, label_length, real_y_true_ts):
    return tf.keras.backend.ctc_batch_cost(real_y_true_ts, y_pred, input_length, label_length)
```
  
</details>


Các hàm   `tk.keras.backend.ctc_batch_cost` sử dụng `tensorflow.python.ops.ctc_ops.ctc_loss` có tham số `preprocess_collapse_repeated`. 
Trong một số chủ đề, nó nhận xét rằng các tham số này nên được đặt thành `True` khi hàm `tf.keras.backend.ctc_batch_cost`  dường như không hoạt động, 
chẳng hạn như `loss` không hội tụ. Tuy nhiên, kinh nghiệm của tôi là mặc dù việc đặt thông số này thành `True` có thể khiến người dùng ảo tưởng rằng loss đang giảm, 
nhưng thực tế nó không huấn luyện mô hình như người dùng dự định. Vui lòng kiểm tra tài liệu về thông số này. Đối với hầu hết các trường hợp, sử dụng 
hàm `tf.keras.backend.ctc_batch_cost` vanilla là đủ tốt. 

## Input Sequence / Label Sequence
Hai thuật ngữ này mà cứ xuất hiện trong các văn bản liên quan đến hàm và trong các bài báo thì lại rất khó hiểu. Ngay cả khi bạn có ý tưởng chung về lý do tại sao 
hai thứ đó cần được tách biệt, vẫn có một số khoảnh khắc khó hiểu khi xác định kích thước và loại tensor khi code. Tôi nghĩ điều mà hầu hết mọi người, 
bao gồm cả bản thân tôi vài ngày trước, muốn biết cuối cùng là "chính xác kích thước / loại tensor mà tôi cần truyền cho tf.keras.backend.ctc_batch_cost" là gì?

Nếu chúng ta xem các tài liệu :
[*] y_true: tensor       (batch, max_string_length) chứa các nhãn thật.
[*] y_pred: input tensor (batch, time_steps, num_categories) chứa dự đoán hoặc đầu ra của softmax.
[*] input_length: tensor (batch, 1)  chứa sequence length cho mỗi batch trong y_pred.
[*] label_length: tensor (batch, 1)  chứa sequence length cho mỗi batch trong y_true.

Ở đây tôi sẽ giải thích bằng một ví dụ.

Giả sử tôi đang train một CRNN, đó là những gì mã được trình bày ở trên đang thực hiện. Tôi có tập dữ liệu gồm 6 loại ảnh chứa văn bản:

```[ “hat”, “cat”, “mouse”, “deer”, “tensorflow”, “good” ]```

Giả sử sử dụng batch size là 2 và đầu ra của convolutional layers cho ra `25 sequences`, tức là `25 lát thời gian (time slices)` sẽ được cấp cho RNN.

Giả sử lô đầu tiên được chọn [“hat”, “good”].

Trong trường hợp này, hình dạng của `y_true` phụ thuộc vào cách người dùng thiết kế việc cung cấp dữ liệu. Vì lô hiện tại có `max_str_len` là 4 (vì "good" là bốn ký tự), 
người dùng có thể cung cấp `y_true` để có hình dạng là (2,4). Hoặc vì `str_len` dài nhất trong toàn bộ tập dữ liệu là 10 (vì “tensorflow” có 10 ký tự), 
người dùng có thể cung cấp `y_true` để có hình dạng là (2,10). Miễn là các ký tự `max_string_length` được sử dụng trong y_true bằng/lớn hơn số ký tự trong từ (hoặc nhãn)
dài nhất trong lô (batch), thì không có vấn đề gì. Vì vậy, điều này đặt ra câu hỏi: “những thứ nên được điền vào ở các vị trí có thể bỏ qua trong y_true là gì?”. 
Bất cứ điều gì. Nó không quan trọng. Đặt số không hoặc -1 hoặc 73839593 nếu bạn thích. Nếu bạn xem xét kỹ hơn trong code của `tf.keras.backend.ctc_batch_cost`, 
`y_true` và `label_length` sẽ kết hợp, một sparse tensor (tensor thưa thớt) sẽ xuất hiện. Quá trình này sẽ làm cho các vị trí có thể bỏ qua trong `y_true` trở nên vô dụng.

y_pred nên có hình dạng là (2, 25, class_size). Dẫu sao, class_size là “kích thước lớp thực tế + 1” trong đó +1 là blank giả của CTC.

```
                                                    Giá trị:
y_pred:       (batch, time_steps, num_categories) = (2, 25, class_size/Number of vocab)
y_true:       (batch, max_string_length)          = (2, 4) or (2, 10)
input_length: (batch, 1) = ? 
label_length: (batch, 1) = ?
```

`input_length` sẽ có hình dạng là (2,1). Nhưng giá trị của nó phải là gì? Câu hỏi này là câu hỏi thực sự đã làm khó tôi. Nó có nên bằng `label_length`? hay nó phải 
chứa số lượng time slices? Nếu vậy thì điều này không quá rõ ràng vì số lượng time slices đã có sẵn trong đó `y_pred`? Tại sao hàm này yêu cầu 
tôi chỉ định điều này?…. Đây là những câu hỏi đã ám ảnh tôi.

Câu trả lời như sau. Mặc dù nó có vẻ kỳ lạ, các giá trị của `input_length` sẽ là [[25], [25]] trong ví dụ này. 
Nó là sự lặp lại của time slices (hoặc “sequence”) đầu ra của RNN.

`label_length` sẽ có hình dạng là (2,1) và như bạn có thể đoán, nó chứa `str_len` cho mỗi nhãn trong batch. Đối với batch ở ví dụ này, giá trị sẽ là [[3], [4]].
Tuy nhiên, tài liệu không đề cập đến một trong những quy tắc quan trọng nhất khi sử dụng ctc loss. Điều này đã được đề cập trong bài báo của CTC.

Độ dài chuỗi RNN (RNN sequence length, hoặc "number of time slices" là 25 trong ví dụ này) phải lớn hơn `( 2 * max_str_len ) + 1`. 
Ở đây `max_str_len` tính trên toàn bộ tập dữ liệu. Vì `max_str_len` trên toàn bộ tập dữ liệu trong ví dụ này là 10 (“tensorflow”) và 25> (2 * 10 + 1) là true, 
nên thiết kế được loss ctc.

```
                                                    Giá trị:
y_pred:       (batch, time_steps, num_categories) = (2, 25, class_size/Number of vocab)
y_true:       (batch, max_string_length)          = (2, 4) or (2, 10)
input_length: (batch, 1) = [[25], [25]] hoặc = [<mfcc len of “hat”>, <mfcc len of “good”> ]
label_length: (batch, 1) = [[3],  [4] ] = [[<len of "hat">],[<len of "good">]]
```

## và đây là ví dụ cụ thể:
Khai báo một layer CTC hoặc dùng loss trực tiếp cũng được.

```python
""" Cách tính number of class:
# Some configs
# Constants
SPACE_TOKEN = '<space>'
SPACE_INDEX = 0
FIRST_INDEX = ord('a') - 1  # 0 is reserved to space
# Accounting the 0th indice                + space + blank label = 28 characters
num_classes    = ord('z') - ord('a') + 1   + 1     + 1 
"""


# y_pred:       (batch, time_steps, num_categories) = (2, 25, class_size/Number of vocab)
# y_true:       (batch, max_string_length)          = (2, 4) or (2, 10)
# input_length: (batch, 1) = [[25], [25]] hoặc = [<mfcc len of “hat”>, <mfcc len of “good”> ]
# label_length: (batch, 1) = [[3],  [4] ] = [[<len of "hat">],[<len of "good">]]
import tensorflow as tf
from tensorflow.keras import layers
import tensorflow.keras as keras
import numpy as np
batch, time_steps, num_categories=2,25,26
max_string_length=10

y_pred=tf.convert_to_tensor(np.random.rand(batch, time_steps, num_categories), dtype= tf.double)
y_true=tf.convert_to_tensor(np.random.rand(batch, max_string_length)*24,dtype=tf.uint8)
input_length = tf.convert_to_tensor([[25], [25]],dtype=tf.uint8)
label_length = tf.convert_to_tensor([[4],  [4] ],dtype=tf.uint8)
# print(y_pred)
# print(y_true)
# print(input_length)
# print(label_length)
class CTCLayer(layers.Layer):
    def __init__(self, name=None):
        super().__init__(name=name)
        self.loss_fn = keras.backend.ctc_batch_cost
    def call(self, y_true, y_pred):
        # Compute the training-time loss value and add it
        # to the layer using `self.add_loss()`.
        batch_len    = tf.cast(tf.shape(y_true)[0], dtype="int64")
        input_length = tf.cast(tf.shape(y_pred)[1], dtype="int64")
        label_length = tf.cast(tf.shape(y_true)[1], dtype="int64")
        input_length = input_length * tf.ones(shape=(batch_len, 1), dtype="int64")
        label_length = label_length * tf.ones(shape=(batch_len, 1), dtype="int64")
        loss = self.loss_fn(y_true, y_pred, input_length, label_length)
        # self.add_loss(loss)
        # At test time, just return the computed predictions
        # return y_pred
        return loss
ctc=CTCLayer()
loss=ctc.call(y_true, y_pred)
print('loss1:',loss)
loss2=keras.backend.ctc_batch_cost(y_true, y_pred, input_length, label_length)
print('loss2:',loss2)
```
Kết quả nó thế này:
```python
loss1: tf.Tensor(
[[61.17607036]
 [62.00751365]], shape=(2, 1), dtype=float64)
loss2: tf.Tensor(
[[67.02553544]
 [70.40033977]], shape=(2, 1), dtype=float64)
```
## Cách dùng Layer CTC:
### Khai báo model thế này

<details>
  <summary>Xem Code:</summary>
  
```python
class CTCLayer(layers.Layer):
    def __init__(self, name=None):
        super().__init__(name=name)
        self.loss_fn = keras.backend.ctc_batch_cost

    def call(self, y_true, y_pred):
        # Compute the training-time loss value and add it
        # to the layer using `self.add_loss()`.
        batch_len    = tf.cast(tf.shape(y_true)[0], dtype="int64")
        input_length = tf.cast(tf.shape(y_pred)[1], dtype="int64")
        label_length = tf.cast(tf.shape(y_true)[1], dtype="int64")

        input_length = input_length * tf.ones(shape=(batch_len, 1), dtype="int64")
        label_length = label_length * tf.ones(shape=(batch_len, 1), dtype="int64")

        loss = self.loss_fn(y_true, y_pred, input_length, label_length)
        self.add_loss(loss)

        # At test time, just return the computed predictions
        return y_pred


def build_model():
    # Inputs to the model
    input_img = layers.Input(
        shape=(img_width, img_height, 1), name="image", dtype="float32"
    )
    labels = layers.Input(name="label", shape=(None,), dtype="float32")

    # First conv block
    x = layers.Conv2D(
        32,
        (3, 3),
        activation="relu",
        kernel_initializer="he_normal",
        padding="same",
        name="Conv1",
    )(input_img)
    x = layers.MaxPooling2D((2, 2), name="pool1")(x)

    # Second conv block
    x = layers.Conv2D(
        64,
        (3, 3),
        activation="relu",
        kernel_initializer="he_normal",
        padding="same",
        name="Conv2",
    )(x)
    x = layers.MaxPooling2D((2, 2), name="pool2")(x)

    # We have used two max pool with pool size and strides 2.
    # Hence, downsampled feature maps are 4x smaller. The number of
    # filters in the last layer is 64. Reshape accordingly before
    # passing the output to the RNN part of the model
    new_shape = ((img_width // 4), (img_height // 4) * 64)
    x = layers.Reshape(target_shape=new_shape, name="reshape")(x)
    x = layers.Dense(64, activation="relu", name="dense1")(x)
    x = layers.Dropout(0.2)(x)

    # RNNs
    x = layers.Bidirectional(layers.LSTM(128, return_sequences=True, dropout=0.25))(x)
    x = layers.Bidirectional(layers.LSTM(64, return_sequences=True, dropout=0.25))(x)

    # Output layer
    x = layers.Dense(len(characters) + 1, activation="softmax", name="dense2")(x)

    # Add CTC layer for calculating CTC loss at each step
    output = CTCLayer(name="ctc_loss")(labels, x)

    # Define the model
    model = keras.models.Model(
        inputs=[input_img, labels], outputs=output, name="ocr_model_v1"
    )
    # Optimizer
    opt = keras.optimizers.Adam()
    # Compile the model and return
    model.compile(optimizer=opt)
    return model


# Get the model
model = build_model()
model.summary()
```
  
</details>

Và cách dùng như thế này:

<details>
  <summary>Xem Code:</summary>
  
```python
epochs = 500
early_stopping_patience = 10
# Add early stopping
early_stopping = keras.callbacks.EarlyStopping(
    monitor="val_loss", patience=early_stopping_patience, restore_best_weights=True
)

# Train the model
history = model.fit(
    train_dataset,
    validation_data=validation_dataset,
    epochs=epochs,
    callbacks=[early_stopping],
)
```
  
</details>



