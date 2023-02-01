import logging

import urllib3

http = urllib3.PoolManager()


def get_url_title(url: str) -> str | None:

    try:
        req = http.request('GET', url)
        body = req.data.decode('utf-8')
        w = body.split('<title>')
        if len(w) < 2:
            raise ValueError('Missing <title> tag')
        title = w[1].split('</title>')[0]

        return title
    except Exception as exc:
        logging.getLogger('utils').error('Failed to request %s - %s', url, exc)
