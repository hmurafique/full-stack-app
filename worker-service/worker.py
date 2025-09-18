from celery import Celery

app = Celery('tasks', broker='amqp://guest:guest@localhost:5672//')

@app.task
def process_order(order_id):
    return f"Order {order_id} processed"

