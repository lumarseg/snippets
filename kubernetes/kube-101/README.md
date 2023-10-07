# KUBE-101

Kubernetes Fundamentals - 101

---

## Installation

Usefull information available at: [Canonical Install Kubernetes](https://ubuntu.com/kubernetes/install)

### Docker + Kuberbetes + WSL2

The easiest way to start Kubernetes at home !!! 🤓

1. Install Docker Destop for Windows
2. Select WSL2 instead of HyperV. WSL integrations requires select WSL distro in Settings / Resources / WSL integration.
3. Enable Kubernetes in Settings / Kubernetes

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

![Kubernetes Components](https://d33wubrfki0l68.cloudfront.net/2475489eaf20163ec0f54ddc1d92aa8d4c87c96b/e7c81/images/docs/components-of-kubernetes.svg)

Information about Components available at: [Kubernetes Components](https://kubernetes.io/docs/concepts/overview/components/)
