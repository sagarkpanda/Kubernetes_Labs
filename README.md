# Container Orchestration with Kubernetes

<!-- https://raw.githubusercontent.com/sagarkrp/sagarkrp/main/images/k8s.svg -->
<p align="center">
<img alt="K8s" width="200px" src="https://github.com/sagarkpanda/sagarkpanda/blob/main/images/k8s.png" style="padding-right:10px;" />
</p>
</br>
<h3> <strong> Read the detailed article on: </strong> </h3> <a href = "https://sagarcodectrl.medium.com/list/kubernetes-a0f8fab4ee0d" target ="_blank">

<picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://github.com/sagarkrp/sagarkrp/blob/main/images/Medium-white1x.png" width="160px" height="35px">
   <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/sagarkrp/sagarkrp/main/images/Medium-dark.svg" width="160px" height="35px">
   <img alt="Medium Alternative Theme." src="https://raw.githubusercontent.com/sagarkrp/sagarkrp/main/images/Medium-dark.svg" width="160px" height="35px">
</picture> </a>

<h1> What is Kubernetes: </h1>
Kubernetes, also known as K8s, is an open-source platform to automate deployment, scaling, and management of containerized applications or containers.

Containers are lightweight packages of an application including all the dependencies. Docker is one such platform for creating containerised applications.

<h1> Features of Kubernetes: </h1>

Container orchestration:
--------------
K8s automates the deployment and management of containers across a cluster of machines. It handles tasks such as container scheduling, scaling, load balancing, and rolling updates.

Service discovery and load balancing:
---------------------
K8s provides a built-in service discovery mechanism that allows containers to find and communicate with each other. It also offers load balancing capabilities to distribute incoming traffic across multiple instances of an application.

Scaling and self-healing:
------------------
K8s enables automatic scaling of application instances based on CPU usage, memory utilization, or custom metrics. It can also automatically restart containers that have failed, ensuring high availability of applications.

Configuration management:
------------------
K8s allows you to define and manage application configurations using declarative manifests. You can specify the desired state of your application, and Kubernetes will work to ensure that the actual state matches the desired state.

Storage orchestration:
-----------------
K8s provides a way to manage persistent storage volumes and attach them to containers as needed. This allows applications to store and retrieve data even when containers are rescheduled or restarted.

Health monitoring and logging:
---------------------
K8s offers tools for monitoring the health and performance of applications running in the cluster. It integrates with various logging and monitoring systems to collect and analyze container and application metrics.


<h1> Architecture of K8s: </h1>
<p allign='justified'>

```
                    +-----------------------+
                    |      Master Node      |
                    +-----------------------+
                    |                       |
                    |   +----------------+  |
                    |   |   API Server   |  |
                    |   +----------------+  |
                    |            |          |
                    |            |          |
                    |   +----------------+  |
                    |   |      etcd      |  |
                    |   +----------------+  |
                    |            |          |
                    |            |          |
                    |   +----------------+  |
                    |   | Controller Mgr |  |
                    |   +----------------+  |
                    |            |          |
                    |            |          |
                    |   +----------------+  |
                    |   |    Scheduler   |  |
                    |   +----------------+  |
                    +-----------------------+
                                |
                                |
                    +-------------------------+
                    |                         |
              +------------+            +------------+
              | Worker Node|            | Worker Node|
              +------------+            +------------+
              |   Kubelet  |            |   Kubelet  |
              |  Container |            |  Container |
              |   Runtime  |            |   Runtime  |
              | kube-proxy |            | kube-proxy |
              +------------+            +------------+
```
</p>
