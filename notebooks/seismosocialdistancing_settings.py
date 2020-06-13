# ## Settings for this repository
#

import pandas as pd
from obspy import UTCDateTime


# Set these values to control the notebook behaviour

# Make sure you take at least a full week (>=7 days) before the first "ban"
start = UTCDateTime("2019-12-01")

# Leaving UTCDateTime() empty means "now":
# and this means 24 hours ago: UTCDateTime() - 24*3600
end = UTCDateTime() - 24*3600 


# This is the time it takes to be sure the data that we download is a complete record that
# we can reliably cache in the archive
safety_window = pd.Timedelta('2 days')

network = "S1"
station = "AUUHS"              #,sydney,brisbane jump, adelaide," # Urban stations
location = "*"
channel = "HHZ"
dataset = "AuSiS_Ulladulla"
time_zone = "Australia/Sydney"
sitedesc = "Ulladulla High School, NSW"

data_provider = "http://auspass.edu.au:8080"
logo = None 
bans = {
        "2020-01-28 00:00":"End of School Summer Holiday",
        "2020-03-18 00:00":'No Large Gatherings',
        "2020-03-25 12:00":'Restaurants/Bars/Schools closed',
        }


reference = {"start": "2020-01-28 00:00",
              "end":  "2020-03-18 00:00"}

summer_hol = {"start":"2019-12-20 00:00",
              "end":  "2020-01-28 00:00"}

lockdown   = {"start":"2020-03-19 00:00",
              "end":  "2020-06-01 00:00"}

reopening    = {"start":"2020-06-01 00:00"}
