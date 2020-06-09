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


# Distributed Message Queue  

Synchronous communication, easy to do, but hard to maintain, slow consumer, failed request.  

Functional requirements: publish and receive 
sendMessage(messageBody)
receiveMessage() 

Scalable, Highly Available, Durable  

Order guarantees,  

vip -> symbolic hostname points to a load balance which routes to multiple servers, make sure the system could horizontal scalable in the future
10k HTTP requests per second for a modern LB

Broker Service  
Request validation  , mandatory parameters, message size
Authentication  , authentication of the sender, authorization for publish and receive
Encryption and Decryption
Caching  authentication  , most used queues
Rate limiting, throttling 
Request dispatching  , write to the metadata service, read to the data service
Request duplication, UUID manages for the messages  

MetaData Service:
Queue information, publisher and receivers
Store the information about queue and data hosts  

Many reads, little writes  
Consistency hash for the meta service to server the data  
partition the data when stored  

Data Service a layer between storage and application
Where and how do we store the messages?  
Database, file system, in memory

How to replicate the data? Replica across the machines.

Leader-follower relationship, write go the leader, read go to all nodes, leader do data replication  

Small cluster of independent hosts, random cluster handle the writes, but replicate across the clusters  


Data Manager Service  
1. Track each nodes health and status  
2. Track the queues to the nodes mapping  

Problems:
Queue creation and deletion  
Message deletion  
Message replication, sync or async (sync for strong consistency, async for eventual consistency)  
Message delivery semantics

# Top k  
Liked photos, shared posts  

Category of streaming problems

TopK(k, startTime, endTime)  

Nonfunctional:
Scalable  
High Available  
High Performance  
Accurate  


Merge n sorted lists, cannot load everything into memory to calculate the last 60 minutes top K. When partition data, we need to deal with replications,  

Count-min sketch  
fast path  
slow path

You cannot derive topK per two hours from topK per one hour data, because the data distribution is not even.  

Simple idea: a sequence of video ids, hash table, min heap to store the top K  
To scale it up: data partition service is needed, processor only pass top k points to the aggregator  
aggregator can load this data into memory.  

To find top K through last 24 hours, we need to process all data to see the result, cannot derive from the hourly data, and we cannot load this data into memory.  
Distributed Job or MapReduce is needed here.  
Gateway aggregated the data and send to the distributed messaging system  
## Partitions  
1. Hot partition  
2. Replication  
3. Add/remove hosts  

Count-min Sketch  

Multiple hash functions to a long hash values, minimum all of the counters for the element.

# Data Calculation Details  

Data Frequency calculation first:  
Raw data (aggregated result) -> maps to partition, same result went to the same partition, form a key value pairs, key is the ID, value is a list of counts  
-> Sum of all the account for a key, a distributed calculation -> Aggregator receive the result from each Calculator store it in the output, the output is not  
sorted.  

Now, we have the output data in the HDFS or S3 -> we need to map the output data which is key is the ID, value is the count -> Each top k service filter out the  
top K IDs and count then send to reducer -> reducer aggregate them into memory and find final list of TopK  

Aggregate data in memory of several minutes, send to a file system  
Aggregator calculates the count map based on the size or a time setting,  

We process data in batch and streaming in both time, and search or merge the result at the end.  When talking about the partition, always think about the hot spot  
non-uniform distribution of the storage, store across the splits.  
## The news feed  
News feed and top K tags have to been pre-generated, as adhoc calculation caused too much latency which doesn't match wit the requirement.  

# Rate Limiting  
Why not using LB to throttle the requests , why do we need throttling?  Throttling doesn't distinguish the requests types.
What about each host just throttle the requests locally?  the requests are not distributed evenly, this is causing the system waste.  


Simple solution:  Rules retriever, Token Bucket Algorithm, each bucket, max capacity, current tokens  

# Chord Distributed Hash Table  

Distribute pairs over millions of peers  
Any peer can query the database  
The peer only store fraction of the hash table  

immediate successor , first key <= current key
Circular DHT  
if one peer is only aware two other peers, could be a million of peers, but each peer only knows few other peers  
Resolving a query, send the key to the nearest successor, successor do the same until the first hash key >= key  
Shortcuts peers, for quickly lookup, each node will have a shortcut peer. Change from O(n) to O(log(n))  
Peer churn  
Peer may come and leave, 2 successors. Heartbeat or ping to the successors, if immediate successor leaves, choose next successor as new immediate  
successor.  Also ask the second successor what's his successor and use as current secondary successor.  

## Data Replication in Consistency Hashing  
the data is stored in the node the 2 successors, if the current node is down, the heartbeat will detect that, the successor will automatically copy over  
more keys from the anti-clock wise node. But this only impact 2 successor nodes.  

# Gossip Protocol  
Data Replication, synchronize data across lots of nodes.  