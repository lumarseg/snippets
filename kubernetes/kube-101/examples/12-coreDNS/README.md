# CoreDNS Script

Please, take a look at: <https://github.com/coredns/deployment/tree/master/kubernetes>

## Deploy CoreDNS

In the best case scenario, all that's needed to replace Kube-DNS are these commands:

```console
./deploy.sh | kubectl apply -f -
kubectl delete --namespace=kube-system deployment kube-dns
```

## Rollback to kube-dns

These commands will deploy kube-dns replacing CoreDNS:

```comsole
./rollback.sh | kubectl apply -f -
kubectl delete --namespace=kube-system deployment coredns
```
