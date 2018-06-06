import altair as alt
from vega_datasets import data as vegdata
from helpers.entity import get_entities


MAP_URL = vegdata.us_10m.url



def makeprotomap():
    countydata = get_entities('county')
    data = []
    data.append(['id', 'poverty'])
    for c in countydata:
        data.append([c['id'][-5:], str(c['% Below poverty level']) ])

    counties = alt.topo_feature(vegdata.us_10m.url, 'counties')
#    unemp_data = data.unemployment.url

    datatext = [','.join(d) for d in data]


    chart = alt.Chart(counties).mark_geoshape().encode(
        color='rate:Q'
    ).transform_lookup(
        lookup='id',
        from_=alt.LookupData(datatext, 'id', ['poverty'])
    ).project(
        type='albersUsa'
    ).properties(
        width=500,
        height=300
    )

    return chart.to_dict()