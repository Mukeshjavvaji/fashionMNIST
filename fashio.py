{
 "metadata": {
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.2-final"
  },
  "orig_nbformat": 2,
  "kernelspec": {
   "name": "python3",
   "display_name": "Python 3.8.2 64-bit",
   "metadata": {
    "interpreter": {
     "hash": "46a1ca3275d84fb8537616ab8d26e06a9f48532a31c6b949fb83418fa691db83"
    }
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2,
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "from matplotlib import pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [],
   "source": [
    "data = pd.read_csv(\"D:/AIML/Image classification/Apparel/train_data/fashion-mnist_train.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "       label  pixel1  pixel2  pixel3  pixel4  pixel5  pixel6  pixel7  pixel8  \\\n",
       "0          2       0       0       0       0       0       0       0       0   \n",
       "1          9       0       0       0       0       0       0       0       0   \n",
       "2          6       0       0       0       0       0       0       0       5   \n",
       "3          0       0       0       0       1       2       0       0       0   \n",
       "4          3       0       0       0       0       0       0       0       0   \n",
       "...      ...     ...     ...     ...     ...     ...     ...     ...     ...   \n",
       "59995      9       0       0       0       0       0       0       0       0   \n",
       "59996      1       0       0       0       0       0       0       0       0   \n",
       "59997      8       0       0       0       0       0       0       0       0   \n",
       "59998      8       0       0       0       0       0       0       0       0   \n",
       "59999      7       0       0       0       0       0       0       0       0   \n",
       "\n",
       "       pixel9  ...  pixel775  pixel776  pixel777  pixel778  pixel779  \\\n",
       "0           0  ...         0         0         0         0         0   \n",
       "1           0  ...         0         0         0         0         0   \n",
       "2           0  ...         0         0         0        30        43   \n",
       "3           0  ...         3         0         0         0         0   \n",
       "4           0  ...         0         0         0         0         0   \n",
       "...       ...  ...       ...       ...       ...       ...       ...   \n",
       "59995       0  ...         0         0         0         0         0   \n",
       "59996       0  ...        73         0         0         0         0   \n",
       "59997       0  ...       160       162       163       135        94   \n",
       "59998       0  ...         0         0         0         0         0   \n",
       "59999       0  ...         0         0         0         0         0   \n",
       "\n",
       "       pixel780  pixel781  pixel782  pixel783  pixel784  \n",
       "0             0         0         0         0         0  \n",
       "1             0         0         0         0         0  \n",
       "2             0         0         0         0         0  \n",
       "3             1         0         0         0         0  \n",
       "4             0         0         0         0         0  \n",
       "...         ...       ...       ...       ...       ...  \n",
       "59995         0         0         0         0         0  \n",
       "59996         0         0         0         0         0  \n",
       "59997         0         0         0         0         0  \n",
       "59998         0         0         0         0         0  \n",
       "59999         0         0         0         0         0  \n",
       "\n",
       "[60000 rows x 785 columns]"
      ],
      "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>label</th>\n      <th>pixel1</th>\n      <th>pixel2</th>\n      <th>pixel3</th>\n      <th>pixel4</th>\n      <th>pixel5</th>\n      <th>pixel6</th>\n      <th>pixel7</th>\n      <th>pixel8</th>\n      <th>pixel9</th>\n      <th>...</th>\n      <th>pixel775</th>\n      <th>pixel776</th>\n      <th>pixel777</th>\n      <th>pixel778</th>\n      <th>pixel779</th>\n      <th>pixel780</th>\n      <th>pixel781</th>\n      <th>pixel782</th>\n      <th>pixel783</th>\n      <th>pixel784</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>2</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>9</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>6</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>5</td>\n      <td>0</td>\n      <td>...</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>30</td>\n      <td>43</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>1</td>\n      <td>2</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>3</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>1</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>3</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>...</th>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n    </tr>\n    <tr>\n      <th>59995</th>\n      <td>9</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>59996</th>\n      <td>1</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>73</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>59997</th>\n      <td>8</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>160</td>\n      <td>162</td>\n      <td>163</td>\n      <td>135</td>\n      <td>94</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>59998</th>\n      <td>8</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>59999</th>\n      <td>7</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n    </tr>\n  </tbody>\n</table>\n<p>60000 rows ?? 785 columns</p>\n</div>"
     },
     "metadata": {},
     "execution_count": 34
    }
   ],
   "source": [
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "data = np.array(data)\n",
    "m,n = data.shape\n",
    "np.random.shuffle(data)\n",
    "\n",
    "dev_data = data[0:1000].T\n",
    "Y_dev = dev_data[0]\n",
    "X_dev = dev_data[1:n]\n",
    "X_dev = X_dev/255.\n",
    "\n",
    "train_data = data[1000:m].T\n",
    "Y_train = train_data[0]\n",
    "X_train = train_data[1:n]\n",
    "X_train = X_train/255."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([[0.        , 0.        , 0.        , ..., 0.        , 0.        ,\n",
       "        0.        ],\n",
       "       [0.        , 0.        , 0.        , ..., 0.        , 0.        ,\n",
       "        0.        ],\n",
       "       [0.        , 0.        , 0.        , ..., 0.        , 0.        ,\n",
       "        0.        ],\n",
       "       ...,\n",
       "       [0.        , 0.        , 0.        , ..., 0.10980392, 0.        ,\n",
       "        0.        ],\n",
       "       [0.        , 0.        , 0.        , ..., 0.        , 0.        ,\n",
       "        0.        ],\n",
       "       [0.        , 0.        , 0.        , ..., 0.        , 0.        ,\n",
       "        0.        ]])"
      ]
     },
     "metadata": {},
     "execution_count": 46
    }
   ],
   "source": [
    "X_dev"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ]
}