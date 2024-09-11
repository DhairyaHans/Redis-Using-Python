# STORING DATA 

## Command to SET (Store) key-value pairs ->
    SET myKey <value>
e.g. -> SET user "Dhairya"

NOTE -> The value must be a String, so to store an object, you must Stringify it, like: 

    SET tracks "[{title: 'typescript', desc: 'Hello TS'}]"


# FETCHING DATA

## Command to GET (Fetch) a value from Redis -> 
    GET myKey
e.g., GET tracks


# DELETE DATA

## Command to DELETE a key-value pair from Redis ->
    DEL myKey
e.g., DEL tracks



# STORING MULTIPLE THINGS FOR A SINGLE KEY
We use HSET/HGET/HDEL for such usecases, where H stands for "Hash"

## Dummy command for HSET ->
    HSET user:100 name "John Doe" email "john.doe@gmail.com" age "30"

## Dummy command for HGET -> 
    HGET user:100 name

    HGET user:100 email

## Dummy command for HDEL ->
    HDEL user:100 age

## HGETALL ->
Returns all the data for a particular Hash Key
    HGETALL user:100



