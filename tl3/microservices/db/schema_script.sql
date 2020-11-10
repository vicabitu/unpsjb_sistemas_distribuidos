CREATE TABLE cookies(
    key character(36) PRIMARY KEY, 
    value character(36) NOT NULL
);


CREATE TABLE users(
    id serial PRIMARY KEY, 
    name character(70) NOT NULL,
    username character(70) NOT NULL,
    age integer NOT NULL, 
    password character(20) NOT NULL
);

INSERT INTO users (name, age, username, password) 
  VALUES ('Pedro Konstantinoff',36,'pedro','un_password'); 

SELECT * FROM users;
