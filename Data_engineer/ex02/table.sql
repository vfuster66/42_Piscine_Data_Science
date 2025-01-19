CREATE TABLE IF NOT EXISTS data_2022_oct (
    event_time TIMESTAMP WITH TIME ZONE,
    event_type VARCHAR(50),
    product_id INTEGER,
    price DECIMAL(10,2),
    user_id BIGINT,
    user_session UUID
);

\copy data_2022_oct FROM './customer/data_2022_oct.csv' CSV HEADER;