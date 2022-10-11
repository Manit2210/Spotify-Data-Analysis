import matplotlib.pyplot as plt
import numpy as np
import file_2 as f2
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
from sklearn.model_selection import train_test_split


from sklearn import datasets, linear_model

dict1 = f2.read_csv('spotify_revenue.csv', 'Normal users spotify.csv',
                    'premium subscribers spotify.csv')
lst_of_coords = [dict1[item] for item in dict1]

ls1 = [i[0] for i in lst_of_coords]
ls2 = [i[1] for i in lst_of_coords]

x_values, y_values = np.meshgrid(range(max(ls1)), range(max(ls2)))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for tup in lst_of_coords:
    ax.scatter(tup[0], tup[1], tup[2])


#best fit
df = pd.DataFrame(lst_of_coords)
sel_col = df[0]
target = sel_col.copy()

predictors = df.drop(columns=[0])

x_train, x_test, y_train, y_test = train_test_split(predictors, target, test_size=0.01, random_state=1)

lm = linear_model.LinearRegression()
lm.fit(x_train, y_train)
z_values = lm.predict(predictors)

ax.plot_surface(predictors[1], predictors[2], z_values)

plt.show()
