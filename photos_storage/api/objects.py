import requests
import json
from django.conf import settings
from django.core.cache import cache


class ApiAuth(object):
    access_token = None

    @staticmethod
    def new_token():
        url = settings.EXTERNAL_API_URL + 'auth'
        res = requests.post(url, json={"apiKey": settings.API_KEY})
        results = res.json()
        cache.set('token', results['token'], 30)
        ApiAuth.access_token = results['token']
        return ApiAuth.access_token

    @staticmethod
    def get_token():
        cashed_token = cache.get('token')
        if cashed_token:
            ApiAuth.access_token = cashed_token
            return ApiAuth.access_token
        return ApiAuth.new_token()


def refresh_token(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            ApiAuth.new_token()
            return func(*args, **kwargs)
    return wrapper


class ApiImages(object):
    pictures = []

    @staticmethod
    def get_cached(key):
        cached = cache.get(key)
        if cached:
            return json.loads(cached)

    @staticmethod
    @refresh_token
    def request_images(page, key):
        token = "Bearer " + ApiAuth.get_token()
        headers = {"Authorization": token}
        pagination = '?page=' + page if page else ''
        res = requests.get(settings.EXTERNAL_API_URL + 'images' + pagination, headers=headers)
        results = res.json()
        cache.set(key, json.dumps(results), 30)
        return results

    def get_images(self, page):
        key = ''.join(['list_page', page or '1'])
        cached = self.get_cached(key)
        if cached:
            return cached
        return self.request_images(page, key)
