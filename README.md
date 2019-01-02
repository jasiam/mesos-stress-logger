## Mesos-stress-logger


Mesos-stress-logger is a simple docker application which you can use to test the logging solution associated to an Apache Mesos orchestration platform like Mesosphere DCOS. It creates folders containing stdout files based on the following parameters passed as environment variables to docker container:

* NUM_FILES: Specifies the number of stdout files you cant to be created
* LINES_TO_ADD: How many log lines do you want to append to stdout files for each iteration. Each line will end with the iterator index number.
* KEYWORD: Single word which will be inserted in the middle of the log message to make easier a later search on your final logs repository (e.g elasticsearch, mongodb, etc...)
* INTERVAL: Time interval (in seconds) the application will wait between logs insertion iteration.


### Usage

Ensure that you run the docker container in 1-N mesos-agent nodes:

$> docker run -d -e NUM_FILES=5 -e LINES_TO_ADD=3 -e KEYWORD=my_keyword -e INTERVAL=5 stresslogger:0.1.0

If you are using Marathon framework to run containers in your Mesos cluster, you can deploy it as a service using a deployment descriptor json as shown below:

```json
{
  "volumes": null,
  "id": "/stresslogger",
  "cmd": null,
  "args": null,
  "user": null,
  "env": {
    "NUM_FILES": "100",
    "LINES_TO_ADD": "5",
    "KEYWORD": "my_keyword",
    "INTERVAL": "2"
  },
  "instances": 1,
  "cpus": 1,
  "mem": 256,
  "disk": 0,
  "gpus": 0,
  "executor": null,
  "constraints": [
    [
      "hostname",
      "CLUSTER",
      "192.168.1.25"
    ]
  ],
  "fetch": null,
  "storeUrls": null,
  "backoffSeconds": 1,
  "backoffFactor": 1.15,
  "maxLaunchDelaySeconds": 3600,
  "container": {
    "docker": {
      "image": "stresslogger:0.1.0",
      "forcePullImage": false,
      "privileged": false,
      "network": "HOST"
    }
  },
  "healthChecks": null,
  "readinessChecks": null,
  "dependencies": null,
  "upgradeStrategy": {
    "minimumHealthCapacity": 1,
    "maximumOverCapacity": 1
  },
  "labels": null,
  "acceptedResourceRoles": null,
  "residency": null,
  "secrets": null,
  "taskKillGracePeriodSeconds": null,
  "portDefinitions": [
    {
      "protocol": "tcp",
      "port": 10006
    }
  ],
  "requirePorts": false
}
```
