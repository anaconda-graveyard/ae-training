# House Price Prediction Application

This is an example workflow for training a model in scikit-learn on house price
data, writing a predictor function (`predict.py`), and developing a simple
Tornado web server application to query the predictor function.

## Tasks

**Deploy Model**

* Deploy the model and generate predictions with different inputs
* Determine the variable(s) with the highest impact on the selling price of the
  house

**Examine Model**

* Change the default editor to JupyterLab in the project settings
* Run the `train.ipynb` notebook, check the accuracy of the model
* Examine the contents of `main.py`, `predict.py`, `static/index.html`, and
  `static/app.js`
* Review the data in the `data/` directory
* Review the dependencies in `anaconda-project.yml`

**Make Changes to Model**

* Change the `alpha` parameter of the Lasso model from 1 to 0.0001 and compare
  the accuracy
* Train, fit, and serialize the model using the notebook `train.ipynb`
* Add fields for the `OverallQual` and `YearBuilt` features by uncommenting code
  in:
  * PredictHandler class in `main.py`
  * HTML form in the `House Information` section of `static/index.html`
* Commit changes to the serialized model and application template

**Redeploy Model**

* Redeploy the new model version with modified parameters and fields
* Determine the impact of the new variables on the selling price of the house
* Describe some limitations of the current version of the model
