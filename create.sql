CREATE TABLE Teachers(username VARCHAR(30) NOT NULL PRIMARY KEY,
            		      name VARCHAR(100) NOT NULL,
            		      password VARCHAR(100) NOT NULL,
            		      location VARCHAR(800),
            		      subjects VARCHAR(100),
            		      education_level VARCHAR(100),
            		      bio VARCHAR(200),
            		      maiden VARCHAR(800) NOT NULL);

CREATE TABLE Resources(resource_id VARCHAR(30) NOT NULL,
            		       teacher_id VARCHAR(30) NOT NULL REFERENCES Teachers(username),
            		       resource_name VARCHAR(500) NOT NULL,
            		       category VARCHAR(100),
                       subject VARCHAR(100),
                       education_level VARCHAR(100),
            		       file VARCHAR(1000),
            		       description VARCHAR(2000),
            		       date_posted VARCHAR(100),
            		       PRIMARY KEY(resource_id, teacher_id));

CREATE TABLE Reviews(review_id SERIAL PRIMARY KEY,
                     resource_id VARCHAR(30) NOT NULL,
                     teacher_id VARCHAR(30) NOT NULL,
                     reviewer_username VARCHAR(30),
                     item_rating INTEGER NOT NULL CHECK(item_rating > 0 AND item_rating <= 5),
                     comments VARCHAR(2000),
                     FOREIGN KEY(teacher_id, resource_id) REFERENCES Resources(teacher_id, resource_id));

#CREATE TABLE Forumns()

INSERT INTO Teachers VALUES('janiston', 'Rachel Green', 'StrongPassword', 'Duke', 'Math', 'Undergraduate', 'I am not qualified for this', 'Rachel');
INSERT INTO Teachers VALUES('jtribbiani', 'Joey Tribbiani', 'StrongPassword', 'UNC', 'Food Studies', 'Undergraduate', 'How ya doin?', 'Joanna');
INSERT INTO Teachers VALUES('rgeller', 'Ross Geller', 'StrongPassword', 'Wheeler High School', 'Archaeology', 'Tenth Grade', 'Fossils are pretty cool', 'Ronie');
INSERT INTO Teachers VALUES('mgeller', 'Monica Geller', 'StrongPassword', 'Highland Ranch Elementary School', 'Physics, English', 'First Grade', 'I hate online teaching!', 'Monica');
INSERT INTO Teachers VALUES('cbing', 'Chandler Bing', 'StrongPassword', 'Harvard', 'Math, Dance', 'Graduate', 'Looking for someone to teach me how to teach', 'Cherry');
INSERT INTO Teachers VALUES('pbuffay', 'Phoebe Buffay', 'StrongPassword', 'Duke', 'Computer Science', 'Undergraduate', 'I code with my nose', 'Patoony');
