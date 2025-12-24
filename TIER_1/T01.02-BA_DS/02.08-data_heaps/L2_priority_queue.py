
# ----------------- !!!!!!!!!!! Only for example


import heapq
from image_converter import convert_image
from priority_queue import PriorityQueue

def convert_image(file_name, target_format):
    # Припустимо, що ця функція конвертує зображення (тут просто імітація)
    print(f"Конвертація {file_name} до {target_format} формату...")
    return f"{file_name.split('.')[0]}.{target_format}"


# ------------- !!!!! :
class PriorityQueue:
    def __init__(self):
        self.queue = []   # list for keeping elements in queue

    def enqueue(self, task, priority):  # adds task
        heapq.heappush(self.queue, (-priority, task)) # negative priority for max priority

    def dequeue(self):  # deletes and returns tasks with max priority
        return heapq.heappop(self.queue)[1]

    def is_empty(self): # checks if queue is empty
        return not bool(self.queue)


def main():
    pq = PriorityQueue()

    # Користувачі завантажують свої зображення
    pq.enqueue(("sample1.jpg", "png"), 1)  # Основний користувач
    pq.enqueue(("premium_sample.jpg", "bmp"), 10)  # Преміум-користувач
    pq.enqueue(("sample2.jpg", "tiff"), 1)  # Основний користувач

    while not pq.is_empty():
        file_name, target_format = pq.dequeue()
        output_file = convert_image(file_name, target_format)
        print(f"Зображення було успішно конвертовано і збережено як {output_file}!")

if __name__ == "__main__":
    main()