select t1.*,
        coalesce(t2.total_declarado,0) as total_declarado,
        coalesce(t2.qtde_itens_declarados,0) as qtde_itens_declarados

from tb_candidatura as t1 -- 1

left join (
    select numero_sequencial,
           sum( valor ) as total_declarado,
           count(1) as qtde_itens_declarados
    from tb_declaracao_2018 
    group by numero_sequencial
) as t2
on t1.numero_sequencial = t2.numero_sequencial

where numero_turno = 1
and descricao_situacao_candidatura = 'APTO'
and descricao_cargo like '%{cargo}%'