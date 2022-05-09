
import time

def timing(get_response):
    def middleware(request):
        time_after = time.time()
        resp = get_response(request)
        time_before = time.time()
        print ("TOTAL TIME", (time_after-time_before))
        return resp
    return middleware