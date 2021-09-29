#!/usr/bin/env bash
   # pragma: no cover
set -e
set -x

bash scripts/test.sh \
    --cov=src/farm \
    --cov-config=.coveragerc \
    --cov-report=html \
    ${@}