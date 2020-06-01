# Autocomplete System Design  
Q: How many entries?  
A: 10 billion

Q: where is the data coming from?  
A: logs

Q where are the latency requirements?  
A: 100ms 99 percentile

Q: machine limitations?  
A: 4 CPUs, 16gb, 20gb


Q: Array or Hashtable  
A: hashtable: sparsity, unicode

Q: The trie cannot fit into the main memory, what will you do?  
A: Split the trie by prefix, one letter per machine. The aggregator will update the database and cache layer.  
Once the aggregator get the result, save that into a DB and publish it to the cache. The front end app will query  
the cache to get the autocomplete results.

# Load Balancer  

L4, or L7 level LB, L4 LB only forward packages based on the top headers of 
the TCP packets, it can simply forward messages to upstream and downstream.
L4 could make decision based on the contents of the message. CPU-heavy LB, apply optimizations and changes the contents
such as compression and encryption.

# Message Systems #  

Key Requirements:  
* One on One conversations
* Keep track of the online/offline statues of its users  
* Support the persistent storage of chat history  
* Support multiple devices
* Low latency  
* Push notifications
* Group Chats  

Message pulling vs pushing?  
Pull model will results lots of empty response and wasted time waiting the server side  
Push model will make sure there is a connection maintain between the server and the client. For 1 billion users, to maintain 
all of the connections are not scale.  


Online status  
Clients pull periodically acts with two purposes, first is heartbeat, second is to fetch the online friends and offline friends.  

Storage estimation:  
100 million active users * 20 messages per day * 100 byte = 100,000 bytes
Schema for Messages  

|Attributes|Purpose|Index|
|---|---|---|
| id | identifier| True|
|thread id| association to thread, one to one| True|
|content| text  messages | False|
|crated time |||
|updated time|||  

Schema for Threads  

|Attributes|Purpose|Index|
|---|---|---|
| id | identifier for thread| True|
|owner id| each owner will own it's private thread| True|
|nickname| customization for users | False|
|participant_ids | all parties ||
|crated time |||
|updated time|||  



## Choice Of Database
* NoSQL for messages, Big data, not easy to change, every message is a log
* SQL for threads, primary key is thread_id + owner_id, index by owner_id + updated time  

## Push And Receive Messages  
Sender
* Clients send messages to the server
* Server create threads for each receivers
* Create a message with that thread  

# Twitter
## Database Schemas
Tweet  

|Attributes|Purpose|Index|
|---|---|---|
| tweat_id | identifier for the tweat| True|
| user id | creator of the tweat| True|
|content| tweat messages | False|
|participant_ids | all parties ||
|crated time |||

User  

|Attributes|Purpose|Index|
|---|---|---|
| name | identifier for the tweat| True|
| id | creator of the tweat| True|
|birthday| | False|
|join date |||
|last join time |||  

User Follows  

|User id1 |User id2|
|---------|---------|  


## Data Sharding  

### Sharding on UserID  
Meaning different servers may save different users info and its tweats and followers and favorites. If the user is a super star,   
Then it may overload the machines which stores the super star users.  

User behavior is not consistent, thus the distribution of the data may not be balanced.  


### Sharding on TweetID  
Meaning to get one user's tweets, we may need to query all machines to get his tweats. Do the same thing for all of the followers,  
Then sort all of the tweats.  

### Sharding on Tweet Creation Time  
The latest tweets may become a hotspot  

### Sharding on TweetID + Creation Time  
Thus the latest tweets are crossed the machines evenly, the query for all tweets for a particular user is fast as well.  


## Cache  
LRU cache policy, key is the user id, values is a double linked list containing all of the tweets for last 3 days.
