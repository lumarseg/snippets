# KUBE-101

Kubernetes Fundamentals - 101

---

## Installation

Alternatives to running Kubernetes in a local environment.

- Docker Desktop (Docker + Kubernetes + WSL2)
- K3s (The lightest Kubernetes, for ARM platform)
- Kind ()
- Minikube
- MicroK8s

Production / Cloud hosted.

- AWS EKS

---

### Docker Desktop (Docker + Kubernetes + WSL2)

| Infrastructure | Use case       | OS             |
| :------------- | :------------- | :------------- |
| `Laptops`, `Workstations` | Start learning, developers | **Linux**, **MAC**, **Windows** |

**Notes:** Docker dependent (It runs VM for MAC and Windows).

The easiest way to start Kubernetes at home !!! 👶

1. Install Docker Destop for Windows.
2. Select WSL2 instead of HyperV. WSL integrations requires: select WSL distro (Settings / Resources / WSL integration).
3. Enable Kubernetes (Settings / Kubernetes).

### K3s

| Infrastructure | Use case       | OS             |
| :------------- | :------------- | :------------- |
| `Laptops`, `IoT Devices` | For developer use, Low powered devices | **Linux** |

**Notes:** x86 & ARM, Linux Native.

(In progress...)

### Kind

| Infrastructure | Use case       | OS             |
| :------------- | :------------- | :------------- |
| `Laptops`, `Workstations` | For developer use | **Linux**, **MAC**, **Windows** |

**Notes:** Multinode, Docker dependent (It runs VM for MAC and Windows).

(In progress...)

### Minikube

| Infrastructure | Use case       | OS             |
| :------------- | :------------- | :------------- |
| `Laptops` | For developer use, | **Linux** |

**Notes:** Addons (ie: DNS, Prometheus ...), Linux Native.

(In progress...)

### MicroK8s (Ubuntu)

| Infrastructure | Use case       | OS             |
| :------------- | :------------- | :------------- |
| `Laptops`, `Workstations`, `Edge/Micro Cloud`, `IoT Devices` | Opinionated Kubernetes, Small to medium clusters, CI/CD pipelines | **Linux** |

**Notes:** Multinode, Addons (ie: DNS, Prometheus ...), x86 & ARM, Linux Native.

Install MicroK8s on Ubuntu Linux

```bash
  sudo snap install microk8s --classic
  sudo mkdir ~/.kube
  sudo usermod -a -G microk8s $USER
  sudo chown -R $USER ~/.kube
  newgrp microk8s
```

Check the status while Kubernetes starts

```bash
  microk8s status --wait-ready
```

Turn on the services you want

```bash
  microk8s enable dashboard dns registry istio
```

Start using Kubernetes

```bash
  microk8s kubectl get all --all-namespaces
```

Access the Kubernetes dashboard

```bash
  microk8s dashboard-proxy
```

Start and stop Kubernetes to save battery

```bash
  microk8s start
  microk8s stop
```

Usefull information available at: [Canonical Install Kubernetes](https://ubuntu.com/kubernetes/install)

### AWS EKS

| Infrastructure | Use case       | OS             |
| :------------- | :------------- | :------------- |
| `Public Cloud` | Traffic peaks | **Linux** |

(In progress...)

---

## Kubernetes Components

![Kubernetes Components](https://d33wubrfki0l68.cloudfront.net/2475489eaf20163ec0f54ddc1d92aa8d4c87c96b/e7c81/images/docs/components-of-kubernetes.svg)

Information about Components available at: [Kubernetes Components](https://kubernetes.io/docs/concepts/overview/components/)
