import sys
sys.path.insert(0, ".")
import serve
from http.server import ThreadingHTTPServer
port = int(sys.argv[1]) if len(sys.argv) > 1 else 8766
print(f"headless serve on {port}", flush=True)
ThreadingHTTPServer(("127.0.0.1", port), serve.Handler).serve_forever()
