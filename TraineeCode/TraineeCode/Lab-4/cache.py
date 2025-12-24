class Cache:
    _MAX_CAPACITY = 0

    """
    Static method to get the maximum capacity of the cache
    """
    
    @classmethod   #conceptually belongs to the class, not just a utility When a method operates on class-level data,
    def get_max_capacity(cls):    # #@classmethod is preferred over @staticmethod to support polymorphism and clean OOP design
        if cls._MAX_CAPACITY == 0:    #if used static method and Cache._MAX_CAPACITY , it breaks the purpose
            cls._MAX_CAPACITY = int(input("Enter MAX_CAPACITY: "))
            print("\n")
        print("Returning MAX_CAPACITY")
  
        return cls._MAX_CAPACITY