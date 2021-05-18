import random
class QueueSimulation:
    def __init__(self,a,b,c,d):
        self.process_rate = a
        self.min_req_rate = b
        self.max_req_rate = c
        self.queue = []
        self.queue_capacity = d
    
    def step(self, req):
        result = []
        lost_count = 0
        while len(self.queue) > 0:
            previous_queue_process = self.queue.pop(0)
            result.append(previous_queue_process)
        while len(result) < self.process_rate:
            process = req.pop(0)
            result.append(process)
        if len(req) == 0:
            pass
        else:
            while len(self.queue) < self.queue_capacity:
                not_yet_processed = req.pop(0)
                self.queue.append(not_yet_processed)
            if len(req) == 0:
                pass
            else:
                lost_count = len(req)
        return result, lost_count

    def run(self, n):
        for i in range (n):
            a = 0
            number_of_requests = random.randint(self.min_req_rate,self.max_req_rate)
            number_of_results = 0
            length_of_queue = 0
            max_length_of_queue = self.queue_capacity
            number_of_results += length_of_queue
            length_of_queue = 0
            if number_of_requests <= self.process_rate - number_of_results:
                number_of_results += number_of_requests
            else:
                number_of_requests -= (self.process_rate - number_of_results)
                if number_of_requests > max_length_of_queue:
                    length_of_queue = max_length_of_queue
                    a += 1
                else:
                    length_of_queue = number_of_requests 
            lost_frequency = a/n 
            return lost_frequency

            
            



        
        

