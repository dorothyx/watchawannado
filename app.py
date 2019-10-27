from eventbrite import Eventbrite
from tok import secret
from datetime import datetime
import pprint

token = secret()
eventbrite = Eventbrite(token)
pp = pprint.PrettyPrinter(indent=4)

user = eventbrite.get_user()  # Not passing an argument returns yourself
print(user["id"])
print(user["name"])

def eb_api_query():
	# dictionary keys of argument are the fields we care about
	argument = {}

	# do something like this...
	argument["location.address"] = "Berkeley"
	argument["start_date.range_start"] = "2019-09-29T00:00:00"

	#this line is to expand the venue field (necessary to retrieve address)
	argument["expand"] = "venue"

	events = eventbrite.event_search(**argument)['events']

	#populate this dictionary with info from the search
	ret_events = []
	for event in events: 
		curr = {}
		curr['name'] = event['name']['text']
		curr['url'] = event['url']
		curr['description'] = event['description']['text']
		curr['date'] = event['start']['local']
		curr['image'] = event['logo']['original']['url']
		curr['location'] = event['venue']['address']
		ret_events.append(event)

	return ret_events



   

    

eb_api_query()
