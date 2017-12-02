import requests

class Respuestas():
    def saluda(self,sender_id):
        JSON = {"messaging_type": "RESPONSE",
        "recipient":{
          "id":1577835825621329
        },
        "message":{
          "text":"Te quiero <3"
        }
        }

        URL = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAACGb9y3susBAAGABRW3zyQaS2feCL86IHN6131UaojVY1U6Nusa2PhRejBRULFt8JGKT5f2qRZCjlWjTQC3xAwpS1KcvcsheT1aaqQW8OD0cmH5SF4vXACTcExU8VJMlg2ZBpn30LtgYBBhS78gmhIU94ZBtXwAt7h2SfOuw8nAaRvzqnX'
        respuesta = requests.post(URL, json = JSON)
        print(respuesta)

    def quick(self,sender_id):



        JSON = {
          "recipient":{
            "id":sender_id
          },
          "message":{
            "text": "Hola, ¿Quiéres ir a una posada?",
            "quick_replies":[

              {
                "content_type":"text",
                "title":"Si",
                "payload":"asistira"
              }
            ]
          }
        }
        URL = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAACGb9y3susBAAGABRW3zyQaS2feCL86IHN6131UaojVY1U6Nusa2PhRejBRULFt8JGKT5f2qRZCjlWjTQC3xAwpS1KcvcsheT1aaqQW8OD0cmH5SF4vXACTcExU8VJMlg2ZBpn30LtgYBBhS78gmhIU94ZBtXwAt7h2SfOuw8nAaRvzqnX'
        respuesta = requests.post(URL, json = JSON)
        print(respuesta)
        return True

    def generic(self,sender_id):

        BASE_URL = "https://f4a27278.ngrok.io"
        URI = "/api/v1/posada"
        URL = BASE_URL + URI

        response = requests.get(URL)
        numero_posadas = response.json()

        lista_posada = []
        for posada in numero_posadas:
            lista_posada.append(
            {
            'title': posada['nombre'],
            'image_url': posada['imagen'],
            'subtitle': posada['telefono'],
            'buttons':[{'type': 'postback', 'title':'Asistiré', 'payload': 220}]
            }
            )
            print("-----------------------------------------")
            print(posada)

        JSON = {
          "recipient":{
            "id":sender_id
          },
          "message":{
            "attachment":{
              "type":"template",
              "payload":{
                "template_type":"generic",
                "elements":lista_posada
              }
            }
          }
        }


        URL = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAACGb9y3susBAAGABRW3zyQaS2feCL86IHN6131UaojVY1U6Nusa2PhRejBRULFt8JGKT5f2qRZCjlWjTQC3xAwpS1KcvcsheT1aaqQW8OD0cmH5SF4vXACTcExU8VJMlg2ZBpn30LtgYBBhS78gmhIU94ZBtXwAt7h2SfOuw8nAaRvzqnX'
        respuesta = requests.post(URL, json = JSON)
        print(respuesta)
