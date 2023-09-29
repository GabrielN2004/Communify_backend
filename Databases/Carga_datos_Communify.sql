USE Communify;
INSERT INTO users (user_name, user_lastname, user_nickname, user_email, user_password, user_birthday)
VALUES ('Juan', 'Perez', 'Juancito', 'juanperez@gmail.com', 'scaloneta2022', '2004-04-04'),
('Maria', 'Lopez', 'Mary', 'marylopez@gmail.com', 'pelusa0979', '1974-07-29'),
('Ana', 'Diaz', 'anita', 'anadiaz@gmail.com','2413sofi', '1991-11-20');

INSERT INTO servers (server_name, server_description)
VALUES ('El mundo del K-POP', 'Comunidad centrada en el mundo del K-POP'),
('Harry Potter', 'Comunidad de fanaticos de la pelicula de Harry Potter');

INSERT INTO channels  (channel_name, channel_description, server_id)
VALUES ('The girls_BLACKPINK', 'Lugar donde conoceras a otros fanaticos',1),
('Stray kids', ' Canal destinada a obtener informacion actualizada del grupo Stray Kids',1),
('Gryffindor', 'Canal destinado a la casa de Gryffindor',2),
('Slytherin', 'Canal destinado a la casa de Slytherin',2);

insert into user_server ( user_id , server_id) values (1,1), (1,2), (2,2), (3,1);


