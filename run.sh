#!/bin/bash
set -ex
uxnasm locomotion.tal locomotion.rom 
./receiver.py | uxnemu -3x ./locomotion.rom | ./hextee | ./sender.py
