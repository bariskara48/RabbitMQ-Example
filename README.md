# RabbitMQ-Example

## Message Broker (RabbitMQ)
- I running up the message broker server (rabbitMQ) via docker. I used the following command for this:
`nano` docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13-management

## Requirements
- You need to only run `npm -i` for install node dependicies.
- Python dependicies:
  - pika
  - pandas 
