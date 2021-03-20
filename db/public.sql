BEGIN WORK;

SET TRANSACTION READ WRITE;

-- Define constraints at public schema
ALTER TABLE public.forms_answer
    ADD CONSTRAINT FK_forms_answer_question_id FOREIGN KEY(question_id) REFERENCES master.question(id);

ALTER TABLE public.forms_participation
    ADD CONSTRAINT FK_forms_participation_student_id FOREIGN KEY(student_id) REFERENCES master.student(id);

ALTER TABLE public.forms_evaluation
    ADD CONSTRAINT FK_forms_evaluation_group_name FOREIGN KEY(group_id) REFERENCES master."group"(id),
    ADD CONSTRAINT FK_forms_evaluation_trainer_id FOREIGN KEY(trainer_id) REFERENCES master.trainer(id),
    ADD CONSTRAINT FK_forms_evaluation_subject_id FOREIGN KEY(subject_id) REFERENCES master.subject(id);

-- Define views at public schema
CREATE VIEW public.forms_student AS
    SELECT st.id,
           st.email,
           st.name,
           st.surname,
           lv.id AS level_id,
           lv.code AS level_code,
           lv.name AS level_name,
           gr.id AS group_id,
           gr.name AS group_name,
           dg.id AS degree_id,
           dg.code AS degree_code,
           subjects.subjects
   FROM master.student st
      LEFT JOIN master."group" gr ON gr.id = st.group_id
      LEFT JOIN master.degree dg ON dg.id = gr.degree_id
      LEFT JOIN master.level lv ON lv.id = dg.level_id
      LEFT JOIN (
                  SELECT ss.student_id,
                         string_agg(su.code::text, ','::text) AS subjects
                  FROM master.subject_student ss
                      LEFT JOIN master.subject su ON ss.subject_id = su.id
                  GROUP BY ss.student_id) subjects ON subjects.student_id = st.id;

CREATE VIEW public.forms_subject AS
    SELECT sb.id,
           sb.code,
           CASE
               WHEN tr.name IS NULL THEN sb.name::text
               ELSE concat(sb.name, ' (', tr.name, ')')
           END AS name,
           dg.id AS degree_id,
           dg.code AS degree_code,
           dg.name AS degree_name,
           tr.id AS trainer_id,
           st.group_id
    FROM master.subject sb
        LEFT JOIN master.degree dg ON dg.id = sb.degree_id
        LEFT JOIN master.subject_trainer_group st ON st.subject_id = sb.id
        LEFT JOIN master.trainer tr ON tr.id = st.trainer_id;

COMMIT;
