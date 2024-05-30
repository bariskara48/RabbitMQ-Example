# RabbitMQ-Example

## Message Broker (RabbitMQ)
- I running up the message broker server (rabbitMQ) via docker. I used the following command for this:
```
$ docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13-management
```

## Requirements
- You need to only run `npm -i` for install node dependicies.
- Python dependicies:
  - pika
  - pandas 

## Results

RabbitMQ:

![Screenshot from 2024-05-31 00-43-30](https://github.com/bariskara48/RabbitMQ-Example/assets/124704473/e411d874-3f8b-43fc-9b15-1da382034007)

Python Worker (Consumer):

![Screenshot from 2024-05-31 00-47-20](https://github.com/bariskara48/RabbitMQ-Example/assets/124704473/6ebcdb34-fb47-4b8c-9a69-47995333bc85)

Association Rules:

![Screenshot from 2024-05-31 00-42-20](https://github.com/bariskara48/RabbitMQ-Example/assets/124704473/bafdd024-65f9-4abd-ae6c-3d4c0ed853e7)
