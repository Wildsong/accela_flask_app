from tasks import add

# This queues the "add" but does not 
# return any result because we're asynchronous.
result = add.delay(4,4)

