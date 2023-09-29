CREATE DATABASE IF NOT EXISTS Communify;
USE Communify;
CREATE TABLE IF NOT EXISTS Users(
user_id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
user_name VARCHAR(50) NOT NULL,
user_lastname VARCHAR(50) NOT NULL,
user_nickname VARCHAR(50) NOT NULL,
user_email VARCHAR(50) NOT NULL,
user_password VARCHAR(255) NOT NULL,
user_birthday DATE NOT NULL,
user_profile_img VARCHAR(255)
) ENGINE= InnoDB;

CREATE TABLE IF NOT EXISTS Servers(
server_id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
server_name VARCHAR(50) NOT NULL,
server_description LONGTEXT
) ENGINE= InnoDB;

CREATE TABLE IF NOT EXISTS User_Server(
user_server_id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
user_id INT NOT NULL,
server_id INT NOT NULL,
CONSTRAINT users_fk FOREIGN KEY(user_id) REFERENCES Users(user_id),
CONSTRAINT servers_fk FOREIGN KEY (server_id) REFERENCES Servers(server_id)
) ENGINE= InnoDB;

CREATE TABLE IF NOT EXISTS Channels(
channel_id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
channel_name VARCHAR(50) NOT NULL,
channel_description LONGTEXT,
server_id INT NOT NULL,
CONSTRAINT server_fk FOREIGN KEY (server_id) REFERENCES Servers(server_id)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS Messages(
message_id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
message_content LONGTEXT,
message_history TIMESTAMP,
user_id INT NOT NULL,
channel_id INT NOT NULL,
CONSTRAINT user_fk FOREIGN KEY (user_id) REFERENCES Users(user_id),
CONSTRAINT channels_fk FOREIGN KEY (channel_id) REFERENCES Channels(channel_id)
) ENGINE = InnoDB;
