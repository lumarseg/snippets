#!/bin/bash

aws cloudformation describe-stacks --stack-name kubernetes-demo
cp ~/.kube/config ~/.kube/config.bak
aws eks update-kubeconfig --name kubernetes-demo
