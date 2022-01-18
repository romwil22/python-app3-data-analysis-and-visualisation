hc.options.xAxis.categories = list(average_month_course.index)
    
    # # iterate per course need to fix
    # hcData = [{"name:": v1, "data:": [v2 for v2 in average_month_course[v1]]} for v1 in average_month_course.columns] 
    # hc.options.series = hcData