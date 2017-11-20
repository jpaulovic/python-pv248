from collections import Counter
import operator


class CallInspector:
    def __init__(self):
        self.counts = Counter()

    def inspect(self, func):
        def wrapper(*args, **kwargs):
            self.counts[args[0]] += 1
            return func(*args, **kwargs)
        return wrapper

    def show_call_stats(self):
        "show some call statistics"
        for n,args in enumerate(self.counts.most_common()):
            print("Function was called {} times with parameter {}.".format(
                args[1], args[0]))
        print("Most frequently called parameter combinations was: {}".format(
            self.counts.most_common()[0]
        ))


inspector = CallInspector()


@inspector.inspect
def fib(n):
    "Return n-th Fibonacci number"
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)


# invoke function and show call statistics
fib(15)
inspector.show_call_stats()