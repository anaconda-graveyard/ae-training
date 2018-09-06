**Dash Oil and Gas Demo App**

This is a demo of the Dash interactive Python framework developed by [Plotly](https://plot.ly/).

Dash abstracts away all of the technologies and protocols required to build an interactive web-based application and is a simple and effective way to bind a user interface around your Python code.

To learn more check out our [documentation](https://plot.ly/dash).

The following are screenshots for the app in this repo:

![Alt desc](https://cdn.rawgit.com/plotly/dash-oil-and-gas-demo/master/screenshots/Screenshot1.png?token=AK-nZHRzEppiigN44Y5izDQcSc35cqIiks5ZUq4zwA%3D%3D)

## Tasks:

**Deploy and Examine Dashboard**

* Deploy oil and gas dashboard
* Examine the contents of `app.py`, `controls.py`, and `points.py`
* Review the data in the `data/` directory
* Review the dependencies in `anaconda-project.yml`
* Explore the data set by changing variables in the dashboard

**Modify Dashboard**

* Make the following changes to the dashboard via the `app.py` file:
  * Change default year range to last 10 years of data from (1990-2010) to
    (2007-2017). This should be changed in the `update_year_slider` function!
  * Change default well status filter from "Active only" to "All"
  * Modify the mapbox to be centered on latitude 42.54, longitude -78.05
* Commit the changes to the dashboard application:
  * Enter `0.2.0` as the commit message and tag, then click the "Commit" button

**Redeploy Dashboard**

* Redeploy the modified dashboard version
* Review the impact of the modifications in the deployed dashboard
