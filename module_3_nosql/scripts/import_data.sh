#!/bin/bash

# Import JSON catalog data into MongoDB
mongoimport \
  --db catalog \
  --collection electronics \
  --file ../data/catalog.json
