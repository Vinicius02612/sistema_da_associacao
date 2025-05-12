<template>
	<v-container class="ma-0 fill-height" max-width="100%">
		<v-row class="mt-0 ml-0 mr-0" :gutter="1">
			<v-col cols="12">
				<span class="ml-4 text-h5">Seus atalhos</span>
				<div>
					<v-hover v-slot:default="{ isHovering, props }">
						<v-btn
							v-bind="props"
							class="ma-4 text-h6"
							@click=""
							prepend-icon="mdi-account-plus"
							:color="isHovering ? 'primary' : ''"
							size="x-large"
							stacked
						>
							Adicionar sócio
						</v-btn>
					</v-hover>
					<v-hover v-slot:default="{ isHovering, props }">
						<v-btn
							v-bind="props"
							class="ma-4 text-h6"
							@click=""
							prepend-icon="mdi-calendar-month"
							:color="isHovering ? 'primary' : ''"
							size="x-large"
							stacked
						>
							Mensalidades
						</v-btn>
					</v-hover>
					<v-hover v-slot:default="{ isHovering, props }">
						<v-btn
							v-bind="props"
							class="ma-4 text-h6"
							@click=""
							prepend-icon="mdi-plus-circle-outline"
							:color="isHovering ? 'primary' : ''"
							size="x-large"
							stacked
						>
							Novo Projeto
						</v-btn>
					</v-hover>
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
							v-for="(item, index) in numbers"
							:key="item.id"
							:style="{ backgroundColor: index % 2 === 0 ? 'white' : '#f8f8f8' }"
						>
							<td>{{ item.id }}</td>
							<td>
								<PhoneLabel v-if="item.number" :data="item.number" />
								<template v-else>Não conectado</template>
							</td>
							<td>{{ item.name }}</td>
							<td><DateLabel :date="new Date(item.fstConnection)" /> </td>
							<td><DateLabel :date="new Date(item.lastConnection)" /> </td>
							<td>
								<v-chip
									:color="getStatusColor(item.status)"
									:append-icon="getStatusIcon(item.status)"
									class="chip-size d-flex justify-space-between"
									size="large"
									variant="tonal"
								>
									{{ getStatusText(item.status) }}
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
										v-tooltip:top="'Visualizar'"
										@click="viewNumber(item)"
									>
										<v-icon size="x-large">mdi-pencil</v-icon>
									</v-btn>
									<v-btn
										width="32"
										height="32"
										v-tooltip:top="dialogAction(item.status).label"
										@click="
											openDialogAction(dialogAction(item.status).action, item.id)
										"
									>
										<v-icon size="x-large">
											mdi-trash-can-outline
										</v-icon>
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
export default {
	name: 'Home',
	data() {
		return {
			message: 'Hello, Vue!'
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