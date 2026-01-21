F5 script to grab LTM outputs and save during upgrades or maintenance.

### RUN:
python f5-show.py Device-HostnameorIP "show ltm pool recursive members"
python f5-show.py Device-HostnameorIP "show ltm node recursive"
python f5-show.py Device-HostnameorIP "show ltm recursive policy"
python f5-show.py Device-HostnameorIP "show ltm virtual recursive"
python f5-show.py Device-HostnameorIP "show ltm virtual-address recursive"
python f5-show.py Device-HostnameorIP "show sys connection"
python f5-show.py Device-HostnameorIP "show sys performance all-stats detail"
python f5-show.py Device-HostnameorIP "show ltm pool recursive members | grep 'Ltm::\|Availability\|State'"
python f5-show.py Device-HostnameorIP "show ltm node recursive | grep 'Ltm::\|Availability\|State'"
python f5-show.py Device-HostnameorIP "show ltm virtual recursive | grep 'Ltm::\|Availability\|State'"
python f5-show.py Device-HostnameorIP "show ltm virtual-address recursive | grep 'Ltm::\|Availability\|State'"
