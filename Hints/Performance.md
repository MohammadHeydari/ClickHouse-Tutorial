# Performance Tips
- Always use MergeTree family engines for large datasets
- Define a good ```ORDER BY``` (this is your primary index!)
- Use ```PARTITION BY``` wisely (don’t over-partition)
- Avoid too many small inserts - > batch your data
- Use ```LIMIT``` when exploring data