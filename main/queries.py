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
    x.ODDIY_XARIDOR IS NOT TRUE
ORDER BY 
    x.id;
"""

variable = """select ball_limit,ball from uzgaruvchi"""

seller_deal = """SELECT s.SHRAQAM,s.SANA,x.FIO,x.LFIO ,x.PNFL ,sum(c.MIQDOR*c.NARX),sum(c.JAMI),s.MUDDAT,x.id,s.savdochi_id FROM SHARTNOMA s
LEFT JOIN XARIDOR x ON x.id=s.XARIDOR_ID 
LEFT JOIN CHIQIM c ON c.SHARTNOMA_ID =s.ID 
WHERE s.SAVDOCHI_ID = ? AND s.SANA BETWEEN ? AND ?
GROUP BY s.SANA,s.SHRAQAM,x.FIO,s.MUDDAT,x.LFIO ,x.PNFL,x.id,s.savdochi_id 
ORDER BY s.SANA,s.SHRAQAM,x.FIO,s.MUDDAT,x.LFIO ,x.PNFL,x.id,s.savdochi_id
"""

sellers = """SELECT f.id,f.FIO FROM FOYDALANUVCHI f 
LEFT JOIN LAVOZIM l2 ON l2.id=f.LAVOZIM_ID 
WHERE LOWER(l2.nomi) LIKE '%sotuvchi%'
ORDER BY FIO 
"""

void_contracts = """SELECT 
    s.SHRAQAM,
    s.SANA,
    x.FIO,x.LFIO ,x.PNFL, 
    SUM(c.MIQDOR * c.NARX) AS TOTAL_AMOUNT,
    SUM(c.JAMI) AS TOTAL_SNARX,
    s.MUDDAT
FROM 
    SHARTNOMA s
LEFT JOIN 
    CHIQIM c ON c.SHARTNOMA_ID = s.ID
LEFT JOIN 
    TULOV t ON t.SHARTNOMA_ID = s.ID
LEFT JOIN 
    XARIDOR x ON x.ID = s.XARIDOR_ID
LEFT JOIN 
    TURTULOV t2 ON t2.ID = t.BOSHQA_ID
WHERE 
    t2.OTMENA IS TRUE 
    AND s.SAVDOCHI_ID = ? AND t.YVAQT BETWEEN ? AND ?
GROUP BY 
    s.SANA, x.FIO, s.SHRAQAM, s.MUDDAT,x.LFIO ,x.PNFL 
ORDER BY 
    s.SANA, x.FIO, s.SHRAQAM, s.MUDDAT,x.LFIO ,x.PNFL ;
"""

seller_info = """SELECT s.SHRAQAM,s.sana,s.SUMMA,s.MUDDAT,sum(g.QOLDIQ) AS qarz FROM XARIDOR x 
LEFT JOIN SHARTNOMA s ON s.XARIDOR_ID = x.ID 
LEFT JOIN GRAFIK g ON g.SHARTNOMA_ID = s.ID 
WHERE x.id= ? AND g.SANA <= ?
GROUP BY s.SANA ,s.SHRAQAM ,s.SUMMA,s.MUDDAT
ORDER BY s.SANA ,s.SHRAQAM ,s.SUMMA,s.MUDDAT
"""

seller = """WITH savdo_data AS (
    SELECT 
        s.SAVDOCHI_ID, 
        SUM(c.MIQDOR * c.NARX) AS total_savdo
    FROM SHARTNOMA s
    LEFT JOIN CHIQIM c ON c.SHARTNOMA_ID = s.ID
    WHERE s.SANA BETWEEN ? AND ?
    GROUP BY s.SAVDOCHI_ID
),
otem_data AS (
    SELECT 
        s.SAVDOCHI_ID, 
        SUM(c.MIQDOR * c.NARX) AS total_otem
    FROM SHARTNOMA s
    LEFT JOIN CHIQIM c ON c.SHARTNOMA_ID = s.ID
    LEFT JOIN TULOV t ON t.SHARTNOMA_ID = s.ID
    LEFT JOIN TURTULOV t2 ON t2.ID = t.BOSHQA_ID
    WHERE t.YVAQT BETWEEN ? AND ?
      AND t2.OTMENA IS TRUE
    GROUP BY s.SAVDOCHI_ID
),
plan_data AS (
  SELECT l2.LAVOZIM_ID AS lavozim_id ,l2."LIMIT"  from LLIMIT l2 
  WHERE l2.SANA BETWEEN ? AND ?
)
SELECT 
    f.FIO,
    l.NOMI AS lavozim_nomi,
    COALESCE(pd.limit,0) AS shaxsiy_reja,
    COALESCE(sd.total_savdo, 0) AS savdo,
    COALESCE(od.total_otem, 0) AS otem
FROM FOYDALANUVCHI f
LEFT JOIN lavozim l ON l.id=f.LAVOZIM_ID 
LEFT JOIN savdo_data sd ON sd.SAVDOCHI_ID = f.id
LEFT JOIN otem_data od ON od.SAVDOCHI_ID = f.id
LEFT JOIN plan_data pd ON pd.LAVOZIM_ID=l.id
WHERE f.id = ?;"""

