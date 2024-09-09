# PUSHING IN A QUEUE
We can use LPUSH (Push from Left Side) or RPUSH (Push from Right Side)

## Command for LPUSH/RPUSH -> 
    LPUSH <queueName> value

    RPUSH <queueName> value
e.g., LPUSH problems "{problemId: 1, userId: 2}"

e.g., RPUSH problems 1


# POPING FROM A QUEUE
We can use LPOP (Pop an element from Left Side) or RPOP (Pop from Right)

## Command for LPOP/RPOP ->
    LPOP <queueName>

    RPOP <queueName>
e.g., LPOP problems

e.g., RPOP problems


# BLOCKING POP
We use BLPOP (Blocking Left POP) or BRPOP (Blocking Right POP)

It returns a value, if already present in the queue,
Else it waits for 'number_of_seconds' seconds, (0 means Infinite Time), If a value is inserted in the queue, within the timeframe, it will pop that value, else it will provide NIL

## Command for BLPOP/BRPOP ->
    BLPOP <queueName> number_of_seconds

    BRPOP <queueName> number_of_seconds
e.g., BRPOP problems 5      // Wait for 5 seconds

e.g., BLPOP problems 0      // Wait for Infinite Seconds, till a value is pushed in the queue