import json
import time
from redis import Redis
redis = Redis(host='redis', port=6379)
try:
  f = open('/usr/tsunami/logs/tsunami-output.json',)
  data = json.load(f)
  redis.set('vulnerabilities', len(data['scanFindings']))
  f.close()
except:
  print("File doesn't exist yet. Sleep for one min")
  time.sleep(60)



