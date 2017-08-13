import argparse

def get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('-i', '--client_id', required=True, action='store', help='App Client_id')  
	parser.add_argument('-s', '--client_secret', required=True, action='store', help='App Client_secret')  
	parser.add_argument('-r', '--redirect_uri', required=True, action='store', help='App Redirect_uri')  
	parser.add_argument('-c', '--code', required=True, action='store', help='App Code')
	my_args = parser.parse_args()
	return my_args
 