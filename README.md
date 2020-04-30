# designflow_calculation
 Used for downloading peak flow data from USGS and calculating design flow for different return period

General Description:

This Python Script can be used to automatically access and download annual peak streamflow data from USGS and use the data for return period analysis.

EV1 distribution was considered in this study for calculating design flow volumes for specifically 10yr, 25yr, 50yr, 100yr, and 500yr return period.

USGS gaging station 03335500 (Wabash River at Lafayette, IN) was used as a sample station for design flow calculations, user could apply any USGS station number with available data as input for reproducing this study.

Note that url was created for accessing the data, they are multiple ways to achieve the same goal. Python package 'hydrofunctions' could be a useful tool for accessing and downloading the annual peak streamflow data and it might be worth a try.

Data Source and Software Requirements:

Streamflow data for each USGS gaging station  can be obtained from the USGS web site: https://waterdata.usgs.gov/nwis/sw/.

This script was originally written in Jupyter Notebook with anaconda 5.1 on MyGeoHub. Python 3 kernel was selected. User needs an account on MyGeohub.org to use Jupyter Notebook. However, this script should be working with python 3 on all PC's with all needed packages imported.