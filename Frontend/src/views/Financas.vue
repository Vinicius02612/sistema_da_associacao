<template>
	<v-container class="ma-0 fill-height align-start" max-width="100%">
		<v-row class="mt-0 ml-0 mr-0" :gutter="1">
			<v-col cols="12">
				<div class="d-flex justify-space-between align-center">
					<div class="d-flex" width="50%">
						<v-hover v-slot:default="{ isHovering, props }">
							<v-card width="50%">
								<v-card-title class="d-flex align-center justify-space-between">
									Receita Total
									<v-icon class="text-green">mdi-hand-coin-outline</v-icon>
								</v-card-title>
								<v-card-text>
									<v-btn class="d-flex justify-space-between" variant="flat" width="100%" >
										<h2>R$ 10.000,00</h2>
										<v-icon size="x-large">mdi-arrow-right</v-icon>
									</v-btn>
								</v-card-text>
							</v-card>
						</v-hover>
						<v-hover v-slot:default="{ isHovering, props }">
							<v-card class="ml-3">
								<v-card-title class="d-flex align-center justify-space-between">
									Despesa Total
									<v-icon class="text-red">mdi-hand-coin-outline</v-icon>
								</v-card-title>
								<v-card-text>
									<v-btn class="d-flex justify-space-between" variant="flat" width="100%" >
										<h2>R$ 1.000,00</h2>
										<v-icon size="x-large">mdi-arrow-right</v-icon>
									</v-btn>
								</v-card-text>
							</v-card>
						</v-hover>
					</div>
				</div>
			</v-col>

			<v-col cols="12">
				<v-card>
					<v-card-title class="d-flex align-center justify-space-between">
						Mensalidades
						<v-btn append-icon="mdi-plus" color="primary" to="/financas/adicionar" variant="elevated">
							Adicionar Mensalidade
						</v-btn>
					</v-card-title>
					<v-card-text>

						<v-table>
							<thead>
								<tr>
									<th>Titular</th>
									<th>CPF</th>
									<th>Data de Nascimento</th>
									<th>Cargo</th>
									<th>Valor</th>
									<th>Status</th>
									<th>Ações</th>
								</tr>
							</thead>
							<tbody>
								<tr
								v-for="(item, index) in MensalidadesFiltered"
								:key="item.cpf"
								:style="{ backgroundColor: index % 2 === 0 ? 'white' : '#f8f8f8' }"
								>
								<td>{{ item.Titular }}</td>
								<td>{{ item.CPF }}</td>
								<td><DateLabel :date="new Date(item.DataNascimento)" /> </td>
								<td>{{ item.Cargo }}</td>
								<td>R$ {{ item.Valor.toFixed(2) }}</td>
								<td>
									<v-chip
									:color="item.EmAtraso ? 'red' : 'green'"
									class="chip-size d-flex justify-center"
									variant="outlined"
									>
									{{ item.EmAtraso ? 'Atrasada' : 'Em Dia' }}
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
		</v-card-text>
	</v-card>
			</v-col>
			
		</v-row>
	</v-container>	
</template>

<script>
import DateLabel from '@/components/ui/DateLabel.vue';

export default {
	name: 'Mensalidades',
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