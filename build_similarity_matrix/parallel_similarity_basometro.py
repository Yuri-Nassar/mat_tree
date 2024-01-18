import pandas as pd
import numpy as np
import trajminer as tm
from trajminer.similarity import MSM, MUITAS
from trajminer.utils.distance import discrete, euclidean

dtypes = {'UF':'string', 'voto':'category', 'orientacaoGoverno':'category', 'anoProposicao':'int32',
          'anoVotacao':'int32', 'tipoProposicao':'category', 'governo':'category', 'parlamentar':'string',
        #   'data':'datetime64[ns]',
           'idVotacao':'string', 'tid':'int64', 'label':'category', 'horaVotacao':'int32', 'diaDaSemanaVotacao':'int32', 'diaDaSemanaVotacaoNome':'category', 'diaDoAno':'int32', 'diaDoMesVotacao':'int32', 'mesVotacao': 'int32', 'delayVotacaoAnos':'int32', 'alinhamento':'category'}
dataset_path = "datasets/basometro/basometro.csv"
basometro_df = pd.read_csv(dataset_path, encoding='latin-1', dtype=dtypes, parse_dates=['data'])

aspects = ['UF','governo','orientacaoGoverno','tipoProposicao','label','diaDaSemanaVotacaoNome','alinhamento',
           'diaDoAno','mesVotacao','anoVotacao','delayVotacaoAnos']
unique_tids = basometro_df.tid.sort_values().unique().tolist()
num_tids = len(unique_tids)

### msm setup
dist_funcs = [discrete, discrete, discrete, discrete, discrete, discrete, discrete,
              euclidean, euclidean, euclidean, euclidean]
thres = [.5, .5, .5, .5, .5, .5, .5, .5, .5, .5, .5]
weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

def process_msm(idx):
    i = idx[0]
    j = idx[1]
    t1 = basometro_df[basometro_df.tid == unique_tids[i]][aspects].values
    t2 = basometro_df[basometro_df.tid == unique_tids[j]][aspects].values
    msm = MSM(dist_funcs, thres, weights)
    return [unique_tids[i],unique_tids[j],msm.similarity(t1,t2)]
