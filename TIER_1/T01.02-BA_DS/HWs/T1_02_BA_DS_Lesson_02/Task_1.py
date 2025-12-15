from queue import Queue

queue = Queue()     # create empty queue

def generate_request(request):  # funtion for generating requests
    print(f"Створено заявку: {request}")
    queue.put(request)


def process_request():          # processing function
    if not queue.empty():
        req = queue.get()
        print(f"Обробляємо заявку: {req}")
    else:
        print("Черга пуста")


generate_request("Заявка-1")    # main part
generate_request("Заявка-2")
generate_request("Заявка-3")

process_request()
process_request()
process_request()
process_request()       # empty queue
