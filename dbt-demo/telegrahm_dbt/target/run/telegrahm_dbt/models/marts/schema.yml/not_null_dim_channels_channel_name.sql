
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select channel_name
from "dbt"."dbt-demo_marts"."dim_channels"
where channel_name is null



  
  
      
    ) dbt_internal_test