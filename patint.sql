-- DROP TABLE IF EXISTS public.patient;
CREATE TABLE IF NOT EXISTS public.patient (
    id SERIAL PRIMARY KEY,
    gender CHAR(1),
    age INTEGER,
    hypertension BOOLEAN,
    heart_disease BOOLEAN,
    ever_married BOOLEAN,
    work_type VARCHAR(50),
    Residence_type VARCHAR(50),
    avg_glucose_level FLOAT,
    bmi FLOAT,
    smoking_status VARCHAR(50),
    stroke BOOLEAN
);

SELECT * FROM patient;





