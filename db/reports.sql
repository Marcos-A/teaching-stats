-- Create reports schema
CREATE SCHEMA IF NOT EXISTS reports;

SET search_path TO reports;

BEGIN WORK;

-- Create tables at reports schema
CREATE TABLE reports.staff(
    id SERIAL,
    email VARCHAR(75) NOT NULL,
    name VARCHAR(50),
    surname VARCHAR(50),
    position VARCHAR(50),
CONSTRAINT staff_pkey PRIMARY KEY(id),
CONSTRAINT UQ_staff_unique_email UNIQUE(email)
);

-- Define views at reports schema
CREATE VIEW reports.answer AS
    SELECT ev.id AS evaluation_id,
        ev."timestamp" AS timestamp,
        EXTRACT(YEAR FROM ev."timestamp") AS year,
        lv.code AS level,
        de.name AS department,
        dg.code AS degree,
        gr.name AS group,
        su.code AS subject_code,
        su.name AS subject_name,
        tr.name AS trainer,
        tp.name AS topic,
        qu.sort AS question_sort,
        ty.name AS question_type,
        qu.statement AS question_statement,
        an.value AS value
    FROM public.forms_evaluation ev
        LEFT JOIN master."group" gr ON gr.id = ev.group_id
        LEFT JOIN master.trainer tr ON tr.id = ev.trainer_id
        LEFT JOIN master.subject su ON su.id = ev.subject_id
        LEFT JOIN public.forms_answer an ON an.evaluation_id = ev.id
        LEFT JOIN master.question qu ON qu.id = an.question_id
        LEFT JOIN master.degree dg ON dg.id = su.degree_id
        LEFT JOIN master.department de ON de.id = dg.department_id
        LEFT JOIN master.level lv ON lv.id = dg.level_id
        LEFT JOIN master.topic tp ON tp.id = qu.topic_id
        LEFT JOIN master.type ty ON ty.id = qu.type_id;

CREATE VIEW reports.answer_cf_mp AS
    SELECT * FROM reports.answer
    WHERE level = 'CF'
    AND topic = 'Assignatura';

CREATE VIEW reports.answer_dept_adm AS
    SELECT *
    FROM reports.answer
    WHERE department = 'Administració i gestió';

CREATE VIEW reports.answer_dept_adm_mp AS
    SELECT *
    FROM reports.answer
    WHERE department = 'Administració i gestió'
    AND topic = 'Assignatura';

CREATE VIEW reports.answer_dept_inf AS
    SELECT *
    FROM reports.answer
    WHERE department = 'Informàtica i comunicacions';

CREATE VIEW reports.answer_dept_inf_mp AS
    SELECT *
    FROM reports.answer
    WHERE department = 'Informàtica i comunicacions'
    AND topic = 'Assignatura';

CREATE VIEW reports.participation AS
    SELECT pa."timestamp",
        st.email AS email,
        st.surname AS surname,
        st."name" AS "name",
        gr.name AS group_name,
        dg.name AS degree_name,
        lv.name AS level_name,
        de.name AS department_name
    FROM public.forms_participation pa
        LEFT JOIN master.student st ON st.id = pa.student_id
        LEFT JOIN master."group" gr ON gr.id = st.group_id
        LEFT JOIN master.degree dg ON dg.id = gr.degree_id
        LEFT JOIN master.level lv ON lv.id = dg.level_id
        LEFT JOIN master.department de ON de.id = dg.department_id;

COMMIT;
