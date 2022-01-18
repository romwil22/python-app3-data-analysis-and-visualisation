from optparse import Option
import justpy as jp
import pandas
from datetime import datetime
from pytz import utc

data = pandas.read_csv("reviews.csv", parse_dates = ["Timestamp"])
data["Weekday"] = data["Timestamp"].dt.strftime("%A")
data["Numeric_day"] = data["Timestamp"].dt.strftime("%w")
average_weekday = data.groupby(["Weekday", "Numeric_day"]).mean()
average_weekday = average_weekday.sort_values("Numeric_day")


chart_def = """
 {
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Aggregated average ratings by day of the week'
    },
    subtitle: {
        text: 'According to the Course Reviews Dataset'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Date'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Rating'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Average Rating',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
"""

def app():
    web_page = jp.QuasarPage()
    h1 = jp.QDiv(a=web_page, text="Analysis of course reviews", classes="text-h2 text-weight-bold text-center q-pa-lg")
    hc = jp.HighCharts(a=web_page, options=chart_def)
    
    hc.options.xAxis.categories = list(average_weekday.index.get_level_values(0))
    hc.options.series[0].data = list(average_weekday["Rating"])
    
    return web_page

jp.justpy(app)