# General Best Practices
- Prefer columnar thinking: select only the columns you need
- Avoid ```SELECT *``` in production queries
- Use appropriate data types (e.g., ```UInt32``` instead of ```Int64``` if possible)
- Keep queries simple and readable