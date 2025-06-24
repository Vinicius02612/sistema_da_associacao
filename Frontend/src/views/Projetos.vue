<template>
	<v-container class="ma-0 fill-height align-start" max-width="100%">
		<v-row class="mt-0 ml-0 mr-0" :gutter="1">
			<v-col cols="12">
				<div class="d-flex justify-space-between align-center mt-2">
					<div class ="d-flex" style="width: 30%">
						<v-text-field
						class=" mr-5 bg-grey-lighten-4"
						append-inner-icon="mdi-magnify"
						label="Busca por Título ou CNPJ"
						v-model="filters.search"
						max-width="70%"
						variant="outlined"
						density="compact"
						hide-details
						/>
						<v-btn append-icon="mdi-plus" color="primary" to="/projetos/adicionar" variant="elevated">
							Novo projeto
						</v-btn>
					</div>
					<div class="d-flex align-center">
						<span>Filtros: </span>
						<v-btn
							class="ma-1 d-flex align-center"
							color="primary"
							variant="outlined"
							@click="filters.selected = 'andamento', filterProjetos()"
						>
							<v-tooltip
								activator="parent"
								location="bottom"
							>
								Em andamento
							</v-tooltip>
							<v-icon>mdi-play-speed</v-icon>
						</v-btn>
						<v-btn
							class="ma-1 d-flex align-center"
							color="gray"
							variant="outlined"
							@click="filters.selected = 'complete', filterProjetos()"
						>
							<v-tooltip
								activator="parent"
								location="bottom"
							>
								Completos
							</v-tooltip>
							<v-icon>mdi-checkbox-marked-circle-outline</v-icon>
						</v-btn>
						<v-btn
							class="ma-1 d-flex align-center"
							variant="outlined"
							color="red"
							@click="filters.selected = 'canceled', filterProjetos()"
						>
							<v-tooltip
								activator="parent"
								location="bottom"
							>
								Cancelados
							</v-tooltip>
							<v-icon>mdi-close</v-icon>
						</v-btn>
						<v-btn
							class="ma-1 d-flex align-center border-lg border-opacity-75"
							variant="outlined"
							@click="filters.selected = 'all', filterProjetos()"
						>
							<v-tooltip
								activator="parent"
								location="bottom"
							>
								Todos
							</v-tooltip>
							<v-icon>mdi-list-box-outline</v-icon>
						</v-btn>
					</div>
				</div>
			</v-col>

			<v-col cols="12">
				<v-table>
							<thead>
								<tr>
									<th>Titulo</th>
									<th>CNPJ</th>
									<th>Instituição/Empresa</th>
									<th>Data de Inicio</th>
									<th>Data de Término</th>
									<th>Status</th>
									<th>Ações</th>
								</tr>
							</thead>
							<tbody>
								<tr
								v-for="(item, index) in projetosFiltered"
								:key="item.id"
								:style="{ backgroundColor: index % 2 === 0 ? 'white' : '#f8f8f8' }"
								>
								<td>{{ item.Titulo }}</td>
								<td>{{ item.CNPJ }}</td>
								<td>{{ item.InstituicaoEmpresa }}</td>
								<td><DateLabel :date="new Date(item.dataInicio)" /> </td>
								<td><DateLabel :date="new Date(item.dataFim)" /> </td>
								<td>
									<v-chip
									:color="item.status === 'Finalizado' ? 'gray' : item.status === 'Cancelado' ? 'red' : 'green'"
									class="chip-size d-flex justify-center"
									variant="outlined"
									>
									{{ item.status }}
								</v-chip>
							</td>
							<td>
								<v-btn-group
									variant="outlined"
									divided
									rounded="lg"
									class="custom-btn-group d-flex align-center"
								>
									<v-btn
										width="32"
										height="32"
									>
										<v-tooltip
											activator="parent"
											location="bottom"
										>
											Editar
										</v-tooltip>
										<v-icon size="x-large">mdi-pencil</v-icon>
									</v-btn>
									<v-btn
										width="32"
										height="32"
									>
										<v-tooltip
											activator="parent"
											location="bottom"
										>
											Apagar
										</v-tooltip>
										<v-icon size="x-large">mdi-trash-can-outline</v-icon>
									</v-btn>
								</v-btn-group>
						</td>
					</tr>
				</tbody>
			</v-table>
			</v-col>
			
		</v-row>
	</v-container>	
</template>

<script>
import DateLabel from '@/components/ui/DateLabel.vue';

export default {
	name: 'projetos',
	components: {
		DateLabel,
	},
	data() {
		return {
			message: 'Hello, Vue!',
			projetos: [
									{
										id: 1,
										Titulo: "Projeto Alfabetização Digital",
										CNPJ: "10.123.456/0001-01",
										InstituicaoEmpresa: "Fundação Saber",
										dataInicio: "2023-02-01",
										dataFim: "2023-12-01",
										status: "Finalizado"
									},
									{
										id: 2,
										Titulo: "Oficina de Arte Urbana",
										CNPJ: "11.234.567/0001-02",
										InstituicaoEmpresa: "Cultura Jovem",
										dataInicio: "2024-04-15",
										dataFim: "2024-09-15",
										status: "Em Andamento"
									},
									{
										id: 3,
										Titulo: "Capacitação Profissional",
										CNPJ: "12.345.678/0001-03",
										InstituicaoEmpresa: "Senai",
										dataInicio: "2022-08-01",
										dataFim: "2023-07-01",
										status: "Finalizado"
									},
									{
										id: 4,
										Titulo: "Projeto Saúde em Ação",
										CNPJ: "13.456.789/0001-04",
										InstituicaoEmpresa: "Secretaria de Saúde",
										dataInicio: "2024-01-01",
										dataFim: "2024-12-31",
										status: "Em Andamento"
									},
									{
										id: 5,
										Titulo: "Inclusão Digital para Idosos",
										CNPJ: "14.567.890/0001-05",
										InstituicaoEmpresa: "Associação Conectar",
										dataInicio: "2023-05-10",
										dataFim: "2023-11-10",
										status: "Finalizado"
									},
									{
										id: 6,
										Titulo: "Projeto Recicla Mais",
										CNPJ: "15.678.901/0001-06",
										InstituicaoEmpresa: "Eco Vida",
										dataInicio: "2024-02-20",
										dataFim: "2024-08-20",
										status: "Em Andamento"
									},
									{
										id: 7,
										Titulo: "Feira de Livros",
										CNPJ: "16.789.012/0001-07",
										InstituicaoEmpresa: "Editora Saber",
										dataInicio: "2023-09-01",
										dataFim: "2023-09-07",
										status: "Finalizado"
									},
									{
										id: 8,
										Titulo: "Semana da Juventude",
										CNPJ: "17.890.123/0001-08",
										InstituicaoEmpresa: "Prefeitura Jovem",
										dataInicio: "2023-06-10",
										dataFim: "2023-06-17",
										status: "Cancelado"
									},
									{
										id: 9,
										Titulo: "Mutirão de Limpeza",
										CNPJ: "18.901.234/0001-09",
										InstituicaoEmpresa: "Amigos do Bairro",
										dataInicio: "2024-03-05",
										dataFim: "2024-03-20",
										status: "Em Andamento"
									},
									{
										id: 10,
										Titulo: "Oficina de Robótica",
										CNPJ: "19.012.345/0001-10",
										InstituicaoEmpresa: "Tech Júnior",
										dataInicio: "2022-10-01",
										dataFim: "2023-03-01",
										status: "Finalizado"
									},
									{
										id: 11,
										Titulo: "Esporte para Todos",
										CNPJ: "20.123.456/0001-11",
										InstituicaoEmpresa: "ONG Movimento",
										dataInicio: "2024-05-01",
										dataFim: "2024-12-01",
										status: "Em Andamento"
									},
									{
										id: 12,
										Titulo: "Projeto Música na Praça",
										CNPJ: "21.234.567/0001-12",
										InstituicaoEmpresa: "Fundação Cultura",
										dataInicio: "2023-04-01",
										dataFim: "2023-10-01",
										status: "Finalizado"
									},
									{
										id: 13,
										Titulo: "Plante uma Árvore",
										CNPJ: "22.345.678/0001-13",
										InstituicaoEmpresa: "Verde Esperança",
										dataInicio: "2024-06-01",
										dataFim: "2024-07-15",
										status: "Em Andamento"
									},
									{
										id: 14,
										Titulo: "Semana da Leitura",
										CNPJ: "23.456.789/0001-14",
										InstituicaoEmpresa: "Biblioteca Central",
										dataInicio: "2023-08-01",
										dataFim: "2023-08-07",
										status: "Finalizado"
									},
									{
										id: 15,
										Titulo: "Concurso de Redação",
										CNPJ: "24.567.890/0001-15",
										InstituicaoEmpresa: "Secretaria de Educação",
										dataInicio: "2023-02-01",
										dataFim: "2023-04-01",
										status: "Finalizado"
									},
									{
										id: 16,
										Titulo: "Cine Comunidade",
										CNPJ: "25.678.901/0001-16",
										InstituicaoEmpresa: "Associação Cultural",
										dataInicio: "2024-07-01",
										dataFim: "2024-07-30",
										status: "Em Andamento"
									},
									{
										id: 17,
										Titulo: "Oficina de Inglês",
										CNPJ: "26.789.012/0001-17",
										InstituicaoEmpresa: "Idiomas para Todos",
										dataInicio: "2023-09-10",
										dataFim: "2023-12-10",
										status: "Finalizado"
									},
									{
										id: 18,
										Titulo: "Projeto Alimenta Bem",
										CNPJ: "27.890.123/0001-18",
										InstituicaoEmpresa: "Ação Solidária",
										dataInicio: "2024-02-01",
										dataFim: "2024-08-01",
										status: "Em Andamento"
									},
									{
										id: 19,
										Titulo: "Turismo Local Sustentável",
										CNPJ: "28.901.234/0001-19",
										InstituicaoEmpresa: "Turismo e Cultura",
										dataInicio: "2023-05-15",
										dataFim: "2023-10-15",
										status: "Cancelado"
									},
									{
										id: 20,
										Titulo: "Feira da Agricultura Familiar",
										CNPJ: "29.012.345/0001-20",
										InstituicaoEmpresa: "Agro Vida",
										dataInicio: "2024-01-10",
										dataFim: "2024-01-15",
										status: "Finalizado"
									}
								],
			projetosFiltered: null,
			filters: {
				selected: "all",
				search: "",
				},
		};
	},
	mounted(){
		this.filterProjetos();
	},
	methods: {
		greet() {
			alert(this.message);
		},
		filterProjetos() {
			switch (this.filters.selected) {
				case "all":
					this.projetosFiltered = this.projetos;
					console.log(this.projetosFiltered);
					break;
				case "andamento":
					this.projetosFiltered = this.projetos.filter((item) => item.status === "Em Andamento");
					break;
				case "canceled":
					this.projetosFiltered = this.projetos.filter((item) => item.status === "Cancelado");
					break;
				case "complete":
					this.projetosFiltered = this.projetos.filter((item) => item.status === "Finalizado");
					break;
				case "search":
					this.projetosFiltered = this.projetos.filter((item) => 
						item?.Titulo?.toLowerCase().includes(this.filters.search.toLowerCase()) ||
						item?.CNPJ?.includes(this.filters.search)

					);
					break;
			}
		},
	},
	watch: {
		"filters.search"() {
			console.log(this.filters.search);
			this.filters.selected = "search";
			this.filterProjetos();
		}
	},
};
</script>

<style scoped>

</style>