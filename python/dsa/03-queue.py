# queue - linear data structure, O(1), FIFO(first in first out), enqueue(adding element at rear end), dequeue(removing element at front end)

class Queue(object):
    
    #constructor
    def __init__(self) -> None:
        self.queue = []
        
    #checking if queue is empty
    def isEmpty(self):
        return self.queue==[]
    
    #padding element to queue
    def enqueue(self, data):
        self.queue.insert(0,data)
        return f'{data} added to queue'
    
    #removing element from queue
    def dequeue(self):
        return f'{self.queue.pop()} removed from queue'
    
    #checking size of queue
    def queueSize(self):
        return f'size of queue is {len(self.queue)}'
    
    
if __name__=='__main__':
    q = Queue()
    print(q.isEmpty())
    print(q.enqueue(1234))
    print(q.queueSize())
    print(q.enqueue(678))
    print(q.queueSize())
    print(q.enqueue(890))
    print(q.queueSize())
    print(q.dequeue())
    print(q.queueSize())
    print(q.dequeue())
    print(q.queueSize())
    

        