import requests

def get_mail():
	url = "https://10minutemail.net/"
	try:
		driver_mail.get(url)
		time.sleep(0.5)
		element = driver_mail.find_element_by_xpath('//*[@class="mailtext"]')
		return  element.get_attribute("value")
	except:
		print "error"
		
		print "get mail..."
	mail = get_mail()
	print "get mail : "+mail
