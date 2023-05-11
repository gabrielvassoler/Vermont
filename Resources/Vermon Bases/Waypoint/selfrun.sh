#!/bin/bash
for counter in $(seq 1 10); do
  sudo make run
  sudo make stop
  sudo make clean
done
