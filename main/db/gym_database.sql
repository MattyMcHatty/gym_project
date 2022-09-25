DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS classes;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    premium BOOLEAN,
    active BOOLEAN
);

CREATE TABLE classes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    date DATE,
    capacity INT
);

CREATE TABLE bookings(
    id SERIAL PRIMARY KEY,
    member_id SERIAL NOT NULL REFERENCES members(id),
    class_id SERIAL NOT NULL REFERENCES classes(id)
);

