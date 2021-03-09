-- Create reports schema
DROP SCHEMA IF EXISTS reports CASCADE;

CREATE SCHEMA IF NOT EXISTS reports AUTHORIZATION postgres;

GRANT ALL ON SCHEMA reports TO postgres;

BEGIN WORK;

-- Define views at reports schema
CREATE VIEW reports.answer AS
    SELECT de.name AS department,
           lv.name AS level,
           dg.code AS degree_code,
           dg.name AS degree_name,
           su.code AS subject_code,
           su.name AS subject_name,
           fe."timestamp",
           tp.name AS question_topic,
           qu.statement AS question_statement,
           an.value AS answer_value
    FROM forms_evaluation fe
    LEFT JOIN master.trainer tr ON tr.id = fe.trainer_id
    LEFT JOIN master.subject su ON su.id = fe.subject_id
    LEFT JOIN forms_answer an ON an.id = fe.id
    LEFT JOIN master.question qu ON qu.id = an.question_id
    LEFT JOIN master.degree dg ON dg.id = su.degree_id
    LEFT JOIN master.department de ON de.id = dg.department_id
    LEFT JOIN master.level lv ON lv.id = fe.level_id
    LEFT JOIN master.topic tp ON tp.id = qu.topic_id;

COMMIT;
