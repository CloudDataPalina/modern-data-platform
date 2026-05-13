// Use catalog database
use catalog

// List all databases
show dbs

// List collections in catalog database
show collections

// Show first 5 documents
db.electronics.find().limit(5).pretty()

// Create index on type field
db.electronics.createIndex({ type: 1 })

// Count laptops
db.electronics.countDocuments({ type: "laptop" })

// Count smartphones with 6-inch screen
db.electronics.countDocuments({
  type: "smart phone",
  "screen size": 6
})

// Calculate average smartphone screen size
db.electronics.aggregate([
  { $match: { type: "smart phone" } },
  { $group: { _id: "$type", avg_screen_size: { $avg: "$screen size" } } }
])
