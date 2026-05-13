# Module 3 – NoSQL Data Repository

## 📌 Module Overview
This module demonstrates how MongoDB can be used as a NoSQL document database for storing and querying semi-structured e-commerce catalog data.

The module covers JSON data ingestion, collection management, indexing, analytical queries, and CSV export using MongoDB command-line tools.

## 🎯 Objectives
- Import JSON catalog data into MongoDB
- Create and manage a MongoDB database and collection
- Query semi-structured document data
- Create an index for query optimization
- Export selected document fields into CSV format

## 🛠 Tools & Technologies
- MongoDB
- mongoimport
- mongoexport
- JavaScript / Mongo Shell
- JSON
- CSV

## 📁 Module Structure
```text
module_3_nosql/
├── README.md
├── data/
│   └── catalog.json
├── scripts/
│   ├── import_data.sh
│   ├── queries.js
│   └── export_data.sh
├── exports/
│   └── electronics.csv
└── screenshots/
```

## 📥 Data Import

```bash
mongoimport --db catalog --collection electronics --file catalog.json
```
**Output:**
```text
438 document(s) imported successfully. 0 document(s) failed to import.
```

## 🗄 Database and Collection Validation

```javascript
show dbs
use catalog
show collections
```
The MongoDB server contained the catalog database and the electronics collection after import.


## ⚡ Index Creation
```javascript
db.electronics.createIndex({ type: 1 })
```
An index was created on the type field to support faster filtering by product category.


## 🔎 Analytical Queries

### Count laptops
```javascript
db.electronics.countDocuments({ type: "laptop" })
```

### Count smartphones with 6-inch screen
```javascript
db.electronics.countDocuments({
  type: "smart phone",
  "screen size": 6
})

```
**Output:**
```text
8
```

### Average smartphone screen size
```javascript
db.electronics.aggregate([
  { $match: { type: "smart phone" } },
  { $group: { _id: "$type", avg_screen_size: { $avg: "$screen size" } } }
])

```
**Output:**
```text
{ _id: "smart phone", avg_screen_size: 6 }
```

## 📤 CSV Export

```bash
mongoexport --db catalog --collection electronics --type=csv --fields _id,type,model --out electronics.csv
```
**Output:**
```text
connected to mongodb://localhost/
exported 438 records
```

## 📸 Screenshots

This module includes screenshots demonstrating:

- [importdata.png](screenshots/importdata.png) – JSON data import into MongoDB
- [database_validation.png](screenshots/database_validation.png) – database and collection validation
- [createindex.png](screenshots/createindex.png) – index creation on the `type` field
- [analytical_queries.png](screenshots/analytical_queries.png) – aggregation and analytical queries
- [exportcsv.png](screenshots/exportcsv.png) – CSV export operation
- [electronicscsv.png](screenshots/electronicscsv.png) – exported CSV verification

Screenshots are available in the screenshots/ directory.


## ▶ Execution Order

1. Download [`catalog.json`](data/catalog.json)
2. Execute [`import_data.sh`](scripts/import_data.sh) to import JSON data into MongoDB
3. Validate databases and collections using [`queries.js`](scripts/queries.js)
4. Create an index on the `type` field
5. Execute aggregation and analytical queries
6. Run [`export_data.sh`](scripts/export_data.sh) to export selected fields into CSV format
7. Verify exported [`electronics.csv`](exports/electronics.csv)
   

## ✅ Module Outcome
- JSON catalog data successfully imported into MongoDB
- MongoDB database and collection validated
- Index created on the type field
- Aggregation and analytical queries executed on semi-structured document data
- Selected fields exported from MongoDB into CSV format

