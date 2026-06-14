-- Write your query below



SELECT student_id,MIN(exam_id)as exam_id,score FROM exam_results as e1 WHERE
score=(SELECT MAX(e2.score) as ms 
FROM exam_results as e2 WHERE e2.student_id=e1.student_id)
GROUP BY student_id,score  ORDER BY e1.student_id