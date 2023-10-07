# KUBE-101

Kubernetes Fundamentals - 101

---

## Installation

Usefull information available at: [Canonical Install Kubernetes](https://ubuntu.com/kubernetes/install)

### MicroK8s (Ubuntu)

1. Install MicroK8s on Ubuntu Linux

```bash
  sudo snap install microk8s --classic
  sudo mkdir ~/.kube
  sudo usermod -a -G microk8s $USER
  sudo chown -R $USER ~/.kube
  newgrp microk8s
```

2. Check the status while Kubernetes starts

```bash
  microk8s status --wait-ready
```

3. Turn on the services you want

```bash
  microk8s enable dashboard dns registry istio
```

4. Start using Kubernetes

```bash
  microk8s kubectl get all --all-namespaces
```

5. Access the Kubernetes dashboard

```bash
  microk8s dashboard-proxy
```

6. Start and stop Kubernetes to save battery

```bash
  microk8s start
  microk8s stop
```

---

## Kubernetes Components

![Kubernetes Components](https://www.google.co.cr/url?sa=i&url=https%3A%2F%2Fkubernetes.io%2Fdocs%2Fconcepts%2Foverview%2Fcomponents%2F&psig=AOvVaw0JOlL8D5Spv2L0KRZckjZm&ust=1696801399641000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCLDluPjz5IEDFQAAAAAdAAAAABAE)