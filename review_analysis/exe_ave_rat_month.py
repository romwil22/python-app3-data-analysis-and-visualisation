import justpy as jp
import pandas
from datetime import datetime
from pytz import utc

data = pandas.read_csv("reviews.csv", parse_dates = ["Timestamp"])
data["Month"] = data["Timestamp"].dt.strftime("%Y-%m")
average_month = data.groupby(data["Month"]).mean()

chart_def = """
 {
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Average rating by month'
    },
    subtitle: {
        text: 'According to the Course Reviews Dataset'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Month'
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
    p1 = jp.QDiv(a=web_page, text="These graph represent course review analysis")
    
    hc = jp.HighCharts(a=web_page, options=chart_def)
    hc.options.xAxis.categories = list(average_month.index)
    hc.options.series[0].data = list(average_month["Rating"])
    
    return web_page

jp.justpy(app)