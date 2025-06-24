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
									<v-btn class="d-flex justify-space-between" variant="flat" width="100%" to="/financas/receitas">
										<h2>R$ {{totalReceitas}}</h2>
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
									<v-btn class="d-flex justify-space-between" variant="flat" width="100%" to="/financas/despesas">
										<h2>R$ 457.89</h2>
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
						Receitas
						<v-btn append-icon="mdi-plus" color="primary" to="/financas/adicionar" variant="elevated">
							Adicionar Receita
						</v-btn>
					</v-card-title>
					<v-card-text>

						<v-table>
							<thead>
								<tr>
									<th>Origem</th>
									<th>Data</th>
									<th>valor</th>
									<th>Ações</th>
								</tr>
							</thead>
							<tbody>
								<tr
								v-for="(item, index) in ReceitasFiltered"
								:key="item.id"
								:style="{ backgroundColor: index % 2 === 0 ? 'white' : '#f8f8f8' }"
								>
								<td>{{ item.Origem }}</td>
								<td><DateLabel :date="new Date(item.Data)" /> </td>
								<td>R$ {{ item.Valor.toFixed(2) }}</td>
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
	name: 'receitas',
	components: {
		DateLabel,
	},
	data() {
		return {
			message: 'Hello, Vue!',
			Receitas: [
									{ id: 1, Origem: "Venda de artesanato", Data: "2025-05-01", Valor: 45.50 },
									{ id: 2, Origem: "Doação", Data: "2025-05-02", Valor: 60.00 },
									{ id: 3, Origem: "Venda de artesanato", Data: "2025-05-03", Valor: 32.75 },
									{ id: 4, Origem: "Doação", Data: "2025-05-04", Valor: 25.00 },
									{ id: 5, Origem: "Venda de artesanato", Data: "2025-05-05", Valor: 68.90 },
									{ id: 6, Origem: "Doação", Data: "2025-05-06", Valor: 15.00 },
									{ id: 7, Origem: "Venda de artesanato", Data: "2025-05-07", Valor: 40.00 },
									{ id: 8, Origem: "Doação", Data: "2025-05-08", Valor: 50.00 },
									{ id: 9, Origem: "Venda de artesanato", Data: "2025-05-09", Valor: 35.20 },
									{ id: 10, Origem: "Doação", Data: "2025-05-10", Valor: 20.00 },
									{ id: 11, Origem: "Venda de artesanato", Data: "2025-05-11", Valor: 55.00 },
									{ id: 12, Origem: "Doação", Data: "2025-05-12", Valor: 30.00 },
									{ id: 13, Origem: "Venda de artesanato", Data: "2025-05-13", Valor: 65.99 },
									{ id: 14, Origem: "Doação", Data: "2025-05-14", Valor: 10.50 },
									{ id: 15, Origem: "Venda de artesanato", Data: "2025-05-15", Valor: 47.30 },
									{ id: 16, Origem: "Doação", Data: "2025-05-16", Valor: 22.00 },
									{ id: 17, Origem: "Venda de artesanato", Data: "2025-05-17", Valor: 28.45 },
									{ id: 18, Origem: "Doação", Data: "2025-05-18", Valor: 60.00 },
									{ id: 19, Origem: "Venda de artesanato", Data: "2025-05-19", Valor: 38.80 },
									{ id: 20, Origem: "Doação", Data: "2025-05-20", Valor: 18.00 }
								],
			ReceitasFiltered: null,
			filters: {
				selected: "all",
				},
		};
	},
	mounted(){
		this.filterReceitas();
	},
	methods: {
		greet() {
			alert(this.message);
		},
		filterReceitas() {
			switch (this.filters.selected) {
				case "all":
					this.ReceitasFiltered = this.Receitas;
					break;
			}
		},
	},
	computed: {
		totalReceitas() {
			return this.Receitas.reduce((total, receita) => total + receita.Valor, 0).toFixed(2);
		},
	},
};

</script>

<style scoped>

</style>