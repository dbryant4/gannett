#!/bin/bash
set -ex

cd project-src/app

export PYTHONPATH=.

pip install -r requirements.txt -r tests/requirements.txt
pytest -v tests
