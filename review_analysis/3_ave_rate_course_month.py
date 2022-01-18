import justpy as jp
import pandas
from datetime import datetime
from pytz import utc

data = pandas.read_csv("reviews.csv", parse_dates = ["Timestamp"])
data["Month"] = data["Timestamp"].dt.strftime("%Y-%m")
average_month_course = data.groupby(["Month", "Course Name"]).mean().unstack()
print(average_month_course)


chart_def = """
{
    chart: {
        type: 'spline'
    },
    title: {
        text: 'Average fruit consumption during one week'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 150,
        y: 100,
        floating: true,
        borderWidth: 1,
        backgroundColor:
            '#FFFFFF'
    },
    xAxis: {
        categories: [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ],
        plotBands: [{ // visualize the weekend
            from: 4.5,
            to: 6.5,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Fruit units'
        }
    },
    tooltip: {
        shared: true,
        valueSuffix: ' units'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: 'John',
        data: [3, 4, 3, 5, 4, 10, 12]
    }, {
        name: 'Jane',
        data: [1, 3, 4, 3, 3, 5, 4]
    }]
}
"""

# MAKING QUASAR WEB PAGE
def app():
    web_page = jp.QuasarPage()
    h1 = jp.QDiv(a=web_page, text="Analysis of course reviews", classes="text-h2 text-weight-bold text-center q-pa-lg")
    
    hc = jp.HighCharts(a=web_page, options=chart_def)
    hc.options.xAxis.categories = list(average_month_course.index)
    
    # iterate per course need to fix
    hcData = [{"name:": v1, "data:": [v2 for v2 in average_month_course[v1]]} for v1 in average_month_course.columns] 
    hc.options.series = hcData
    
    return web_page

jp.justpy(app)