# House price prediction app

This is an example workflow for training a model in xgboost on house price data,
writing a predictor function (`predict.py`), and developing a simple tornado
web server application to query the predictor function.

# Tasks

* Run the `train.ipynb` notebook, check the accuracy of the model
* Change the `alpha` parameter of the Lasso model to 0.0001
* Train and pickle the model using the notebook `train.ipynb`, then commit the
  serialized model
* Add fields for the `OverallQual` and `YearBuilt` features by uncommenting code in:
  * PredictHandler class in `main.py`
  * HTML form in the `House Information` section of `static/index.html`
