import requests

class Respuestas():
	def saluda(self, sender_id):
		JSON = {"messaging_type":"RESPONSE",
		"recipient":{
		"id":sender_id
		},
		"message":{
		"text":"Holi333"
			}
		}

		URL = "https://graph.facebook.com/v2.6/me/messages?access_token=EAAFISPRZAHBMBAMcjw3xkHX8ZC1RrgJ7qD0X98JtuCZCbTnTAG3SQjCZBAMPoGCJ9553Vz59zZBzynFaEYHo3T704cxxv1AtvH5isodBcucXenS4R9oNanT1SBbUTSFw0wZBPwbbBAdXHOOOHdx92GF58YGCaDnpi4Dj0lDGOIBQZDZD"
		respuesta = requests.post(URL, json = JSON)
		return respuesta, 200

	def quick(self, sender_id):
		JSON = {
		"recipient":{
		"id":sender_id
		},
		"message":{
		"text": "Here's a quick reply!",
		"quick_replies":[
		{
		"content_type":"text",
		"title":"Search",
		"payload":"POSTBACK_IMAGE",
		"image_url":"https://www.anipedia.net/imagenes/caracteristicas-generales-de-los-gatos.jpg"
		},
		{
		"content_type":"location"
		},
		{
		"content_type":"text",
		"title":"Something Else",
		"payload":"POSTBACK_TEXT"
		}
		]
		}
		}

		URL = "https://graph.facebook.com/v2.6/me/messages?access_token=EAAFISPRZAHBMBAMcjw3xkHX8ZC1RrgJ7qD0X98JtuCZCbTnTAG3SQjCZBAMPoGCJ9553Vz59zZBzynFaEYHo3T704cxxv1AtvH5isodBcucXenS4R9oNanT1SBbUTSFw0wZBPwbbBAdXHOOOHdx92GF58YGCaDnpi4Dj0lDGOIBQZDZD"
		respuesta = requests.post(URL, json = JSON)
		return True, 200

	def generics(self, sender_id):
		JSON = {
		"recipient":{
		"id":sender_id
		},
		"message":{
		"attachment":{
		"type":"template",
		"payload":{
		"template_type":"generic",
		"elements":[
		{'title': 'Cotizar',
		'image_url': "https://www.anipedia.net/imagenes/caracteristicas-generales-de-los-gatos.jpg",
		'subtitle': 'Cotiza tu envío',
		'buttons':[{'type': 'postback', 'title':'Quiero cotizar', 'payload': 220}]
		},
		{'title': 'Cotizar',
		'image_url': "https://www.anipedia.net/imagenes/caracteristicas-generales-de-los-gatos.jpg",
		'subtitle': 'Cotiza tu envío',
		'buttons':[{'type': 'postback', 'title':'Quiero cotizar', 'payload': 220}]
		}
		]
		}
		}
		}
		}
		URL = "https://graph.facebook.com/v2.6/me/messages?access_token=EAAFISPRZAHBMBAMcjw3xkHX8ZC1RrgJ7qD0X98JtuCZCbTnTAG3SQjCZBAMPoGCJ9553Vz59zZBzynFaEYHo3T704cxxv1AtvH5isodBcucXenS4R9oNanT1SBbUTSFw0wZBPwbbBAdXHOOOHdx92GF58YGCaDnpi4Dj0lDGOIBQZDZD"
		send = requests.post(URL,json = JSON)
		print(send.text)
		return True, 200

	def pln(self, sender_id):
		JSON = {"messaging_type":"RESPONSE",
		"recipient":{
		"id":sender_id
		},
		"message":{
		"text":"Que desea?"
			}
		}

		URL = "https://graph.facebook.com/v2.6/me/messages?access_token=EAAFISPRZAHBMBAMcjw3xkHX8ZC1RrgJ7qD0X98JtuCZCbTnTAG3SQjCZBAMPoGCJ9553Vz59zZBzynFaEYHo3T704cxxv1AtvH5isodBcucXenS4R9oNanT1SBbUTSFw0wZBPwbbBAdXHOOOHdx92GF58YGCaDnpi4Dj0lDGOIBQZDZD"
		respuesta = requests.post(URL, json = JSON)
		return respuesta, 200