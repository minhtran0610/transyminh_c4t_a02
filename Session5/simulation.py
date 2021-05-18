import random
class Simulation:
    def __init__(self,a,b,c):
        self.process_rate = a
        self.min_req_rate = b
        self.max_req_rate = c
    
    def run(self, n):
        sum_of_requests = 0
        dropped_requests = 0
        for i in range (n):
            req_rate = random.randint(self.min_req_rate, self.max_req_rate)
            sum_of_requests += req_rate
            if req_rate <= self.process_rate:
                pass
            else:
                dropped_requests += (req_rate - self.process_rate)
        lost_request_rate = dropped_requests/sum_of_requests
        return lost_request_rate
