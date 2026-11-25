"""Servidor local do site (alternativa ao Live Server). Rode com: py _serve.py"""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ROUTES = {
    "/": "/index.html",
    "/about": "/about.html",
    "/tech": "/tech.html",
    "/news": "/news.html",
    "/legal": "/legal.html",
    "/privacy": "/privacy.html",
    "/about/": "/about.html",
    "/tech/": "/tech.html",
    "/news/": "/news.html",
    "/legal/": "/legal.html",
    "/privacy/": "/privacy.html",
}


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()

    def do_GET(self):
        path = self.path.split("?", 1)[0]
        if path in ROUTES:
            path = ROUTES[path]
        self.path = path
        return super().do_GET()


if __name__ == "__main__":
    import webbrowser

    url = "http://127.0.0.1:8770/"
    server = ThreadingHTTPServer(("127.0.0.1", 8770), Handler)
    print(f"Site no ar em {url}  (feche esta janela ou aperte Ctrl+C para parar)")
    webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
