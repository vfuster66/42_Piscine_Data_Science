DROP TABLE IF EXISTS items;

CREATE TABLE IF NOT EXISTS items (
    product_id INTEGER,
    category_id NUMERIC(20),
    category_code TEXT,
    brand VARCHAR(50)
);

\copy items FROM './item/item.csv' CSV HEADER;