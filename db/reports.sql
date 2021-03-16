-- Create reports schema
DROP SCHEMA IF EXISTS reports CASCADE;

CREATE SCHEMA IF NOT EXISTS reports AUTHORIZATION postgres;

GRANT ALL ON SCHEMA reports TO postgres;

BEGIN WORK;

-- Define views at reports schema
CREATE VIEW reports.answer AS
    SELECT fe."timestamp",
        lv.name AS level,
        de.name AS department,
        dg.name AS degree_name,
        gr.name AS group_name,
        su.code AS subject_code,
        su.name AS subject_name,
        tr.name AS trainer_name,
        tp.name AS question_topic,
        qu.sort AS question_sort,
        qu.statement AS question_statement,
        an.value AS answer_value
    FROM public.forms_evaluation fe
        LEFT JOIN master."group" gr ON gr.id = fe.classgroup_id
        LEFT JOIN master.trainer tr ON tr.id = fe.trainer_id
        LEFT JOIN master.subject su ON su.id = fe.subject_id
        LEFT JOIN public.forms_answer an ON an.evaluation_id = fe.id
        LEFT JOIN master.question qu ON qu.id = an.question_id
        LEFT JOIN master.degree dg ON dg.id = su.degree_id
        LEFT JOIN master.department de ON de.id = dg.department_id
        LEFT JOIN master.level lv ON lv.id = fe.level_id
        LEFT JOIN master.topic tp ON tp.id = qu.topic_id;

COMMIT;
