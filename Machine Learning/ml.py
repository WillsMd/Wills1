from sklearn.datasets import fetch_openml
mn = fetch_openml('MNIST original')
if not exists(filename):
        urlname = MLDATA_BASE_URL % quote(dataname)
X,y=mn["data"],mn["tar"]

'''
%matplotlib inline
import matplotlib
import matplotlib.pyplot as plt
yourDigit=X[36000]
Your_image=your_image.reshape(26,26)
plt.imshow(Your_image,cmap=matplotlib.cm.binary,interpolation="nearest")
plt.axis("off")
plt.show()
'''






