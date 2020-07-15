select *
from tb_candidatura

where descricao_situacao_candidatura = '{status_candidatura}'
and descricao_cargo not like '%{cargo}%'