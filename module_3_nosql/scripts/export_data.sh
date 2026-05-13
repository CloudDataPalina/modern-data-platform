#!/bin/bash

# Export selected fields from MongoDB collection to CSV
mongoexport \
  --db catalog \
  --collection electronics \
  --type=csv \
  --fields _id,type,model \
  --out ../exports/electronics.csv
