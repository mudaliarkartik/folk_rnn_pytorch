import matplotlib.pyplot as plt
plt.switch_backend('agg') 
import pickle
import numpy as np
from tensorboard.backend.event_processing.event_accumulator import EventAccumulator

event_acc = EventAccumulator('RMSProp_all_data_train_50')
event_acc.Reload()

train_loss = []
val_loss = []

for i in event_acc.scalars.Items('loss/train'):
    if(i[1] > 17000 ):
        train_loss.append(i.value)

for j in event_acc.scalars.Items('loss/eval'):
    if(j[1] > 17000 ):
        val_loss.append(j.value)

plt.plot(train_loss)
plt.plot(val_loss)
plt.title('Validation loss')
plt.ylabel('Loss')
plt.xlabel('Iteration')
plt.legend(['Train','Validation'], loc='upper left')
plt.savefig('./output/Lr0.003_rmsprop_decay_finetune_50.png')

