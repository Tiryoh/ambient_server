#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import argparse
import urllib.parse as urlparse
from http.server import BaseHTTPRequestHandler, HTTPServer

VERSION = '0.0.4'


def get_co2_sensor_data():
    with open('/dev/shm/logger_co2', 'r') as f:
        return int(f.readline())

def get_temp_sensor_data():
    with open('/dev/shm/logger_temp', 'r') as f:
        return int(f.readline())

def get_hum_sensor_data():
    with open('/dev/shm/logger_hum', 'r') as f:
        return int(f.readline())

def get_sensor_timestamp():
    with open('/dev/shm/logger_timestamp', 'r') as f:
        return f.readline().strip()

def calc_thi(temperature, humidity):
    return int(0.81 * temperature + 0.01 * \
               humidity * (0.99 * temperature - 14.3) + 46.3)


class JsonResponsehandler(BaseHTTPRequestHandler):
    def __init__(self, *args):
        BaseHTTPRequestHandler.__init__(self, *args)

    def do_GET(self):
        uri = self.path
        uri_arg = urlparse.parse_qs(urlparse.urlparse(uri).query, keep_blank_values=True)
        if uri == "/api/v1/ambient":
            sensor_dict = {
                "ambient": {
                    "co2": get_co2_sensor_data(),
                    "temperature": get_temp_sensor_data(),
                    "humidity": get_hum_sensor_data(),
                },
                "timestamp": get_sensor_timestamp()
            }
            body = json.dumps(sensor_dict)
            print(body)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header("Content-length", len(body))
            self.end_headers()
            self.wfile.write(body.encode("UTF-8"))
        elif uri == "/api/v1/thi":
            sensor_dict = {
                "thi": calc_thi(get_temp_sensor_data(), get_hum_sensor_data()),
                "timestamp": get_sensor_timestamp()
            }
            body = json.dumps(sensor_dict)
            print(body)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header("Content-length", len(body))
            self.end_headers()
            self.wfile.write(body.encode("UTF-8"))
        else:
            body = "API Not Found.\nSee https://github.com/Tiryoh/ambient_server/blob/master/README.md#api\n"
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.send_header("Content-length", len(body))
            self.end_headers()
            self.wfile.write(body.encode("UTF-8"))

def main():
    parser = argparse.ArgumentParser(description="usage:set JSON responce server port e.g.) '--port 5000' or '-p 5000'")
    parser.add_argument("-p", "--port", type=int, default=5000, help="define TCP port")
    parser.add_argument("--version", action="version", version="ambient_server v" + VERSION)
    args = parser.parse_args()

    server = HTTPServer(("", args.port), JsonResponsehandler)
    print("ambient_server v" + VERSION + " running on port " + str(args.port))
    server.serve_forever()


if __name__ == '__main__':
    main()
