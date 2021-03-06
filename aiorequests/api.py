import aiohttp

from aiorequests.client import HTTPClient
from aiorequests._utils import default_pool, default_loop


def head(url, **kwargs):
    """
    Make a ``HEAD`` request.

    See :py:func:`aiorequests.request`
    """
    return _client(**kwargs).head(url, **kwargs)


def get(url, headers=None, **kwargs):
    """
    Make a ``GET`` request.

    See :py:func:`aiorequests.request`
    """
    return _client(**kwargs).get(url, headers=headers, **kwargs)


def post(url, data=None, **kwargs):
    """
    Make a ``POST`` request.

    See :py:func:`aiorequests.request`
    """
    return _client(**kwargs).post(url, data=data, **kwargs)


def put(url, data=None, **kwargs):
    """
    Make a ``PUT`` request.

    See :py:func:`aiorequests.request`
    """
    return _client(**kwargs).put(url, data=data, **kwargs)


def patch(url, data=None, **kwargs):
    """
    Make a ``PATCH`` request.

    See :py:func:`aiorequests.request`
    """
    return _client(**kwargs).patch(url, data=data, **kwargs)


def delete(url, **kwargs):
    """
    Make a ``DELETE`` request.

    See :py:func:`aiorequests.request`
    """
    return _client(**kwargs).delete(url, **kwargs)


def options(url, **kwargs):
    """
    Make a ``OPTIONS`` request.

    See :py:func:`aiorequests.request`
    """
    return _client(**kwargs).options(url, **kwargs)


def request(method, url, **kwargs):
    """
    Make an HTTP request.

    :param str method: HTTP method. Example: ``'GET'``, ``'HEAD'``. ``'PUT'``,
         ``'POST'``.
    :param str url: http or https URL, which may include query arguments.

    :param headers: Optional HTTP Headers to send with this request.
    :type headers: Headers or None

    :param params: Optional parameters to be append as the query string to
        the URL, any query string parameters in the URL already will be
        preserved.

    :type params: dict w/ str or list/tuple of str values, list of 2-tuples, or
        None.

    :param data: Optional request body.
    :type data: str, file-like, IBodyProducer, or None

    :param reactor: Optional twisted reactor.

    :param bool persistent: Use persistent HTTP connections.  Default: ``True``
    :param bool allow_redirects: Follow HTTP redirects.  Default: ``True``

    :param auth: HTTP Basic Authentication information.
    :type auth: tuple of ``('username', 'password')``.

    :param cookies: Cookies to send with this request.  The HTTP kind, not the
        tasty kind.
    :type cookies: ``dict`` or ``cookielib.CookieJar``

    :param int timeout: Request timeout seconds. If a response is not
        received within this timeframe, a connection is aborted with
        ``CancelledError``.

    :rtype: Deferred that fires with an IResponse provider.

    """
    return _client(**kwargs).request(method, url, **kwargs)


#
# Private API
#

def _client(*args, **kwargs):
    return HTTPClient()
