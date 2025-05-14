<template>
	<v-container class="ma-0 fill-height align-start" max-width="100%">
		<v-row class="mt-0 ml-0 mr-0" :gutter="1">
			<v-col cols="12">
				<v-card class="align-center justify-center">
					<v-card-title class="align-start justify-start">
						Detalhes do Sócio
					</v-card-title>
					<v-card-text>
							<div class="d-flex align-center justify-center" style="width: 100%;">
								<v-row class="mt-0 ml-0 mr-0 align-start justify-center" :gutter="1">
									<v-col cols="4">
										<span>Nome</span>
										<v-text-field
										variant="outlined"
										v-model="data.name"
										:rules="[ruleRequired, ruleFullName]"
										size="compact"
										></v-text-field>
										
										<span>CPF</span>
										<v-text-field
											variant="outlined"
											v-model="data.cpf"
											:rules="[ruleRequired, ruleFullName]"
											size="compact"
										></v-text-field>
										
										<span>Mantem atividade agrícola, artesanal ou cultural na cominidade</span>
										<v-combobox
											width="20%"
											v-model="data.atvNaComunidade"
											:items="atividadeAgricola.map(item => item.text)"
											variant="outlined"
											:rules="[ruleRequired]"
										></v-combobox>

									</v-col>

									<v-col cols="4">
										<span>Email</span>
										<v-text-field
											variant="outlined"
											v-model="data.email"
											:rules="[ruleRequired, ruleEmail]"
										></v-text-field>
										
										<div class="d-flex align-center justify-center" style="width: 100%;">
											<div class="mr-3" style="width: 50%;">
												<span>Cargo</span>
												<v-combobox
												v-model="data.cargo"
												:items="cargos.map(item => item.text)"
												variant="outlined"
												:rules="[ruleRequired]"
												></v-combobox>
											</div>
											
											<div class="ml-3" style="width: 50%;">
												<span>Quantidade de pessoas na família</span>
												<v-text-field
												type="number"
												variant="outlined"
												v-model="data.familia"
												:rules="[ruleRequired]"
												></v-text-field>
											</div>
										</div>

										<div class="d-flex align-center justify-center" style="width: 100%;">
											<div class="mr-3" style="width: 50%;">
												<span>sexo</span>
												<v-checkbox class="my-0" value="homem" label="Homem" v-model="data.sexo"></v-checkbox>
												<v-checkbox class="my-0" value="mulher" label="Mulher" v-model="data.sexo"></v-checkbox>
											</div>
											
											<div class="ml-3" style="width: 50%;">
												<span>Data de nascimento</span>
												<v-date-input
													clearable
													v-model="data.birthDate"
													variant="outlined"></v-date-input>
											</div>
										</div>

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
				name: '',
				email: '',
				cpf: '',
				birthDate: '',
				cargo: '',
				familia: '',
				atvNaComunidade: '',
				sexo: '',
			},
			atividadeAgricola: [
				{ text: 'Sim', value: true },
				{ text: 'Não', value: false }
			],
			cargos: [
				{ text: 'Presidente', value: 'presidente' },
				{ text: 'Vice-Presidente', value: 'vice-presidente' },
				{ text: 'Diretor', value: 'diretor' },
				{ text: 'Gerente', value: 'gerente' },
				{ text: 'Tesoureiro', value: 'tesoureiro' },
				{ text: 'Secretário', value: 'secretario' },
				{ text: 'Fiscal', value: 'fiscal' },		
				{ text: 'Suplente', value: 'suplente' },
				{ text: 'Associado', value: 'associado' },
				{ text: 'Funcionário', value: 'funcionario' }
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