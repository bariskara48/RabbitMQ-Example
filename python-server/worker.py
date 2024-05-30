import pika
import pandas as pd
import json
from eclat import eclat
import io

def callback(ch, method, properties, body):
    print("Received a message")
    
    # Decode the message body to a string
    csv_data = body.decode('utf-8')
    
    # Read the CSV data into a DataFrame
    df = pd.read_csv(io.StringIO(csv_data))
    
    # Convert the DataFrame to a matrix (list of lists)
    matrix = df.values.tolist()
    
    # Run the Eclat algorithm
    result = eclat(matrix, 2)

    # Convert the result to a JSON string
    result_str = json.dumps(result)

    # Publish the result to the queue
    ch.basic_publish(exchange='', routing_key='data_mining_queue', body=result_str)

    # Acknowledge the message
    ch.basic_ack(delivery_tag=method.delivery_tag)

def start_worker():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.basic_qos(prefetch_count=20)
    channel.basic_consume(queue='data_mining_queue', on_message_callback=callback)
    print("Worker is waiting for messages...")
    channel.start_consuming()

if __name__ == '__main__':
    start_worker()
