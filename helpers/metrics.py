def get_metric_counties(allcounties):
    records = []
    for c in allcounties:
        if c['2016']['total_population'] >= 50000:
            records.append(c)
    return records


