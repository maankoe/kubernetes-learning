# K8s learning
Done on mac, using minikube, docker, and kubectl


## Install minikube
```
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-darwin-amd64
```
and install it


## Start docker minikube
* Run docker desktop
```
minikube start
eval $(minikube docker-env)  # connect minikube to docker
```

## Build the images
```
docker build -f Dockerfile -t hello-python:latest .  # in app dir
docker build -f Dockerfile -t time-python:latest .   # in time dir
```

If the tag is updated (from latest) also update it on the image in `kubernetes/deployment.yaml`

## Deploy the services
```
kubectl create -f deployment.yaml  # in kubernetes dir
```

## Expose services to localhost and open browser
This is a minikube/mac thing from what I can tell

```
kubectl expose deployment time-deployment --type=LoadBalancer
kubectl expose deployment hello-deployment --type=LoadBalancer

minikube service time-service
minikube service hello-service
```

## Shut down the services and deployments
kubectl delete service time-service
kubectl delete deployment time-deployment
kubectl delete service hello-service
kubectl delete deployment hello-deployment


## General kubectl statuses
* kubectl
    * get
        * nodes
        * deployments
        * services
        * pods


## Clean up the exposed minikube service
Again minikube/mac specific from above

```
kubectl delete service time-deployment
kubectl delete service hello-deployment
```

## Stop minikube and docker
```
minikube stop
```
* Quit docker desktop, I guess
