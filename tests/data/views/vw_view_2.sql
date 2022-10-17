create view vw_view_2 as
select * 
from some_table st
join vw_view_3 sv on
    sv.id = st.id