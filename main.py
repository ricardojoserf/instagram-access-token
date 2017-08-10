import sys, json, requests, os, config

def get_token(client_id, client_secret, redirect_uri, code):
	
	command = "curl \-F 'client_id="+client_id+"' \
	    -F 'client_secret="+client_secret+"' \
	    -F 'grant_type=authorization_code' \
	    -F 'redirect_uri="+redirect_uri+"' \
	    -F 'code="+code+"' \
	    https://api.instagram.com/oauth/access_token 2>/dev/null"

	resp = os.popen(command).read()

	respJson = json.loads(resp)

	try:

		access_token = respJson.get("access_token")
		if(access_token == None):
			print("ERROR: " + respJson.get("error_message") + " Get a new code and add it to the config file visiting: \n\nhttps://api.instagram.com/oauth/authorize/?client_id="+client_id+"&redirect_uri="+redirect_uri+"&response_type=code \n\nThe code is after /?code=")
			return ""

		else:
			return str(access_token)

	except:
		print("Well this was unexpected...")
		return ""


def main():

	if(config.client_id == "" or config.client_secret == ""):
		print("Using the values sys.agv[1:4], not the config.py file")
		token = get_token(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
		return
	
	else:
		print("Using the values in the config.py file")
		token = get_token(config.client_id, config.client_secret, config.redirect_uri, config.code)

	if(token != ""):
		print("ACCESS TOKEN = "+token+"")

if __name__ == "__main__":
    main()

