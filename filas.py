from typing import Deque, Any, Iterator
from collections import deque

class Queue:

    def __init__(self, maxlen = None) -> None:
        self.__items: Deque[Any] = deque(maxlen=maxlen)

    def enqueue(self, *items: Any) -> None:
        for item in items:
            self.__items.append(item)

    def dequeue(self) -> Any:
        if not self:
            raise IndexError('pop from empty queue')

        return self.__items.popleft()

    def __repr__(self) -> str:
        return str(self.__items)

    def __bool__(self) -> bool:
        return bool(self.__items)

    def __len__(self) -> int:
        return len(self.__items)

    def __iter__(self) -> Iterator:
        return self.__items.__iter__()
    
    def __getitem__(self, index: int) -> Any:
        return self.__items[index]

if __name__ == "__main__":
    fila = Queue()

fila.enqueue ('A', 'B', 'C', 'D')

print(fila.__repr__())
print(fila.__getitem__(2))
print(fila.__bool__())
print(fila.__iter__())

fila.enqueue ('d', 'e', 'f', 'g')

print(fila)

print('Item com índice 1:', fila[1], end ='\n\n')

for item in fila:
    print('Interaçâo:', item)
