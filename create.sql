CREATE TABLE Reviews(review_id SERIAL PRIMARY KEY,
                     resource_id VARCHAR(30) NOT NULL,
                     teacher_id VARCHAR(30) NOT NULL,
                     reviewer_username VARCHAR(30),
                     item_rating INTEGER NOT NULL CHECK(item_rating > 0 AND item_rating <= 5),
                     comments VARCHAR(2000),
                     FOREIGN KEY(teacher_id, resource_id) REFERENCES Resources(teacher_id, resource_id));

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
            		       file VARCHAR(1000),
            		       description VARCHAR(2000),
            		       date_posted VARCHAR(100),
            		       PRIMARY KEY(resource_id, teacher_id));
