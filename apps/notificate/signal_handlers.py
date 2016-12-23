from .rabbit_connect import RabbitConnector

rabbit_connector = RabbitConnector()


def save_handler(sender, instance, **kwargs):
    message = {
        'msg': 'saved',
        'code': 1
    }
    rabbit_connector.send_message(message)
    print('saved')


def delete_handler(sender, instance, **kwargs):
    message = {
        'msg': 'deleted',
        'code': 2
    }
    rabbit_connector.send_message(message)
    print('deleted')
