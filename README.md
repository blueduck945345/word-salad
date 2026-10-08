# word-salad

## Description

SDK and sever for Motorola task.

In order to make the process threadsafe, I opted to incorporate Redis as a datastore for the line entry data. Because Redis is single-threaded, as long as operations are atomic, sampling and loading lines should also be threadsafe.

Redshift has a couple advantages:
 - Redis can manage the transaction itself and just let the server just concern itself with the I/O
 - Could let the server scale independently and have a synchronized state solution for multiple containers
 - Can horizontally scale the datastore in terms of memory

 Disadvantages:
 - Its adding a new technology
 - Need to be able recover if Redis crashes (which is possible)

An alternative might have been to just use a threadsafe lock within the server but that would not be suspectible to crashes and would not scale to multiple containers.

The server stores data by performing a `SADD` operation, adding any number of sanitized lines to the designated set. Sampling involves an `SPOP` operation and removes the specified number of set entries at random.

## Setup

### Server

- Install Docker Desktop and CLI
- Within /server directory -- run `docker-compose up`

### SDK

- See `/sdk/README.md`
