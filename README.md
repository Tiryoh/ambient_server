# ambient_server

## Requirements

* [Tiryoh/ambient_logger](https://github.com/Tiryoh/ambient_logger)

## Sample

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pprint
import requests

response = requests.get('http://co2-sensor-pi.local:5000')
pprint.pprint(response.json())
```

## License

(C) 2019 Tiryoh

This repository is released under the MIT license, see [LICENSE](./LICENSE).  
Unless attributed otherwise, everything in this repository is under the MIT license.
