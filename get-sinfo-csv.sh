#!/usr/bin/bash
# sinfo -h --format="[%n--%c CPUs,%Y Cores|Memory=%m,State=%a,Load=%O,partition:%P\")" #human-readable
# sinfo --format="%n,%c,%Y,%m,%T,%O,%P" | sort -r > sinfo.csv
sinfo --format="%n,%c,%Y,%m,%T,%O,%G,%C" | sort -r > sinfo.csv
