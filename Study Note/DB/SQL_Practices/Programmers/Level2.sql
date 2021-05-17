-- 루시와 엘라 찾기

-- 동물 보호소에 들어온 동물 중 이름이 Lucy, Ella, Pickle, Rogan, Sabrina, Mitty인 동물의 아이디와 이름, 성별 및 중성화 여부를 조회

SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE FROM ANIMAL_INS
WHERE NAME IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
ORDER BY ANIMAL_ID


-- 이름에 el이 들어가는 동물 찾기

-- 이름에 "EL"이 들어가는 개의 아이디와 이름을 조회

-- LIKE 사용

SELECT ANIMAL_ID, NAME FROM ANIMAL_INS
WHERE NAME LIKE '%EL%' AND ANIMAL_TYPE = 'Dog'
ORDER BY NAME


-- 중성화 여부 파악하기

-- 동물의 아이디와 이름, 중성화 여부를 아이디 순으로 조회
-- 중성화가 되어있다면 'O', 아니라면 'X'라고 표시

-- CASE WHEN ... THEN
-- ELSE ...
-- END AS ... 구문

SELECT ANIMAL_ID, NAME,
CASE WHEN (SEX_UPON_INTAKE LIKE '%Neutered%') THEN 'O'
WHEN (SEX_UPON_INTAKE LIKE '%Spayed%') THEN 'O'
ELSE 'X'
END AS '중성화'
FROM ANIMAL_INS
ORDER BY ANIMAL_ID


-- 동명 동물 수 찾기

-- 두 번 이상 쓰인 이름과 해당 이름이 쓰인 횟수를 조회
-- 이름 순으로 조회

-- HAVING 사용

SELECT NAME, COUNT(NAME) AS 'COUNT' FROM ANIMAL_INS 
GROUP BY NAME
HAVING COUNT(NAME) >= 2
ORDER BY NAME


-- 고양이와 개는 몇 마리 있을까

-- 고양이와 개가 각각 몇 마리인지 조회
-- 고양이를 개보다 먼저 조회

SELECT ANIMAL_TYPE, COUNT(*) AS 'count' FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE


-- 최솟값 구하기

-- 가장 먼저 들어온 동물은 언제 들어왔는지 조회

-- 시간은 빠를수록 작은 값으로 취급

SELECT MIN(DATETIME) AS '시간' FROM ANIMAL_INS


-- 동물 수 구하기

-- 동물이 몇 마리 들어왔는지 조회

SELECT COUNT(*) AS 'count' FROM ANIMAL_INS


-- NULL 처리하기

-- 동물의 생물 종, 이름, 성별 및 중성화 여부를 아이디 순으로 조회
-- 이름이 없는 동물의 이름은 "No name"으로 표시

SELECT ANIMAL_TYPE, 
CASE WHEN NAME IS NULL THEN 'No name'
ELSE NAME
END AS 'NAME',
SEX_UPON_INTAKE FROM ANIMAL_INS
ORDER BY ANIMAL_ID


-- 입양 시각 구하기(1)

-- 09:00부터 19:59까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회
-- 시간대 순으로 정렬

SELECT HOUR(DATETIME), COUNT(*) FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) >= 9 AND HOUR(DATETIME) <= 19
GROUP BY HOUR(DATETIME)
ORDER BY HOUR(DATETIME)


-- 중복 제거하기

-- 동물의 이름은 몇 개인지 조회
-- 이름이 NULL인 경우는 집계하지 않으며

-- COUNT(DISTINCT ..)

SELECT COUNT(DISTINCT NAME) AS 'count' FROM ANIMAL_INS
WHERE NAME IS NOT NULL


-- DATETIME에서 DATE로 형 변환

-- 동물의 아이디와 이름, 들어온 날짜(시, 분, 초 제외)를 조회

SELECT ANIMAL_ID, NAME, 
DATE_FORMAT(DATETIME, '%Y-%m-%d') AS '날짜' 
FROM ANIMAL_INS
