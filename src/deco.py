import functools
import time


def profile(f):
    @functools.wraps(f)
    def deco(*args):
        start = time.time()
        deco._num_call += 1
        result = f(*args)
        deco._num_call -= 1
        if deco._num_call == 0:
            print(f'Elapsed {time.time() - start}ms')
        return result

    deco._num_call = 0

    return deco

def pre(cond, message):
    """
    Precondition decorator creater. Checks if the passed condition is true
    :param cond: Condition to check
    :param message: Message to display if the condition is not met
    :return: pre decorator
    """

    def deco(func):

        @functools.wraps(func)
        def inner(self, *args, **kwargs):
            job = kwargs['job'] if 'job' in kwargs else args[2] # func(cr, uid, job_obj) or func(cr, uid, job=job_obj)
            if not cond(self, job):
                raise osv.except_osv(_('Precondition is not met'),
                                     _("%s" % message))
            return func(self, *args, **kwargs)

        return inner

    return deco



def cache(max_limit=None):
    def inner(f):
        @functools.wraps(f)
        def deco(*args):
            if args not in deco._cache:
                result = f(*args)
                if max_limit is not None and len(deco._cache) > max_limit:
                    first_key = next(iter(deco._cache))
                    deco._cache.pop(first_key)
                deco._cache[args] = result
            return deco._cache[args]

        deco._cache = {}
        return deco

    return inner

#fibo = cache(profile(fibo))
@cache(max_limit=2)
#@functools.lru_cache
@profile
def fibo(n):
    """Inefficient fibo function"""
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

# 1 1 2 3 5 8 13
print(fibo(150))
help(fibo)
