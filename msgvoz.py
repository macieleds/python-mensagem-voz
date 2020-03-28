from __future__ import print_function
from telesign.voice import VoiceClient

customer_id = "D831ADEB-6586-4365-9F9B-DD04279780DC"
api_key = "s+CTmbEpa1tN22qPxOLfszDlNjfjiuqBaK2p+h2v/feaEIArbB9NwwIPfs0z3ZJNYnhoDEWA8ENrLJTUDcrQfQ=="

phone_number = "5511 numero do telefone de destino"
message = "Mensagem que será ouvida ao atender."
message_type = "ARN"

voice = VoiceClient(customer_id, api_key)
response = voice.call(phone_number, message, message_type)


