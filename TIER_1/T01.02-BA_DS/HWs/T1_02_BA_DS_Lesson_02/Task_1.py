from queue import Queue

requests_queue = Queue()    # Creating an empty queue

request_id_counter = 0


def generate_request():
    global request_id_counter
    request_id_counter += 1                       # own number for each request
    request = f"Request-{request_id_counter}"     # creating a new request
    requests_queue.put(request)                   # add request at the end of the queue
    print(f"Created request: {request}")


def process_request():
    if not requests_queue.empty():                # check if queue has at least one element
        request = requests_queue.get()            # remove the oldest request

        print(f"Processing request: {request}")
    else:
        print("Queue is empty")


generate_request()      # Generate 3 requests 
generate_request()
generate_request()

process_request()       # simulate processing of requests
process_request()
process_request()

process_request()       # additional for empty queue