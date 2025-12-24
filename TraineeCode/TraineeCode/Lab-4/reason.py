# class Cache:
#     _MAX_CAPACITY = None

#     @staticmethod
#     def get_max_capacity():
#         if Cache._MAX_CAPACITY is None:
#             Cache._MAX_CAPACITY = int(
#                 input("Enter Cache capacity: ")
#             )
#         return Cache._MAX_CAPACITY


# class LRUCache(Cache):
#     _MAX_CAPACITY = None



# print("Cache capacity:", Cache.get_max_capacity())
# print("LRUCache capacity:", LRUCache.get_max_capacity())
# print("Cache capacity again:", Cache.get_max_capacity())


class Cache:
    _MAX_CAPACITY = None

    @classmethod
    def get_max_capacity(cls):
        if cls._MAX_CAPACITY is None:
            cls._MAX_CAPACITY = int(
                input(f"Enter {cls.__name__} capacity: ")
            )
        return cls._MAX_CAPACITY


class LRUCache(Cache):
    _MAX_CAPACITY = None




print("Cache capacity:", Cache.get_max_capacity())
print("LRUCache capacity:", LRUCache.get_max_capacity())
print("Cache capacity again:", Cache.get_max_capacity())
