select distinct answer_date,round(COUNT(issue_id)/count(DISTINCT author_id),2)
from answer_tb a
where month(answer_date)=11
group by answer_date
order by answer_date


select
    (case when author_level>=5 and author_level <=6 then '5-6级'
   when author_level>=3 and author_level <=4 then '3-4级'
    when author_level>=1 and author_level <=2 then '1-2级'
    end) as level_cut,
    count( a.author_id)as num
from author_tb a
inner join answer_tb b
on a.author_id=b.author_id
where char_len>100
group by level_cut
order by num desc



如果是连续的日期，那么日期-日期对应的行数，所求出的日期是一样的值，基于这个可以找出
select t2.author_id,author_level,t2.day_cnt
from 
    (select author_id,count(*) day_cnt
    from 
        (select answer_date,author_id,
                dense_rank()over(partition by author_id order by answer_date) as cnt
        from answer_tb
        group by answer_date,author_id
        ) t1
    group by author_id,date_sub(answer_date,interval cnt day)
    having count(*)>=3
    ) t2
join author_tb
on t2.author_id=author_tb.author_id
order by t2.author_id;
