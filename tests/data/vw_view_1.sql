create view vw_view_1 as
select * 
from some_table st
join vw_view_3 sv on
    sv.id = st.id