# Date time +7 Vietnam time

```python
import dateutil, datetime
def tt(): return datetime.datetime.now(dateutil.tz.tzoffset(None, 7*60*60)) 
stime=tt().strftime('%Y-%m-%d  %H:%M:%S')   #'2020-02-23  00:08:27' 
stime
```
