-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "Patient" (
    "id" int   NOT NULL,
    "gender" varchar   NOT NULL,
    "age" int   NOT NULL,
    "hypertension" int   NOT NULL,
    "heart_disease" int   NOT NULL,
    "ever_married" varchar   NOT NULL,
    "work_type" varchar   NOT NULL,
    "Residence_type" varchar   NOT NULL,
    "avg_glucose_level" float   NOT NULL,
    "bmi" float   NOT NULL,
    "smoking_status" varchar   NOT NULL,
    "stroke" int   NOT NULL,
    CONSTRAINT "pk_Patient" PRIMARY KEY (
        "id"
     )
);

