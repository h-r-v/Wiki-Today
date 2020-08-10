from flask import Flask
from flask.views import MethodView
from MyScraper import get_wiki_data

app = Flask(__name__)

fetch_date = 'November_30'
scraped_data = ""

class Wiki(MethodView):
    def get(self):
        return scraped_data

    def post(self, date_chosen):

        global fetch_date
        global scraped_data
        fetch_date = date_chosen
        
        scraped_data = get_wiki_data(date=fetch_date)
        print(scraped_data)
        return "DATABASE UPDATED"

wiki_view = Wiki.as_view('wiki_api')
app.add_url_rule('/wiki/<date_chosen>', methods=['POST']\
                 , view_func=wiki_view)
app.add_url_rule('/wiki', methods=['GET']\
                 , view_func=wiki_view)

if __name__=='__main__':
    app.run()

