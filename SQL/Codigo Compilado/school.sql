create database school;
use school;

-- Degree table
create table degree (
	degree_code int,
    degree_name varchar(50),
    degree_duration float,
    constraint pk_dc primary key(degree_code)
);

-- Subject table
create table subject (
    subject_code int,
    subject_name varchar(50),
    subject_credits float,
    constraint pk_sc primary key(subject_code)
);

-- Teacher table
create table teacher (
    teacher_code int,
    teacher_name varchar(150),
    teacher_dir varchar(200),
    teacher_phone bigint,
    teacher_schedule date,
    constraint pk_tc primary key(teacher_code)
);

/*
 * Student table
 * with a foreign key
 */

 create table student(
    student_code int,
    student_name varchar(50),
    student_age int,
    student_semester int,
    student_gender varchar(10),
    degree_key int,
    constraint pk_sc primary key(student_code),
    constraint fk_dk primary key(degree_key) REFERENCES degree(degree_code)
 );