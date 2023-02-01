from datetime import datetime, timedelta

'''
{
  'id': 'W3gAKiDp8pBctExIQ9g5HcJqGFFQX8VfwrCCLhDlD3ep2WCjH2b96bemG2nc1r6N',
  'ttl': 1209600,
  'created': '2023-01-23T10:09:42.963Z',
  'userId': 50442
}
'''


class MappaLoginResponse:

    def __init__(self, data: dict):
        self.auth: str = data.get('id', '')
        self.user_id: int = data.get('userId', 0)
        self.valid_until: datetime = datetime.strptime(
            data.get('created', '0001-01-01T00:00:00')[0:19], '%Y-%m-%dT%H:%M:%S') +\
            timedelta(seconds=data.get('ttl', 0))

    def __str__(self):
        return f'{self.user_id} [{self.auth}] {self.valid_until}'


class MappaAssociadoResponse:
    def __init__(self, data: dict):
        self.codigo = data.get('codigo', 0)
        self.codigoCategoria = data.get('codigoCategoria', 0)
        self.codigoEquipe = data.get('codigoEquipe', 0)
        self.codigoFoto = data.get('codigoFoto', 0)
        self.codigoRamo = data.get('codigoRamo', 0)
        self.codigoRamoAdulto = data.get('codigoRamoAdulto', 0)
        self.codigoSegundaCategoria = data.get('codigoSegundaCategoria', 0)
        self.codigoTerceiraCategoria = data.get('codigoTerceiraCategoria', 0)
        self.dataAcompanhamento = data.get('dataAcompanhamento', '')
        self.dataNascimento = data.get('dataNascimento', '')
        self.dataValidade = data.get('dataValidade', '')
        self.linhaFormacao = data.get('linhaFormacao', '')
        self.nome = data.get('nome', '')
        self.nomeAbreviado = data.get('nomeAbreviado', '')
        self.numeroDigito = data.get('numeroDigito', 0)
        self.sexo = data.get('sexo', '')
        self.username = data.get('username', 0)


class MappaEscotistaResponse:
    def __init__(self, data: dict):
        self.ativo = data.get('ativo', True)
        self.codigo = data.get('codigo', 0)
        self.codigoAssociado = data.get('codigoAssociado', 0)
        self.codigoFoto = data.get('codigoFoto', 0)
        self.codigoGrupo = data.get('codigoGrupo', 0)
        self.codigoRegiao = data.get('codigoRegiao', '')
        self.nomeCompleto = data.get('nomeCompleto', '')
        self.username = data.get('username', '')


class MappaGrupoResponse:
    def __init__(self, data: dict):
        self.codigo = data.get('codigo', 0)
        self.codigoModalidade = data.get('codigoModalidade', 0)
        self.codigoRegiao = data.get('codigoRegiao', '')
        self.nome = data.get('nome', '')


class MappaDadosEscotista:

    def __init__(self, data: dict):
        self.associado = MappaAssociadoResponse(data.get('associado', {}))
        self.escotista = MappaEscotistaResponse(data.get('escotista', {}))
        self.grupo = MappaGrupoResponse(data.get('grupo', {}))
