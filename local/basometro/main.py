from local.basometro.TreeNode import TreeNode

columns = ["UF", "voto", "orientacaoGoverno", "anoProposicao", "anoVotacao", "tipoProposicao", "governo", "parlamentar",
           "data", "idVotacao", "tid", "label", "horaVotacao", "diaDaSemanaVotacao", "diaDaSemanaVotacaoNome",
           "diaDoAno", "diaDoMesVotacao", "mesVotacao", "delayVotacaoAnos", "alinhamento"]
TreeNode.dashboard(TreeNode.df_dict)
