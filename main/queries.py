customers = """
WITH joriy_shartnoma_cte AS (
    SELECT 
        s.xaridor_id,
        SUM(c.miqdor * c.narx) AS joriy_shartnoma
    FROM 
        SHARTNOMA s
    LEFT JOIN 
        CHIQIM c ON c.shartnoma_id = s.id
    WHERE 
        s.sana BETWEEN ? AND ?
    GROUP BY 
        s.xaridor_id
),
excluded_shartnoma_cte AS (
    SELECT DISTINCT
        t.shartnoma_id
    FROM 
        TULOV t
    LEFT JOIN 
        TURTULOV t2 ON t2.id = t.boshqa_id
    WHERE 
        t2.otmena IS TRUE
),
total_grafik_ball_cte AS (
    SELECT 
        s.xaridor_id,
        SUM(g.ball) / COUNT(DISTINCT s.id) AS jami
    FROM 
        SHARTNOMA s
    LEFT JOIN 
        GRAFIK g ON g.shartnoma_id = s.id
    WHERE 
        s.id NOT IN (SELECT shartnoma_id FROM excluded_shartnoma_cte)
    GROUP BY 
        s.xaridor_id
),
total_shartnoma_cte AS (
    SELECT 
        s.xaridor_id,
        SUM(c.miqdor * c.snarx) AS total_sum,
        COUNT(DISTINCT s.id) AS shartnoma_count
    FROM 
        SHARTNOMA s
    LEFT JOIN 
        CHIQIM c ON c.shartnoma_id = s.id
    WHERE 
        s.id NOT IN (SELECT shartnoma_id FROM excluded_shartnoma_cte)
    GROUP BY 
        s.xaridor_id
)
SELECT 
    x.id,
    x.fio,
    x.PNFL,
    x.pasport,
    x.tsana,
    x.tel1,
    x.tel2,
    CASE 
        WHEN COALESCE(j.joriy_shartnoma, 0) > 0 THEN ' '
        ELSE NULL 
    END AS savdochi,
    COALESCE(j.joriy_shartnoma, 0) AS joriy_oy_shartnoma,
    CASE 
        WHEN COALESCE(t.total_sum, 0) > 0 THEN 
            ((COALESCE(t.total_sum, 0)* ? )/ (COALESCE(t.shartnoma_count, 1)* ? )) +
            COALESCE(g.jami, 0) * ? * 0.4
        ELSE 0
    END AS oy_boshi_limit,
    f.fio AS masul,
    x.ENTRY_DATE AS kelish_sanasi
FROM 
    XARIDOR x
LEFT JOIN 
    joriy_shartnoma_cte j ON j.xaridor_id = x.id
LEFT JOIN 
    total_shartnoma_cte t ON t.xaridor_id = x.id
LEFT JOIN 
    total_grafik_ball_cte g ON g.xaridor_id = x.id
LEFT JOIN 
    FOYDALANUVCHI f ON f.id = x.FOYDALANUVCHI_ID
WHERE 
    x.ODDIY_XARIDOR IS NOT TRUE and x.id < 100
ORDER BY 
    x.id;
"""

variable = """select ball_limit,ball from uzgaruvchi"""
