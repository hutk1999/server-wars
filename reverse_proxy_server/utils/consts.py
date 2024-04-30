HOSTNAME = 'fast_api_server:8000'
SERVER_IP = '192.168.1.2'
SERVER_PORT = 9000

URL_PATH_WHITELIST = [
    '/geolocation/ip',
    '/geolocation/country',
    '/geolocation/topfive',
]

HEADER_KEYS = ['Content-Encoding', 'Transfer-Encoding', 'content-encoding', 'transfer-encoding',
               'content-length', 'Content-Length']

USER_AGENTS = ["Mozilla/5.0 (Android; Linux armv7l",
               "Mozilla/5.0 (WindowsCE",
               "Mozilla/5.0 (Windows NT",
               "Mozilla/5.0 (Windows; U;",
               "Mozilla/5.0 (X11; FreeBSD amd64",
               "Mozilla/5.0 (X11; Linux i686",
               "Mozilla/5.0 (X11; Linux x86_64",
               "Mozilla/5.0 (X11; U; FreeBSD",
               "Mozilla/5.0 (X11; U; Linux arm7tdmi",
               "Mozilla/5.0 (X11; U; Linux armv6l",
               "Mozilla/5.0 (X11; U; Linux; en-US",
               "Mozilla/5.0 (X11; U; Linux i586",
               "Mozilla/5.0 (X11; U; Linux; i686",
               "Mozilla/5.0 (X11; U; Linux i686",
               "Mozilla/5.0 (X11; U; Linux ppc",
               "Mozilla/5.0 (X11; U; Linux x86_64",
               "Mozilla/5.0 (X11; U; NetBSD amd64",
               "Mozilla/5.0 (X11; U; OpenBSD arm",
               "Mozilla/5.0 (X11; U; OpenBSD i386",
               "Mozilla/5.0 (X11; U; SunOS",
               "Mozilla/5.0 (X11; U; Linux x86_64",
               "Mozilla/5.0 (Linux; Android 7.1.1",
               "Mozilla/5.0 (Linux; Android 7.1.1",
               "Mozilla/5.0 (Linux; Android 6.0.1",
               "Mozilla/5.0 (Linux; Android 5.1.1",
               "Mozilla/5.0 (Linux; Android 5.1",
               "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac",
               "Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac",
               "Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac",
               "Mozilla/5.0 (iphone x Build/MXB48T; wv)"]
