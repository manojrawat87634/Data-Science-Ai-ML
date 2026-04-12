create table student (
     id bigint primary key auto_increment,
     name varchar(100) not null,
     email varchar(200) not null unique,
     phone varchar(20) not null unique,
     created_at datetime default now(),
      index email_idx(email),
      index phone_idx(phone));


create table courses
 ( id bigint primary key auto_increment, name varchar(200) not null unique);


CREATE TABLE course_pricing (
    id bigint PRIMARY KEY AUTO_INCREMENT,
    course_id bigint,
    price DECIMAL(10,2),
    currency VARCHAR(10),
    valid_from DATETIME,
    valid_to DATETIME,
    FOREIGN KEY (course_id) REFERENCES courses(id)
);


CREATE TABLE modules (
    id bigint PRIMARY KEY AUTO_INCREMENT,
    module_name VARCHAR(100)
);


CREATE TABLE course_modules (
    course_id BIGINT,
    module_id BIGINT,
    total_classes INT,   -- 🔥 THIS IS WHAT YOU NEED
    PRIMARY KEY (course_id, module_id),
    FOREIGN KEY (course_id) REFERENCES courses(id),
    FOREIGN KEY (module_id) REFERENCES modules(id)
);


CREATE TABLE enrollments (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    student_id BIGINT,
    course_id BIGINT,
    enrolled_at DATETIME DEFAULT NOW(),

    FOREIGN KEY (student_id) REFERENCES student(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);
