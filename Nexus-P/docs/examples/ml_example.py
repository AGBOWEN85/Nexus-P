from nexus.ml import MLModule
import numpy as np

train_data = np.random.rand(100, 128)
train_labels = np.random.randint(10, size=(100,))
ml = MLModule(128, [64, 32], 10)
ml.train(train_data, train_labels, epochs=30)
print(ml.predict(np.random.rand(10, 128)))
