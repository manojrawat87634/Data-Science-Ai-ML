create table students (
    id bigint primary key auto_increment,
    name varchar(50),
    email varchar(200) not null unique,
    index email_idx(email));

CREATE TABLE marks (
     id bigint PRIMARY KEY auto_increment,
     student_id bigint,
     test_id INT,
     marks INT,
     FOREIGN KEY (student_id) REFERENCES students(id),
     INDEX idx_student (student_id),
     INDEX idx_test (test_id),
     INDEX idx_marks (marks)
 );

INSERT INTO students (name, email) VALUES
('Rahul Sharma', 'rahul@gmail.com'),
('Amit Verma', 'amit@gmail.com'),
('Neha Singh', 'neha@gmail.com'),
('Priya Gupta', 'priya@gmail.com'),
('Karan Mehta', 'karan@gmail.com'),
('Anjali Roy', 'anjali@gmail.com');

INSERT INTO marks (student_id, test_id, marks) VALUES
-- Test 1
(1, 101, 78),
(2, 101, 85),
(3, 101, 91),
(4, 101, 76),
(5, 101, 88),
(6, 101, 82),

-- Test 2
(1, 102, 84),
(2, 102, 80),
(3, 102, 89),
(4, 102, 79),
(5, 102, 92),
(6, 102, 86);


 SELECT
   *, 
    ROW_NUMBER() OVER (
        PARTITION BY m.test_id
        ORDER BY m.marks DESC
    ) as rank
FROM marks m
JOIN students s ON s.id = m.student_id;