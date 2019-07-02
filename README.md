# ambient_server

## Sample

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pprint
import requests

response = requests.get('http://co2-sensor-pi.local:5000')
pprint.pprint(response.json())
```
