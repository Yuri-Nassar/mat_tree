# import pandas as pd
#
# df_sample1 = pd.read_csv("/home/gbl/Projects/Academics/mat_tree/dataset/basometro/2022-09-28_6M_specific_test.csv")
# df_sample2 = pd.read_csv("/home/gbl/Projects/Academics/mat_tree/dataset/basometro/2022-09-28_6M_specific_train.csv")
#
# df_concat = pd.concat([df_sample1, df_sample2], ignore_index=True)
# df_concat.to_csv('/home/gbl/Projects/Academics/mat_tree/dataset/basometro/2022-09-28_6M_specific.csv', sep='\t')

# list = ['UF', 'voto', 'orientacaoGoverno', 'anoProposicao', 'anoVotacao', 'tipoProposicao', 'governo', 'parlamentar',
#         'data', 'idVotacao', 'tid', 'label', 'horaVotacao', 'diaDaSemanaVotacao', 'diaDaSemanaVotacaoNome', 'diaDoAno',
#         'diaDoMesVotacao', 'mesVotacao', 'delayVotacaoAnos', 'alinhamento']
# df_master = df_sample1.merge(df_sample2,
#                              on=list,
#                              how='outer')
# df_master.to_csv('/home/gbl/Projects/Academics/mat_tree/dataset/basometro/2022-09-28_6M_specific.csv')
import csv

header = ['', 'UF', 'voto', 'orientacaoGoverno', 'anoProposicao', 'anoVotacao', 'tipoProposicao', 'governo',
          'parlamentar', 'data', 'idVotacao', 'tid', 'label', 'horaVotacao', 'diaDaSemanaVotacao',
          'diaDaSemanaVotacaoNome', 'diaDoAno', 'diaDoMesVotacao', 'mesVotacao', 'delayVotacaoAnos', 'alinhamento']
data = []

with open("/home/gbl/Projects/Academics/mat_tree/dataset/basometro/2022-09-28_6M_specific_test.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    l = next(csv_reader, None)
    for row in csv_reader:
        if row is not header:
            data.append(row)

with open("/home/gbl/Projects/Academics/mat_tree/dataset/basometro/2022-09-28_6M_specific_train.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    l = next(csv_reader, None)
    for row in csv_reader:
        if row is not header:
            data.append(row)
    print(f'Processed {line_count} lines.')

with open('/home/gbl/Projects/Academics/mat_tree/dataset/basometro/2022-09-28_6M_specific.csv', 'w') as f:
    # using csv.writer method from CSV package
    write = csv.writer(f)

    write.writerow(header)
    write.writerows(data)
