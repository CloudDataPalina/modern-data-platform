# Module 6 – Database Optimization, Security & Access Control

## 📌 Module Overview
This module focuses on **database performance optimization, security, and access control**.
It demonstrates how a Database Administrator improves query efficiency, reduces memory usage, enforces role-based access control, and protects sensitive data through encryption.

The module consists of **two practical labs**:
1. Database and query optimization
2. User access management and data encryption

---

## 🎯 Learning Objectives
- Optimize SQL queries using indexes and execution plans
- Analyze query performance with `EXPLAIN`
- Reduce memory usage by optimizing data types
- Execute table optimization commands
- Implement role-based access control (RBAC)
- Apply column-level security
- Encrypt and decrypt sensitive data using AES encryption

---

## 📁 Module Structure
```
module_5_security_optimization/
├── README.md                           ← Module documentation and explanation
│
├── lab_1_optimization/                 ← Database & query optimization
│ ├── commands/                         ← SQL commands used in the lab
│ │ └── optimization_commands.sql
│ │
│ └── screenshots/                      ← Performance and optimization evidence
│ ├── pre_indexing_output.jpg           ← Query execution before indexing
│ ├── index_creation.jpg                ← Index creation confirmation
│ ├── post_indexing_output.jpg          ← Query execution after indexing
│ ├── memory_before_editing.jpg         ← Memory usage before data type changes
│ ├── final_data_types.jpg              ← Optimized column data types
│ ├── memory_after_editing.jpg          ← Reduced memory usage
│ └── DimDate_optimized.jpg             ← OPTIMIZE TABLE execution
│
└── lab_2_security/                     ← Access control & encryption
├── commands/                           ← SQL commands used in the lab
│ └── security_commands.sql
│
└── screenshots/                        ← Security configuration evidence
├── db_admin_access.jpg                 ← Full admin privileges
├── db_analyst_access.jpg               ← Analyst role permissions
├── db_reporter_access.jpg              ← Read-only reporter access
├── db_external_database_level.jpg      ← External user (database-level access)
├── db_external_table_level.jpg         ← Column-level access control
├── encrypted_data_query.jpg            ← Encrypted data output
└── decrypted_data_query.jpg            ← Decrypted data output
```

---

## 🛠 Tools & Technologies
- MySQL – Relational database management system
- MySQL CLI – Query execution and optimization
- phpMyAdmin – User management and schema optimization
- SQL – Indexing, access control, and encryption
- AES Encryption – Data protection
- Cloud IDE (IBM Skills Network Labs) – Execution environment

---

## Lab 1 – Database & Query Optimization
### Description
This lab demonstrates how to **improve database performance and efficiency**.
Query execution is analyzed before and after indexing, memory usage is optimized by adjusting data types, and table optimization commands are applied.

### Key Activities
- Execute SQL queries with and without indexes
- Analyze execution plans using `EXPLAIN`
- Create indexes to improve query performance
- Optimize column data types to reduce memory usage
- Execute `OPTIMIZE TABLE` to improve table efficiency

### 📄 Commands Used
- Optimization commands:
  - [`optimization_commands.sql`](lab_1_optimization/commands/optimization_commands.sql)

### 🧪 Validation & Evidence
- Query performance comparison and memory optimization proof:
  - [`screenshots/`](lab_1_optimization/screenshots/)

---

## Lab 2 – Access Control & Data Encryption
### Description
This lab focuses on **database security and controlled access management**.
Multiple database users are created with different privilege levels, and sensitive sales data is protected using AES encryption.

### Key Activities
- Create database users with role-based permissions
- Assign full, limited, read-only, and column-level access
- Restrict access to sensitive columns
- Encrypt sensitive data using AES encryption
- Query encrypted data with and without decryption keys

### 📄 Commands Used
- Security and encryption commands:
  - [`security_commands.sql`](lab_2_security/commands/security_commands.sql)

### 🧪 Validation & Evidence
- User privileges and encryption verification:
  - [`screenshots/`](lab_2_security/screenshots/)

---

## 🎯 Skills Demonstrated
- SQL query optimization and indexing
- Execution plan analysis with `EXPLAIN`
- Memory optimization through data type tuning
- MySQL performance tuning fundamentals
- Role-based access control (RBAC)
- Column-level security implementation
- AES encryption and decryption
- Secure database administration practices

---

## 🔐 Security Note
All credentials, passwords, and encryption keys shown in this project are used **for educational purposes only**.
In production environments, secrets should be stored securely using environment variables or dedicated secret management solutions.

---

## ✅ Module Outcome
- Query performance significantly improved using indexing
- Database memory usage reduced through optimized schema design
- Secure user access implemented using role-based permissions
- Sensitive data protected through encryption
- Database optimized for performance, security, and reliability
