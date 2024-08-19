from exponential_regression.repository.exponential_regression_repository import ExponentialRegressionRepository

import numpy as np
from sklearn.linear_model import LinearRegression


class ExponentialRegressionRepositoryImpl(ExponentialRegressionRepository):
    def regressionAnalysis(self, X, y):
        print("regressionAnalysis()")

        log_y = np.log(y)
        model = LinearRegression()
        model.fit(X[:, np.newaxis], log_y)

        X_new = np.linspace(1, 100, 100)
        y_pred = np.exp(model.predict(X_new[:, np.newaxis]))

        result = {
            'original_data': list(map(lambda x: [int(x[0]), float(x[1])], zip(X, y))),
            'predicted_data': list(map(lambda x: [float(x[0]), float(x[1])], zip(X, y_pred))),
            'coefficient': model.coef_.tolist(),
            'intercept': float(model.intercept_)
        }

        return result
