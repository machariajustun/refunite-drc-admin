#!/bin/sh
nose2 --coverage refunite_drc_admin --with-coverage -v
flake8 refunite_drc_admin tests
