# Crazy Firewall
When you launch it, the script opens multiple ports on your system.
If you scan your system you will see them. Use it in controlled environments under your responsibility.

## How to run

```shell
python crazy_firewall.py

...
PORT 49416 open
PORT 46817 open
PORT 34318 open
PORT 48188 open
PORT 39966 open
PORT 46194 open
PORT 16789 open
PORT 16497 open
PORT 16298 open
...
Check...
Check...
Check...
```

And then scan your localhost

```shell
netstat -plutn | grep "LISTEN"

...
tcp        0      0 0.0.0.0:55169           0.0.0.0:*               LISTEN      25444/nc
tcp        0      0 0.0.0.0:11521           0.0.0.0:*               LISTEN      25269/nc
tcp        0      0 0.0.0.0:30977           0.0.0.0:*               LISTEN      25023/nc
tcp        0      0 0.0.0.0:54433           0.0.0.0:*               LISTEN      24856/nc
tcp        0      0 0.0.0.0:64321           0.0.0.0:*               LISTEN      24566/nc
tcp        0      0 0.0.0.0:36641           0.0.0.0:*               LISTEN      24560/nc
tcp        0      0 0.0.0.0:25761           0.0.0.0:*               LISTEN      24536/nc
tcp        0      0 0.0.0.0:64737           0.0.0.0:*               LISTEN      24454/nc
tcp        0      0 0.0.0.0:32353           0.0.0.0:*               LISTEN      24263/nc
tcp        0      0 0.0.0.0:51425           0.0.0.0:*               LISTEN      24124/nc
tcp        0      0 0.0.0.0:4610            0.0.0.0:*               LISTEN      25532/nc
tcp        0      0 0.0.0.0:27906           0.0.0.0:*               LISTEN      25481/nc
tcp        0      0 0.0.0.0:46978           0.0.0.0:*               LISTEN      25393/nc
tcp        0      0 0.0.0.0:63490           0.0.0.0:*               LISTEN      25344/nc
tcp        0      0 0.0.0.0:49762           0.0.0.0:*               LISTEN      25290/nc
tcp        0      0 0.0.0.0:8898            0.0.0.0:*               LISTEN      24972/nc
tcp        0      0 0.0.0.0:41058           0.0.0.0:*               LISTEN      24957/nc
tcp        0      0 0.0.0.0:58690           0.0.0.0:*               LISTEN      24878/nc
tcp        0      0 0.0.0.0:25282           0.0.0.0:*               LISTEN      24733/nc
tcp        0      0 0.0.0.0:4034            0.0.0.0:*               LISTEN      24693/nc
tcp        0      0 0.0.0.0:2146            0.0.0.0:*               LISTEN      24425/nc
tcp        0      0 0.0.0.0:58754           0.0.0.0:*               LISTEN      24392/nc
tcp        0      0 0.0.0.0:31010           0.0.0.0:*               LISTEN      24353/nc
tcp        0      0 0.0.0.0:17890           0.0.0.0:*               LISTEN      24331/nc
tcp        0      0 0.0.0.0:9762            0.0.0.0:*               LISTEN      24314/nc
tcp        0      0 0.0.0.0:45954           0.0.0.0:*               LISTEN      24300/nc
...
```

Good luck.