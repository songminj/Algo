SELECT COUNT(*) AS COUNT
FROM ECOLI_DATA
WHERE (GENOTYPE & 2) = 0              -- 2번 형질(값=2) 없음
  AND (GENOTYPE & 5) <> 0;            -- 1번(1) 또는 3번(4) 보유 → 1|4 = 5
