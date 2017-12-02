#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request
import requests
from respuestas import Respuestas

app = Flask(__name__)

ACCESS_TOKEN = 'EAAFISPRZAHBMBAMcjw3xkHX8ZC1RrgJ7qD0X98JtuCZCbTnTAG3SQjCZBAMPoGCJ9553Vz59zZBzynFaEYHo3T704cxxv1AtvH5isodBcucXenS4R9oNanT1SBbUTSFw0wZBPwbbBAdXHOOOHdx92GF58YGCaDnpi4Dj0lDGOIBQZDZD'
VERIFY_TOKEN = 'cintaroja'

@app.route('/')
def home():
	return 'Inicio de servidor'

@app.route('/webhook', methods = ['GET','POST'])
def webhook():
	if request.method == 'POST':
		mensaje = request.json
		print(mensaje)

		for evento in mensaje['entry']:
			messaging = evento['messaging']
			for event_message in messaging:
				sender_id = event_message['sender']['id']
				try:
					message = event_message['message']['text']
					pln = event_message['message']['nlp']['entities']['intent'][0]['value']
				except:
					message = "HOLA"

				print(message + ' por ' + sender_id + str(pln))
				respuestas = Respuestas()
				
				if message.upper() == 'HOLA':
					respuestas.saluda(sender_id)
				elif message.upper() == 'QUICK':
					respuestas.quick(sender_id)
				elif message.upper() == 'GENERIC':
					respuestas.generics(sender_id)
				elif pln.upper() == 'QUIERO':
					respuestas.pln(sender_id)
		return 'ok'

	elif request.method == 'GET':
		if request.args.get('hub.verify_token') == VERIFY_TOKEN:
			return request.args.get('hub.challenge')
		return 'Verificar Token'


if __name__ == '__main__':
	app.run(port = 5000, debug = True)