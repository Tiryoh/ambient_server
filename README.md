# ambient_server

## Requirements

* [Tiryoh/ambient_logger](https://github.com/Tiryoh/ambient_logger)

## Usage

Install the requirements first.

After that, just run the followings:
```sh
./sensor_server.py
```

## Samples to get data from this server

Replace `co2-sensor-pi` to the hostname of the server.

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pprint
import requests

response = requests.get('http://co2-sensor-pi.local:5000/api/v1/ambient')
pprint.pprint(response.json())
```

```sh
#!/usr/bin/env bash
set -eu
curl -Ss http://co2-sensor-pi.local:5000/api/v1/ambient
```

## API

### `/api/v1/ambient`

* URL
  * `/api/v1/ambient`
* Return-Type
  * `application/json`

## License

(C) 2019 Tiryoh

This repository is released under the MIT license, see [LICENSE](./LICENSE).  
Unless attributed otherwise, everything in this repository is under the MIT license.
