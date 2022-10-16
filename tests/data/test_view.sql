create view test_view as
select * 
from some_table st
join vw_some_view sv on
    sv.id = st.id
join vw_some_other_view ov on
    ov.id = st.id