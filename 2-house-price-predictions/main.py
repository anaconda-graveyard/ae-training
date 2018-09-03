import os
import sys
import json
import argparse

import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver
from tornado.options import define, options

import pandas as pd
from predict import predict

root = os.path.dirname(__file__)
static = os.path.join(root, 'static')


class Application(tornado.web.Application):
    def __init__(self, anaconda_project_hosts):
        handlers = [
            (r"/api/predict", PredictHandler),
            # (r"/api/batch", BatchHandler),
            (r"/(.*)",  tornado.web.StaticFileHandler, {"path": static, "default_filename": "index.html"}),
        ]
        tornado.web.Application.__init__(self, handlers, debug=False)
        self._application = dict(anaconda_project_hosts=anaconda_project_hosts)


class PrepHandler(tornado.web.RequestHandler):
    def prepare(self):
        anaconda_project_hosts = self.application._application['anaconda_project_hosts']
        if self.request.host not in anaconda_project_hosts:
            print("{} not allowed in aborting...".format(self.request.host))
            print("Allowed hosts: {}".format(anaconda_project_hosts))
            raise tornado.web.HTTPError(403)


class IndexHandler(PrepHandler):
    def get(self):
        self.write("Prediction endpoint available at /api/predict and /api/batch")


def get_record():
    i = 0
    return pd.read_csv('data/test.csv', nrows=10)[i:i+1].reset_index(drop=True)


class PredictHandler(PrepHandler):
    def get(self):
        df = get_record()
        # df.at[(0, 'OverallQual')] = self.get_argument("OverallQual", default=0)
        # df.at[(0, 'YearBuilt')] = self.get_argument("YearBuilt", default=0)
        df.at[(0, 'YearRemodAdd')] = self.get_argument("YearRemodAdd", default=0)
        df.at[(0, 'LotArea')] = self.get_argument("LotArea", default=0)
        df.at[(0, 'LotFrontage')] = self.get_argument("LotFrontage", default=0)
        df.at[(0, 'GrLivArea')] = self.get_argument("GrLivArea", default=0)
        df.at[(0, '1stFlrSF')] = self.get_argument("stFlrSF", default=0)
        df.at[(0, '2ndFlrSF')] = self.get_argument("ndFlrSF", default=0)
        df.at[(0, 'FullBath')] = self.get_argument("FullBath", default=0)
        df.at[(0, 'GarageCars')] = self.get_argument("GarageCars", default=0)
        df.at[(0, 'Fireplaces')] = self.get_argument("Fireplaces", default=0)

        predictions = predict(df).tolist()[0]
        self.write(json.dumps(predictions))


def main(anaconda_project_hosts):
    http_server = tornado.httpserver.HTTPServer(Application(anaconda_project_hosts))
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    # arg parser for the standard anaconda-project options
    parser = argparse.ArgumentParser(prog="home-price-clf",
                                     description="Classification API")
    parser.add_argument('--anaconda-project-address', action='append', default=[],
                        help='IP address the application should listen on')
    parser.add_argument('--anaconda-project-host', action='append', default=[],
                        help='Hostname to allow in requests')
    parser.add_argument('--anaconda-project-port', action='store', default=8086, type=int,
                        help='Port to listen on')
    parser.add_argument('--anaconda-project-iframe-hosts',
                        action='append',
                        help='Space-separated hosts which can embed us in an iframe per our Content-Security-Policy')
    parser.add_argument('--anaconda-project-no-browser', action='store_true',
                        default=False,
                        help='Disable opening in a browser')
    parser.add_argument('--anaconda-project-use-xheaders',
                        action='store_true',
                        default=False,
                        help='Trust X-headers from reverse proxy')
    parser.add_argument('--anaconda-project-url-prefix', action='store', default='',
                        help='Prefix in front of urls')

    args = parser.parse_args(sys.argv[1:])
    anaconda_project_hosts = args.anaconda_project_host
    anaconda_project_port = args.anaconda_project_port

    if len(anaconda_project_hosts) == 0:
        local_hosts = ['localhost', '127.0.0.1']
        anaconda_project_hosts = ['{}:{}'.format(host, anaconda_project_port) for host in local_hosts]

    define("port", default=anaconda_project_port, help="run on the given port", type=int)
    print("Tornado App running on port {} with accepted host: {}".format(anaconda_project_port, anaconda_project_hosts))
    main(anaconda_project_hosts)
