-- 코드를 입력하세요
SELECT o.animal_id, o.name
from animal_ins i left join animal_outs o using(animal_id)
where o.datetime < i.datetime
order by i.datetime