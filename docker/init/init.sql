CREATE DATABASE IF NOT EXISTS course;

CREATE TABLE course.events
(
    event_time DateTime,
    user_id UInt32,
    event_type String,
    page String,
    device String
)
ENGINE = MergeTree
ORDER BY (event_time, user_id);