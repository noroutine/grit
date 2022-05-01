from grit import *

from grafanalib.core import (
    Graph, Target
)

someOtherPanel = somePanel = Graph(
    title="Oplog Lag",
    lineWidth=2,
    targets=[
        Target(
            expr="rate(mongodb_mongod_replset_oplog_head_timestamp[5m])",
            legendFormat='{{ instance }}'
        )
    ],
)

GritDash(
    uid="jmeter-grafanalib",
    version=8,
    title="jmeter (grafanalib)",
    description="Your description",
    tags=[
        'prometheus'
    ],
    timezone="browser",
    dataSource="Prometheus",
    stack=Stack(
        row8(somePanel)
    )
)


