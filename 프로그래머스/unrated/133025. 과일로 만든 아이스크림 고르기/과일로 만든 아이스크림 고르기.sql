-- 코드를 입력하세요
select a.flavor
from first_half as a
    left join icecream_info as b
    on a.flavor = b.flavor
where a.total_order > 3000 and b.ingredient_type like 'fruit_based'
order by a.total_order desc;