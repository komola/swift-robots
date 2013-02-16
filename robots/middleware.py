# Copyright 2013 komola GmbH
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
    Robots middleware denies access for search engines
"""

from webob import Request, Response

class RobotsMiddleware(object):
    """
    Robots middleware denies access for search engines

    If the path is /robots.txt, it will respond with Deny All.
    """

    def __init__(self, app, *args, **kwargs):
        self.app = app

    def GET(self, req):
        """Returns a 200 response with "GO AWAY!" in the body."""
        return Response(request=req, body="User-agent: *\nDisallow: /", content_type="text/plain")

    def __call__(self, env, start_response):
        req = Request(env)
        try:
            if req.path == '/robots.txt':
                return self.GET(req)(env, start_response)
        except UnicodeError:
            # definitely, this is not /robots.txt
            pass
        return self.app(env, start_response)


def filter_factory(global_conf, **local_conf):
    def robots_filter(app):
        return RobotsMiddleware(app)
    return robots_filter