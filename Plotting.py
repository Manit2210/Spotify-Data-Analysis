"""
Plotting shit
"""
from sklearn.model_selection import train_test_split
import file_2 as f2
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Data Preparation
# file = "spotify_revenue.csv"
# df = pd.read_csv(file)
#
# # Prepare model data point for visualization
#
# x = df.iloc[:, 2]
# y = df.iloc[:, 3]
# z = df.iloc[:, 1]


# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(x, y, y_train, marker='.', color='red')
# ax.set_xlabel("X1")
# ax.set_ylabel("X2")
# ax.set_zlabel("y")
#
# model = LinearRegression()
# model.fit(x, y_train)
# y_pred = model.predict(z)
#
# print("MAE: {}".format(np.abs(y_test - y_pred).mean()))
# print("RMSE: {}".format(np.sqrt(((y_test - y_pred) ** 2).mean())))
# coefs = model.coef_
# intercept = model.intercept_
# xs = np.tile(np.arange(61), (61, 1))
# ys = np.tile(np.arange(61), (61, 1)).T
# zs = xs * coefs[0] + ys * coefs[1] + intercept
# print("Equation: y = {:.2f} + {:.2f}x1 + {:.2f}x2".format(intercept, coefs[0],
#                                                           coefs[1]))
# ax.plot_surface(xs, ys, zs, alpha=0.5)
# plt.show()

# x_pred = np.linspace(75, 250, 10)  # range of values of ad-supported users
# y_pred = np.linspace(45, 190, 10)  # range of values for paid subscribers
# xx_pred, yy_pred = np.meshgrid(x_pred, y_pred)
# model_viz = np.array([xx_pred.flatten(), yy_pred.flatten()]).T

# Train

# ols = LinearRegression()
# model = ols.fit(x, y)
# # predicted = ols.fit(x,y).predict(model_viz)
#
# # Evaluate
#
# r2 = model.score(x, y)
#
# # Plot
#
# plt.style.use('default')
#
# fig = plt.figure(figsize=(12, 4))
#
# ax1 = fig.add_subplot(131, projection='3d')
# ax2 = fig.add_subplot(132, projection='3d')
# ax3 = fig.add_subplot(133, projection='3d')
#
# axes = [ax1, ax2, ax3]
#
# for ax in axes:
#     ax.plot(x, y, z, color='k', zorder=15, linestyle='none', marker='o', alpha=0.5)
#     ax.scatter(xx_pred.flatten(), yy_pred.flatten(), predicted, facecolor=(0, 0, 0, 0), s=20, edgecolor='#70b3f0')
#     ax.set_xlabel('Num_of_ad-supported_users in Millions', fontsize=9)
#     ax.set_ylabel('Num_of_premium_subscribers in Millions', fontsize=9)
#     ax.set_zlabel('Revenue in Millions', fontsize=12)
#     ax.locator_params(nbins=4, axis='x')
#     ax.locator_params(nbins=5, axis='x')
#
# ax1.text2D(0.2, 0.32, 'aegis4048.github.io', fontsize=13, ha='center', va='center',
#            transform=ax1.transAxes, color='grey', alpha=0.5)
# ax2.text2D(0.3, 0.42, 'aegis4048.github.io', fontsize=13, ha='center', va='center',
#            transform=ax2.transAxes, color='grey', alpha=0.5)
# ax3.text2D(0.85, 0.85, 'aegis4048.github.io', fontsize=13, ha='center', va='center',
#            transform=ax3.transAxes, color='grey', alpha=0.5)
#
# ax1.view_init(elev=28, azim=120)
# ax2.view_init(elev=4, azim=114)
# ax3.view_init(elev=60, azim=165)
#
# fig.suptitle('$R^2 = %.2f$' % r2, fontsize=20)
#
# fig.tight_layout()


dict1 = f2.read_csv('spotify_revenue.csv', 'Normal users spotify.csv',
                    'premium subscribers spotify.csv')
lst_of_coords = [dict1[item] for item in dict1]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(2, 3, 4)
for tup in lst_of_coords:
    ax.scatter(tup[0], tup[1], tup[2])

ax.set_xlabel('Premium Subscribers')
ax.set_ylabel('Ad Paying Subscribers')
ax.set_zlabel('Revenue in Millions')
