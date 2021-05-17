-- 모든 레코드 조회하기

-- 모든 동물의 정보를 ANIMAL_ID순으로 조회

SELECT ANIMAL_ID, ANIMAL_TYPE, DATETIME, INTAKE_CONDITION, NAME, SEX_UPON_INTAKE FROM ANIMAL_INS
ORDER BY ANIMAL_ID

SELECT * FROM ANIMAL_INS
ORDER BY ANIMAL_ID


-- 이름이 없는 동물의 아이디

-- 이름이 없는 채로 들어온 동물의 ID를 조회

SELECT ANIMAL_ID FROM ANIMAL_INS
WHERE NAME IS NULL


-- 최댓값 구하기

-- 가장 최근에 들어온 동물은 언제 들어왔는지 조회

SELECT MAX(DATETIME) FROM ANIMAL_INS


-- 이름이 있는 동물의 아이디

-- 이름이 있는 동물의 ID를 조회

SELECT ANIMAL_ID FROM ANIMAL_INS
WHERE NAME IS NOT NULL
ORDER BY ANIMAL_ID


-- 역순 정렬하기

-- 이름과 보호 시작일을 조회
-- ANIMAL_ID 역순

SELECT NAME, DATETIME FROM ANIMAL_INS
ORDER BY ANIMAL_ID DESC


-- 아픈 동물 찾기

-- 아픈 동물의 아이디와 이름을 조회
-- 아이디 순

SELECT ANIMAL_ID, NAME FROM ANIMAL_INS
WHERE INTAKE_CONDITION = 'Sick'


-- 어린 동물 찾기

-- 젊은 동물의 아이디와 이름을 조회
-- 아이디 순으로 조회

SELECT ANIMAL_ID, NAME FROM ANIMAL_INS
WHERE NOT INTAKE_CONDITION = 'Aged'

SELECT ANIMAL_ID, NAME FROM ANIMAL_INS
WHERE INTAKE_CONDITION != 'Aged'


-- 동물의 아이디와 이름

-- 모든 동물의 아이디와 이름을 ANIMAL_ID순으로 조회

SELECT ANIMAL_ID, NAME FROM ANIMAL_INS
ORDER BY ANIMAL_ID


-- 여러 기준으로 정렬하기

-- 아이디와 이름, 보호 시작일을 이름 순으로 조회
-- 이름이 같은 동물 중에서는 보호를 나중에 시작한 동물을 먼저

SELECT ANIMAL_ID, NAME, DATETIME FROM ANIMAL_INS
ORDER BY NAME, DATETIME DESC


-- 상위 n개 레코드

-- 가장 먼저 들어온 동물의 이름을 조회

SELECT NAME FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 1