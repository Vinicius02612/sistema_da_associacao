<template>
	<v-container class="ma-0 fill-height align-start" max-width="100%">
		<v-row class="mt-0 ml-0 mr-0" :gutter="1">
			<v-col cols="12">
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
			
		};
	},
	
	methods: {
		greet() {
			alert(this.message);
		},
		
	},

};
</script>

<style scoped>

</style>