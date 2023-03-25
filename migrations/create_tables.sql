CREATE TABLE IF NOT EXISTS health (
    id serial PRIMARY KEY,
    YearStart INTEGER,
    YearEnd INTEGER,
     LocationAbbr VARCHAR, 
     LocationDesc VARCHAR, 
     Topic VARCHAR,
    Question VARCHAR,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)