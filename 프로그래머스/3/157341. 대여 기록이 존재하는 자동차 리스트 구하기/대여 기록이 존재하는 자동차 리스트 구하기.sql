-- 코드를 입력하세요
SELECT C.CAR_ID FROM CAR_RENTAL_COMPANY_CAR C, CAR_RENTAL_COMPANY_RENTAL_HISTORY H
WHERE C.CAR_ID = H.CAR_ID AND C.CAR_TYPE='세단' AND MONTH(H.START_DATE) = 10
GROUP BY C.CAR_ID
ORDER BY C.CAR_ID DESC