# knative-api-events-functions

Triggering knative function as a result of changes of Virtual Machine resources and display the content of (Mirtual Machine) Cloud Event

## Overview

The contents of this repository demonstrates how to use a Knative [ApiServerSource](https://knative.dev/docs/eventing/sources/apiserversource/) to trigger Knative [function](https://knative.dev/docs/functions/) when changes of OpenShift Virtual Machines (kubevirt) events are received.

An overview of the architecture can be found below:

![Overall Architecture](/images/architecture.png)

## Prerequisites

The following prerequisites must be satisfied prior to deploying the solution contained within this repository

1. OpenShift Cluster
2. Access to an OpenShift Cluster with `cluster-admin` privileges
3. Installation of OpenShift Serverless (Knative)
4. Installation of Knative Eventing
5. 4. Installation of Knative Serving
6. Installaton of OpenShift Virtulization (kubevirt)
7. OpenShift  Command Line Interfaces (cli) 

## Installation

1. Create a new namespace 

```shell
oc apply -f namespaces/apiserversource-example.yaml
```

2. Apply Knative resources

```shell
oc apply -f knative
```

## Validation
Verify the integration by deploying a (kubevirt) Virtual Machine  to trigger the knative function