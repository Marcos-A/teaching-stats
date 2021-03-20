-- Create reports schema
DROP SCHEMA IF EXISTS reports CASCADE;

CREATE SCHEMA IF NOT EXISTS reports AUTHORIZATION postgres;

GRANT ALL ON SCHEMA reports TO postgres;

BEGIN WORK;

-- Define views at reports schema
CREATE VIEW reports.answer AS
    SELECT ev."timestamp",
        lv.name AS level,
        de.name AS department_name,
        dg.name AS degree_name,
        gr.name AS group_name,
        su.code AS subject_code,
        su.name AS subject_name,
        tr.name AS trainer_name,
        tp.name AS question_topic,
        qu.sort AS question_sort,
        qu.statement AS question_statement,
        an.value AS answer_value
    FROM public.forms_evaluation ev
        LEFT JOIN master."group" gr ON gr.id = ev.group_id
        LEFT JOIN master.trainer tr ON tr.id = ev.trainer_id
        LEFT JOIN master.subject su ON su.id = ev.subject_id
        LEFT JOIN public.forms_answer an ON an.evaluation_id = ev.id
        LEFT JOIN master.question qu ON qu.id = an.question_id
        LEFT JOIN master.degree dg ON dg.id = su.degree_id
        LEFT JOIN master.department de ON de.id = dg.department_id
        LEFT JOIN master.level lv ON lv.id = dg.level_id
        LEFT JOIN master.topic tp ON tp.id = qu.topic_id;

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
