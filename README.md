# Decisions


## Flask

Why Flask ?

Micro python webframework,
no steep learning curve and serves
the purpose of this task, as well as,
many enterprises.

Also, a long-long time ago, a savant
techie friend of mine told me about
it, in response to me talking about 
using Django for a simple project.

Django was definitely an overkill
on the baseline resource level.

His remark still stands true today.

Flask does not aim to offer every
function a monolithic webframework
may, rather it does the "web" part
of the webframework exceptionally
well.


## Ansible

Why Ansible ?

Ansible is very ~~pervasive~~ resilient, in a sense, that AWS adopted it for playbooks,
therefore it's, as solid, as ever of configuration framework and IaC now too.


## Prometheus

>Note (humorous):

If the /metrics requests counters turn into a run away train,

I promise it is not the Prometheus Counter logic, it's the Mirai's successor IoT B0tnet

Confirmed on localhost, counters don't change without refreshes over cputime lightyears


## Site (tree)

```
/gandalf
└── Gandalf's picture 

/colombo
└── Colombo's current time

/metrics
├── gandalf_requests_total
└── colombo_requests_total
```


## References

https://flask.palletsprojects.com/en/stable/quickstart/#a-minimal-application

https://docs.python.org/3.9/library/zoneinfo.html

https://prometheus.github.io/client_python/

https://prometheus.github.io/client_python/exporting/http/flask/

https://prometheus.github.io/client_python/instrumenting/counter/