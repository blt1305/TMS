import time
from django.db import connection

class QueryLogsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        print(f'Query path: {request.path}, Query time: {time.time() - start_time}')
        print(f"Qyery count: {len(connection.queries)}")
        for query in   connection.queries:
              print(f"Query: {query['sql']}")
        return response