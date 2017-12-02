import requests

class Respuestas():
	def saluda(self, sender_id):
		JSON = {"messaging_type":"RESPONSE",
		"recipient":{
		"id":sender_id
		},
		"message":{
		"text":"Saludo"
			}
		}

		URL = "https://graph.facebook.com/v2.6/me/messages?access_token=EAAFISPRZAHBMBAMcjw3xkHX8ZC1RrgJ7qD0X98JtuCZCbTnTAG3SQjCZBAMPoGCJ9553Vz59zZBzynFaEYHo3T704cxxv1AtvH5isodBcucXenS4R9oNanT1SBbUTSFw0wZBPwbbBAdXHOOOHdx92GF58YGCaDnpi4Dj0lDGOIBQZDZD"
		respuesta = requests.post(URL, json = JSON)
		return respuesta, 200

	def ir(self, sender_id):
		JSON = {"messaging_type":"RESPONSE",
		"recipient":{
		"id":sender_id
		},
		"message":{
		"text":"Tu asistencia está confirmada"
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
		"text": "Muestrame las posadas",
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

		URL = "https://f4a27278.ngrok.io/api/v1/posada"
		response = requests.get(URL)
		numero_posadas = response.json()

		lista = []
		for x in numero_posadas:
			lista.append(
			{
			'title': x['nombre'],
			'image_url': x['imagen'],
			'subtitle': x['telefono'],
			'buttons':[{'type': 'postback', 'title':'Quiero ir', 'payload': 220}]
			})

		JSON = {
		"recipient":{
		"id":sender_id
		},
		"message":{
		"attachment":{
		"type":"template",
		"payload":{
		"template_type":"generic",
		"elements": lista
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