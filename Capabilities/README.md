kctl run pod1 --image=nginx
kctl run pod2--image=nginx
kctl get pods

----------------------------

sagar [ ~ ]$ kctl get pods
NAME  READY   STATUS    RESTARTS   AGE     IP            NODE                               
pod1   1/1     Running   0          7m28s   10.244.1.15   aks-agentpool-68606885-vmss000000  
pod2   1/1     Running   0          8m26s   10.244.1.14   aks-agentpool-68606885-vmss000000 

----------------------------

$kctl exec -it pod1 bash

inside pod
apt update
apt install iputils-ping

----------------------------

kctl get pods -o wide

NAME       READY   STATUS    RESTARTS   AGE   IP            
pod3       1/1     Running   0          12s   10.244.1.16 

----------------------------

securityContext:
     capabilities:
      drop: ["NET_RAW", "KILL"]



securityContext:
     capabilities:
      add: ["NET_RAW", "KILL"]

