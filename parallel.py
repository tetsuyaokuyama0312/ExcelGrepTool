from concurrent import futures

DEFAULT_MAX_WORKERS = 20


def invoke_and_join_all(fn, input_values: list, max_workers=DEFAULT_MAX_WORKERS, **kwargs):
    future_list = []
    with futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        for value in input_values:
            future = executor.submit(fn, value, **kwargs)
            future_list.append(future)
        futures.as_completed(fs=future_list)
    return list(map(lambda f: f.result(), future_list))
