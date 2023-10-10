#!/bin/bash

aws cloudformation describe-stacks --stack-name eksClusterDemo
cp ~/.kube/config ~/.kube/config.bak
aws eks update-kubeconfig --name eksClusterDemo
