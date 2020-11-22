from newsapi import NewsApiClient
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    
    newsapi= NewsApiClient(api_key="47df81b865b74a16afecb6ac1acf2fd9")
    topheadlines = newsapi.get_top_headlines
     