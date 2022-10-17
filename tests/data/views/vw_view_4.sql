create view vw_view_4 as
select * 
from some_table st
join vw_view_1 sv on
    sv.id = st.id
join vw_view_2 sv2 on
    sv2.id = st.id