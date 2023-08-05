kctl expose deployment mywebapp --target-port=80 --port=80 --type=LoadBalancer

$kctl rollout history deployment/mywebapp

$kctl rollout undo deployment/mywebapp

$kctl rollout undo deployment/mywebapp --to-revision 1
