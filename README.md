Dispatch API
============

Our dispatch API allows individual edge locations to access the latest dispatch
decisions made cloud-side.

Dispatched resources might include, for example:

* hard shutdown of a location or an individual microgrid component
* charging or discharging a battery
* activation or deactivation of balancing power
* activation or deactivation of a power plant

Microgrid controllers are expected to regularly query this API to keep up to
date with what resources the cloud wishes them to deploy.
