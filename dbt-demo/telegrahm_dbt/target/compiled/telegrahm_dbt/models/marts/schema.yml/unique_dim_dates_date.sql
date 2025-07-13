
    
    

select
    date as unique_field,
    count(*) as n_records

from "dbt"."dbt-demo_marts"."dim_dates"
where date is not null
group by date
having count(*) > 1


