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
										
										<span>CNPJ</span>
										<v-text-field
											variant="outlined"
											v-model="data.cnpj"
											:rules="[ruleRequired, ruleFullName]"
											size="compact"
										></v-text-field>
										
										<span>Descrição do projeto</span>
										<v-textarea
											v-model="data.descricao"
											variant="outlined"
											:rules="[ruleRequired]"
										></v-textarea>

									</v-col>

									<v-col cols="4">
										<span>Instituicao/Empresa	</span>
										<v-text-field
											variant="outlined"
											v-model="data.empresa"
											:rules="[ruleRequired, ruleEmail]"
										></v-text-field>

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
										<v-btn color="primary" class="ma-2" @click="greet" >
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
				empresa: '',
				cnpj: '',
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
		}
	},
};
</script>

<style scoped>

</style>