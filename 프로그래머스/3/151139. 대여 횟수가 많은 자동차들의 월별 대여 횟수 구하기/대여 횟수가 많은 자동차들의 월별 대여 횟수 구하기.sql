WITH filtered AS (
  SELECT CAR_ID, START_DATE
  FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
  WHERE START_DATE >= '2022-08-01'
    AND START_DATE <  '2022-11-01'   -- 8~10월(10월31일 포함)만 포함하는 반개구간
),
qualified AS (
  SELECT CAR_ID
  FROM filtered
  GROUP BY CAR_ID
  HAVING COUNT(*) >= 5               -- 기간 내 총 대여 5회 이상인 차량만
)
SELECT
  MONTH(f.START_DATE) AS MONTH,
  f.CAR_ID,
  COUNT(*) AS RECORDS
FROM filtered f
JOIN qualified q USING (CAR_ID)
GROUP BY MONTH(f.START_DATE), f.CAR_ID
ORDER BY MONTH ASC, CAR_ID DESC;      -- 월 오름차순, 같은 월은 CAR_ID 내림차순