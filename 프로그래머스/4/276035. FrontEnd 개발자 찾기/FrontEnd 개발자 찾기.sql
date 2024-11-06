-- 먼저 Front End 스킬에 해당하는 모든 CODE 값을 OR 연산으로 합친 값을 구하는 서브쿼리
WITH FRONTEND_SKILL_CODE AS (
    SELECT 
        BIT_OR(CODE) AS TOTAL_FRONTEND_CODE
    FROM 
        SKILLCODES
    WHERE 
        CATEGORY = 'Front End'
)

-- 합산된 Front End 스킬 코드와 개발자의 SKILL_CODE를 비교
SELECT 
    D.ID, 
    D.EMAIL, 
    D.FIRST_NAME, 
    D.LAST_NAME
FROM 
    DEVELOPERS D
JOIN 
    FRONTEND_SKILL_CODE F ON (D.SKILL_CODE & F.TOTAL_FRONTEND_CODE) != 0
ORDER BY 
    D.ID ASC;
