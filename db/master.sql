-- Create master schema
CREATE SCHEMA IF NOT EXISTS master;

SET search_path TO master;

BEGIN WORK;

SET TRANSACTION READ WRITE;

-- Create tables at master schema
CREATE TABLE department(
    id SERIAL,
    code VARCHAR(3) NOT NULL,
    name VARCHAR(75) NOT NULL,
CONSTRAINT department_pkey PRIMARY KEY(id),
CONSTRAINT UQ_department_unique_code UNIQUE(code),
CONSTRAINT UQ_department_unique_name UNIQUE(name)
);

CREATE TABLE level(
    id SERIAL,
    name VARCHAR(25) NOT NULL,
    code VARCHAR(3) NOT NULL,
CONSTRAINT level_pkey PRIMARY KEY(id),
CONSTRAINT UQ_level_unique_name UNIQUE(name),
CONSTRAINT UQ_level_unique_code UNIQUE(code)
);

CREATE TABLE degree(
    id SERIAL,
    code VARCHAR(4) NOT NULL,
    name VARCHAR(75) NOT NULL,
    department_id SMALLINT NOT NULL,
    level_id SMALLINT,
CONSTRAINT degree_pkey PRIMARY KEY(id),
CONSTRAINT FK_degree_department_id FOREIGN KEY(department_id) REFERENCES department(id),
CONSTRAINT FK_degree_level_id FOREIGN KEY(level_id) REFERENCES level(id),
CONSTRAINT UQ_degree_unique_code UNIQUE(code),
CONSTRAINT UQ_degree_unique_name UNIQUE(name)
);

CREATE TABLE "group"(
    id SERIAL,
    name VARCHAR(11) NOT NULL,
    degree_id SMALLINT NOT NULL,
CONSTRAINT group_pkey PRIMARY KEY(id),
CONSTRAINT FK_group_degree_id FOREIGN KEY(degree_id) REFERENCES degree(id),
CONSTRAINT UQ_group_unique_name UNIQUE(name)
);

CREATE TABLE topic(
    id SERIAL,
    name VARCHAR(25) NOT NULL,
CONSTRAINT topic_pkey PRIMARY KEY(id),
CONSTRAINT UQ_topic_unique_name UNIQUE(name)
);

CREATE TABLE type(
    id SERIAL,
    name VARCHAR(25) NOT NULL,
CONSTRAINT question_type_pkey PRIMARY KEY(id),
CONSTRAINT UQ_type_unique_name UNIQUE(name)
);

CREATE TABLE question(
    id SERIAL,
    sort SMALLINT NOT NULL,
    statement TEXT NOT NULL,
    disabled TIMESTAMPTZ,
    type_id SMALLINT NOT NULL,
    level_id SMALLINT NOT NULL,
    topic_id SMALLINT NOT NULL,
    created TIMESTAMPTZ NOT NULL,
CONSTRAINT question_pkey PRIMARY KEY(id),
CONSTRAINT FK_question_level_id FOREIGN KEY(level_id) REFERENCES level(id),
CONSTRAINT FK_question_topic_id FOREIGN KEY(topic_id) REFERENCES topic(id),
CONSTRAINT FK_question_type_id FOREIGN KEY(type_id) REFERENCES type(id)
);

CREATE TABLE student(
    id SERIAL,
    email VARCHAR(75) NOT NULL,
    name VARCHAR(50),
    surname VARCHAR(50),
    group_id SMALLINT NOT NULL,
CONSTRAINT student_pkey PRIMARY KEY(id),
CONSTRAINT FK_student_group_id FOREIGN KEY(group_id) REFERENCES "group"(id),
CONSTRAINT UQ_student_unique_email UNIQUE(email)
);

CREATE TABLE subject(
    id SERIAL,
    code VARCHAR(10) NOT NULL,
    name VARCHAR(75) NOT NULL,
    degree_id SMALLINT NOT NULL,
    topic_id SMALLINT,
CONSTRAINT subject_pkey PRIMARY KEY(id),
CONSTRAINT FK_subject_degree_id FOREIGN KEY(degree_id) REFERENCES degree(id),
CONSTRAINT FK_subject_topic_id FOREIGN KEY(topic_id) REFERENCES topic(id),
CONSTRAINT UQ_subject_unique_code_degree_id UNIQUE(code, degree_id),
CONSTRAINT UQ_subject_unique_name_degree_id UNIQUE(name, degree_id)
);

CREATE TABLE subject_student(
    subject_id SMALLINT,
    student_id INTEGER,
CONSTRAINT subject_student_pkey PRIMARY KEY(subject_id, student_id),
CONSTRAINT FK_subject_student_student_id FOREIGN KEY(student_id) REFERENCES student(id),
CONSTRAINT FK_subject_student_subject_id FOREIGN KEY(subject_id) REFERENCES subject(id)
);

CREATE TABLE trainer(
    id SERIAL,
    name VARCHAR(75) NOT NULL,
CONSTRAINT trainer_pkey PRIMARY KEY(id),
CONSTRAINT UQ_trainer_unique_name UNIQUE(name)
);

CREATE TABLE subject_trainer_group(
    id SERIAL,
    subject_id SMALLINT NOT NULL,
    trainer_id SMALLINT NOT NULL,
    group_id SMALLINT,
CONSTRAINT subject_trainer_group_pkey PRIMARY KEY(id),
CONSTRAINT FK_subject_trainer_group_subject_id FOREIGN KEY(subject_id) REFERENCES subject(id),
CONSTRAINT FK_subject_trainer_group_trainer_id FOREIGN KEY(trainer_id) REFERENCES trainer(id),
CONSTRAINT FK_subject_trainer_group_group_id FOREIGN KEY(group_id) REFERENCES "group"(id),
CONSTRAINT UQ_subject_trainer_group UNIQUE(subject_id, trainer_id, group_id)
);

COMMIT;
