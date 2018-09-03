# House Price Prediction Application

This is an example workflow for training a model in xgboost on house price data,
writing a predictor function (`predict.py`), and developing a simple tornado
web server application to query the predictor function.

## Tasks

*Initial Model*

* Run the `train.ipynb` notebook, check the accuracy of the model
* Train and pickle the model using the notebook `train.ipynb`, then commit the
  serialized model
* Deploy the application and generate predictions with different inputs
* Determine the variable(s) with the highest impact on the selling price of the house

*Changes to Model*

* Add fields for the `OverallQual` and `YearBuilt` features by uncommenting code
  in:
  * PredictHandler class in `main.py`
  * HTML form in the `House Information` section of `static/index.html`
* Change the `alpha` parameter of the Lasso model to 0.0001 and compare the
  accuracy

*Redeploy model*

* Redeploy the application with the new model parameter and fields
* Determine the impact of the new variables on the selling price of the house
