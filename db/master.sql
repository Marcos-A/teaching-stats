-- Create master schema
DROP SCHEMA IF EXISTS master CASCADE;

CREATE SCHEMA IF NOT EXISTS master AUTHORIZATION postgres;

GRANT ALL ON SCHEMA master TO postgres;

SET search_path TO master;

BEGIN WORK;

SET TRANSACTION READ WRITE;

-- Create tables at master schema
CREATE TABLE department(
    id SMALLINT,
    code VARCHAR(3),
    name VARCHAR(75),
CONSTRAINT department_pkey PRIMARY KEY(id)
);

CREATE TABLE level(
    id SMALLINT,
    name VARCHAR(25),
    code VARCHAR(3),
CONSTRAINT level_pkey PRIMARY KEY(id)
);


CREATE TABLE degree(
    id SMALLINT,
    code VARCHAR(4),
    name VARCHAR(75),
    department_id SMALLINT,
    level_id SMALLINT,
CONSTRAINT degree_pkey PRIMARY KEY(id),
CONSTRAINT FK_degree_department_id FOREIGN KEY(department_id) REFERENCES department(id),
CONSTRAINT FK_degree_level_id FOREIGN KEY(level_id) REFERENCES level(id)
);

CREATE TABLE "group"(
    id INTEGER,
    name VARCHAR(5),
    degree_id SMALLINT,
CONSTRAINT group_pkey PRIMARY KEY(id),
CONSTRAINT FK_group_degree_id FOREIGN KEY(degree_id) REFERENCES degree(id)
);

CREATE TABLE topic(
    id SMALLINT,
    name VARCHAR(25),
CONSTRAINT topic_pkey PRIMARY KEY(id)
);

CREATE TABLE type(
    id SMALLINT,
    name VARCHAR(25),
CONSTRAINT question_type_pkey PRIMARY KEY(id)
);

CREATE TABLE question(
    id SMALLINT,
    sort SMALLINT,
    statement TEXT,
    disabled TIMESTAMPTZ,
    type_id SMALLINT,
    level_id SMALLINT,
    topic_id SMALLINT,
    created TIMESTAMPTZ,
CONSTRAINT question_pkey PRIMARY KEY(id),
CONSTRAINT FK_question_level_id FOREIGN KEY(level_id) REFERENCES level(id),
CONSTRAINT FK_question_topic_id FOREIGN KEY(topic_id) REFERENCES topic(id),
CONSTRAINT FK_question_type_id FOREIGN KEY(type_id) REFERENCES type(id)
);

CREATE TABLE student(
    id INTEGER,
    email VARCHAR(75),
    name VARCHAR(50),
    surname VARCHAR(50),
    group_id SMALLINT,
CONSTRAINT student_pkey PRIMARY KEY(id),
CONSTRAINT FK_student_group_id FOREIGN KEY(group_id) REFERENCES "group"(id),
CONSTRAINT CH_student_unique_email UNIQUE(email)
);

CREATE TABLE subject(
    id SMALLINT,
    code VARCHAR(10),
    name VARCHAR(75),
    degree_id SMALLINT,
    topic_id SMALLINT,
CONSTRAINT subject_pkey PRIMARY KEY(id),
CONSTRAINT FK_subject_degree_id FOREIGN KEY(degree_id) REFERENCES degree(id),
CONSTRAINT FK_subject_topic_id FOREIGN KEY(topic_id) REFERENCES topic(id)
);

CREATE TABLE subject_student(
    subject_id SMALLINT,
    student_id INTEGER,
CONSTRAINT subject_student_pkey PRIMARY KEY(subject_id, student_id),
CONSTRAINT FK_subject_student_student_id FOREIGN KEY(student_id) REFERENCES student(id),
CONSTRAINT FK_subject_student_subject_id FOREIGN KEY(subject_id) REFERENCES subject(id)
);

CREATE TABLE trainer(
    id SMALLINT,
    name VARCHAR(75),
CONSTRAINT trainer_pkey PRIMARY KEY(id)
);

CREATE TABLE subject_trainer(
    subject_id SMALLINT,
    trainer_id SMALLINT,
CONSTRAINT subject_trainer_pkey PRIMARY KEY(subject_id, trainer_id),
CONSTRAINT FK_subject_trainer_subject_id FOREIGN KEY(subject_id) REFERENCES subject(id),
CONSTRAINT FK_subject_trainer_trainer_id FOREIGN KEY(trainer_id) REFERENCES trainer(id)
);

COMMIT;
