DROP DATABASE IF EXISTS adopt;

CREATE DATABASE adopt;

\c adopt

CREATE TABLE pets
(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    species TEXT NOT NULL,
    photo_url TEXT,
    age INT,
    notes TEXT,
    available BOOLEAN NOT NULL DEFAULT TRUE
);

INSERT INTO pets
(name, species, photo_url, age, notes, available)
VALUES
('Sparky', 'dog', 'https://vetsource.com/wp-content/uploads/2018/11/img-pet-adoption-101.jpg', 2, 'Super gentle. Already potty trained!', 't'),
('Valentina', 'dog', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSjMD_t9BGEGinm718nX-8hFwWscBnF8ALsIA&usqp=CAU', 3, 'Very loving, like luxurious surroundings.', 't'),
('Juicy', 'cat', 'https://ca-times.brightspotcdn.com/dims4/default/0c2f8d6/2147483647/strip/true/crop/1611x846+0+30/resize/1200x630!/quality/90/?url=https%3A%2F%2Fcalifornia-times-brightspot.s3.amazonaws.com%2Ffd%2Fef%2F05c1aab3e76c3d902aa0548c0046%2Fla-la-hm-pet-issue-18-jpg-20150615', 2, 'Loves tuna!', 't');