import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
from pandas import DataFrame, Series
from sklearn import metrics

cali = fetch_california_housing()

cali_df = pd.DataFrame(cali.data, columns=cali.feature_names)

cali_df['MedHouseValue'] = pd.Series(cali.target)

X_train, X_test, Y_train, Y_test = train_test_split(
    cali.data, cali.target, random_state=11)

regress = LinearRegression()
regress.fit(X=X_train, y=Y_train)

# e = enumerate(cali.feature_names)

# for i, name in e:
#     print(f'{name:>10}: {regress.coef_[i]}')

predicted = regress.predict(X_test)
expected = Y_test
print("Multiple Linear Regression using All features:")
print(f"R2 Score: {metrics.r2_score(expected, predicted)}")
print(f"MSE Score: {metrics.mean_squared_error(expected, predicted)} \n")

e = enumerate(cali.feature_names)
for i, name in e:
    X_train, X_test, Y_train, Y_test = train_test_split(
        cali.data, cali.target, random_state=11)
    predicted = regress.predict(X_test)
    expected = Y_test
    print(f'{"Feature " + str(i):>10} has R2 Score: {metrics.r2_score(expected, predicted)}')
    print(f'{"":>10} has MSE Score: {metrics.mean_squared_error(expected, predicted)} \n')

# z = zip(predicted[::1000], expected[::1000])
# for p, e in z:
#     #print(f'predicted: {p:.2f}, expected: {e:.2f}')
#     print(f"R2 Score: {metrics.r2_score(e, p)}")
#     print(f"MSE Score: {metrics.mean_squared_error(e, p)}")

# df = pd.DataFrame()
# df['Expected'] = pd.Series(expected)
# df['Predicted'] = pd.Series(predicted)
# figure = plt.figure(figsize=(9, 9))
# axes = sns.scatterplot(data=df,
#                        x='Expected', y='Predicted')
# start = min(expected.min(), predicted.min())
# end = max(expected.max(), predicted.max())
# axes.set_xlim(start, end)
# axes.set_ylim(start, end)
# line = plt.plot([start, end], [start, end],'k--')