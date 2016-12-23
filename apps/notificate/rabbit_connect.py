import json

import pika
from django.conf import settings as django_settings


class RabbitConnector:
    def __init__(self, queue="default_queue"):
        self._queue = queue
        self.settings = django_settings

        connection = pika.BlockingConnection(pika.ConnectionParameters(
            host=self._get_host(), port=self._get_port()))
        self.channel = connection.channel()
        self.channel.queue_declare(queue=self._queue)

    def send_message(self, msg=None):
        if msg is None:
            msg = {'msg': "default_msg"}
        self.channel.basic_publish(exchange='', routing_key=self._queue,
                                   body=json.dumps(msg))

    def _get_host(self):
        return getattr(self.settings, 'RABBIT_HOST', 'localhost')

    def _get_port(self):
        return int(getattr(self.settings, 'RABBIT_PORT', '5672'))
