**JOAS Journal Paper 2024**

Open access data and codes to reproduce publication's results

The codes and datasets provided are part of the submission to the JOAS Journal 2024. The raw data were collected from open-source database of historical flights; Opensky Network.

Please note, that some of the datasets provided were split into a number of smaller datasets to comply with GitHub data size requirements. The datasets were split based on either the time (weeks of month) or the position (runways).

To have the codes run properly, make sure you have installed the following packages in your Python IDE: matplotlib.pyplot, numpy, os, pandas, pyproj, and shapely.

Before running the code, you need to specify/change path to the input/output data.

We advice to run and understand the study on the small example first in order to be able to reproduce the whole study.

The directory contains example codes for determining runways, calculation of PM Utilization in percent, and example codes to plot PM and non-PM trajectories. The Outputs folder is prepared for outputs from the scripts. The PM Datasets folder contains flight trajectories adhering to the PM systems at studied airports. The PM flights from full data folder contains codes on how to extract PM andhering trajectories from full dataset. Input for these codes needs to be downloaded from the OpenSky historical database individually. The PM utilization calculation folder contains codes to calculate the PM utilization at each of the studied airports.

--------------------
**SMALL EXAMPLE**
-------------------
For better understanding of our analysis, we prapared smaller example with reduced time period analysis for one of the studied airports. Follow read_me.txt instructions in the corresponding folder to run the example.
