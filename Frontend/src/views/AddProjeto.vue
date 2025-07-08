<template>
	<v-container class="ma-0 fill-height align-start" max-width="100%">
		<v-row class="mt-0 ml-0 mr-0" :gutter="1">
			<v-col cols="12">
				<v-card class="align-center justify-center">
					<v-card-title class="align-start justify-start">
						Adicionar Projeto
					</v-card-title>
					<v-card-text>
							<div class="d-flex align-center justify-center" style="width: 100%;">
								<v-row class="mt-0 ml-0 mr-0 align-start justify-center" :gutter="1">
									<v-col cols="4">
										<span>Título deo Projeto</span>
										<v-text-field
										variant="outlined"
										v-model="data.titulo"
										:rules="[ruleRequired, ruleFullName]"
										size="compact"
										></v-text-field>
									</v-col>

									<v-col cols="4">
										

										<div class="d-flex align-center justify-center" style="width: 100%;">

											<div class="mr-3" style="width: 50%;">
												<span>Data de Início</span>
												<v-row dense>
													<v-col cols="4">
														<v-text-field
															variant="outlined"
															v-model="data.dayI"
															label="Dia"
															type="number"
															:min="1"
															:max="31"
															:rules="[ruleRequired]"
															size="compact"
														>
														</v-text-field>
													</v-col>
													<v-col cols="4">
														<v-text-field
															variant="outlined"
															v-model="data.monthI"
															label="Mês"
															type="number"
															:min="1"
															:max="12"
															:rules="[ruleRequired]"
															size="compact"
														>
														</v-text-field>
													</v-col>
													<v-col cols="4">
														<v-text-field
															variant="outlined"
															v-model="data.yearI"
															label="Ano"
															type="number"
															:min="1900"
															:max="2100"
															:rules="[ruleRequired]"
															size="compact"
														>
														</v-text-field>
													</v-col>
												</v-row>
											</div>
											<div class="ml-3" style="width: 50%;">
												<span>Data de Finalização</span>
												<v-row dense>
													<v-col cols="4">
														<v-text-field
															variant="outlined"
															v-model="data.dayF"
															label="Dia"
															type="number"
															:min="1"
															:max="31"
															:rules="[ruleRequired]"
															size="compact"
														>
														</v-text-field>
													</v-col>
													<v-col cols="4">
														<v-text-field
															variant="outlined"
															v-model="data.monthF"
															label="Mês"
															type="number"
															:min="1"
															:max="12"
															:rules="[ruleRequired]"
															size="compact"
														>
														</v-text-field>
													</v-col>
													<v-col cols="4">
														<v-text-field
															variant="outlined"
															v-model="data.yearF"
															label="Ano"
															type="number"
															:min="1900"
															:max="2100"
															:rules="[ruleRequired]"
															size="compact"
														>
														</v-text-field>
													</v-col>
												</v-row>
											</div>
										</div>

										<span>Status</span>
										<v-combobox
											v-model="data.status"
											:items="status.map(item => item.text)"
											variant="outlined"
											:rules="[ruleRequired]"
										></v-combobox>
										

									</v-col>
									<v-col class="d-flex align-center justify-center" cols="8">
										<v-btn color="primary" class="ma-2" @click="addProjeto" >
											Adicionar
										</v-btn>
									</v-col>
								</v-row>

							</div>
					</v-card-text>
				</v-card>
			</v-col>

		</v-row>
	</v-container>	
</template>

<script>
import DateLabel from '@/components/ui/DateLabel.vue';
import { VDateInput } from 'vuetify/labs/VDateInput'
import { ruleRequired, ruleEmail, ruleFullName } from '@/helpers/RulesHelper';
import axios from 'axios';
export default {
	name: 'Socios',
	components: {
		DateLabel,
		VDateInput
	},
	data() {
		return {
			message: 'Hello, Vue!',
			data: {
				titulo: '',
				dayI: '',
				monthI: '',
				yearI: '',
				dayF: '',
				monthF: '',
				yearF: '',
				dataInicio: '',
				datafim: '',
				descrição: '',
				status: '',
			},
			status: [
				{ text: 'Em Andamento', value: 'inProgress' },
				{ text: 'Finalizado', value: 'complete' },
				{ text: 'Cancelado', value: 'cancel' },
			],
			ruleRequired,
			ruleEmail,
			ruleFullName,
		};
	},
	methods: {
		greet() {
			alert(this.message);
		},
		//criar metodo para cadastrar projeto na api usando axios:http://localhost:8000/projetos/

		async addProjeto() {
			try {
				const data_inicio = `${this.data.yearI}-${String(this.data.monthI).padStart(2, '0')}-${String(this.data.dayI).padStart(2, '0')}`;
				const data_fim = `${this.data.yearF}-${String(this.data.monthF).padStart(2, '0')}-${String(this.data.dayF).padStart(2, '0')}`;

				const payload = {
					titulo: this.data.titulo,
					data_inicio: data_inicio,
					data_fim: data_fim,
		
				};

				console.log(payload);

				const response = await axios.post('http://localhost:8000/projetos/', payload,{
					headers: {
						'Content-Type': 'application/json',
					}
				});
				if (response.status === 200) {
					alert('Projeto adicionado com sucesso!');
					console.log(response.data);
					this.$router.push("/home");
				}
			} catch (error) {
				console.error('Erro:', error);
				alert('Erro ao adicionar projeto.');
			}
		}


	},
};
</script>

<style scoped>

</style>