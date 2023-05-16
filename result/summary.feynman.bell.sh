#!/bin/bash -l

basepath=/home/jiang631/data/scibench
datasource=Feynman
dates=2023-05-12
metric=neg_mse
python parse_results.py --fp $basepath/result/$datasource/$dates/ \
--metric $metric \
--dso_basepath $basepath/dso_classic \
--noise_type normal \
--noise_scale 0.0 \
--is_numbered 0
