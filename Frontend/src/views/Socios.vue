<template>
	<v-container class="ma-0 fill-height align-start" max-width="100%">
		<v-row class="mt-0 ml-0 mr-0" :gutter="1">
			<v-col cols="12">
				<div class="d-flex justify-space-between align-center mt-2">
					<div class ="d-flex" style="width: 30%">
						<v-text-field
						class=" mr-5 bg-grey-lighten-4"
						append-inner-icon="mdi-magnify"
						label="Busca por nome ou CPF"
						v-model="filters.search"
						max-width="70%"
						variant="outlined"
						density="compact"
						hide-details
						/>
						<v-btn append-icon="mdi-plus" color="primary" to="/socios/adicionar" variant="elevated">
							Adicionar sócio
						</v-btn>
					</div>
					<div class="d-flex align-center">
						<span>Filtros: </span>
						<v-btn
							class="ma-1 d-flex align-center"
							color="primary"
							variant="outlined"
							@click="filters.selected = true, filterSocios()"
						>
							<v-tooltip
								activator="parent"
								location="bottom"
							>
								Com Atividade
							</v-tooltip>
							<v-icon>mdi-checkbox-marked-circle-outline</v-icon>
						</v-btn>
						<v-btn
							class="ma-1 d-flex align-center"
							variant="outlined"
							color="red"
							@click="filters.selected = false, filterSocios()"
						>
							<v-tooltip
								activator="parent"
								location="bottom"
							>
								Sem Atividade
							</v-tooltip>
							<v-icon>mdi-close</v-icon>
						</v-btn>
						<v-btn
							class="ma-1 d-flex align-center border-lg border-opacity-75"
							variant="outlined"
							@click="filters.selected = 'all', filterSocios()"
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
							<th>CPF</th>
							<th>Data de Nascimento</th>
							<th>Pessoas na Família</th>
							<th>Cargo</th>
							<th>Possui Atividade</th>
							<th>Ações</th>
						</tr>
					</thead>
					<tbody>
						<tr
							v-for="(item, index) in sociosFiltered"
							:key="item.Id"
							:style="{ backgroundColor: index % 2 === 0 ? 'white' : '#f8f8f8' }"
						>
							<td>{{ item.Nome }}</td>
							<td>{{ item.CPF }}</td>
							<td><DateLabel :date="new Date(item.DataDeNascimento)" /> </td>
							<td>{{ item.PessoasNaFamilia }}</td>
							<td>{{ item.Cargo }}</td>
							<td>
								<v-chip
									:color="item.PossuiAtividade ? 'green' : 'red'"
									class="d-flex justify-center bg-opacity-50"
									variant="outlined"
								>
									<span v-if="item.PossuiAtividade">sim</span>
									<span v-else>não</span>
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
											Bloquear
										</v-tooltip>
										<v-icon size="x-large">mdi-cancel</v-icon>
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
import axios from 'axios';
export default {
    name: 'Socios',
    components: {
        DateLabel,
    },
    data() {
        return {
            message: 'Hello, Vue!',
            socios: [], // Initialize socios as an empty array
            sociosFiltered: null,
            filters: {
                selected: "all",
                search: "",
            },
        };
    },
    async mounted() { // Use async here because you'll be awaiting loadSocios
        await this.loadSocios(); // First, load the data
        this.filterSocios(); // Then, apply initial filters
    },
    methods: {
        greet() {
            alert(this.message);
        },
        async loadSocios() {
            try {
                const response = await axios.get('http://localhost:8000/users', {
                    headers: {
                        'Content-Type': 'application/json',
                    }
                });
                if (response.status === 200) {
                    this.socios = response.data.map(user => ({
                        Id: user.id,
                        Nome: user.name,
                        CPF: user.cpf,
                        DataDeNascimento: user.data_nascimento,
                        PessoasNaFamilia: user.quantidade,
                        Cargo: user.cargo,
                        PossuiAtividade: user.possui_atividade, // Ensure this matches your API response if it exists, otherwise set a default
                        Email: user.email
                    }));
                }
            } catch (error) {
                console.error('Erro ao carregar sócios:', error);
                alert('Erro ao carregar lista de sócios');
            }
        },
        filterSocios() {
            let tempSocios = [...this.socios]; // Create a copy to filter

            if (this.filters.search) {
                tempSocios = tempSocios.filter((item) =>
                    item?.Nome?.toLowerCase().includes(this.filters.search.toLowerCase()) ||
                    item?.CPF?.includes(this.filters.search)
                );
            }

            switch (this.filters.selected) {
                case "all":
                    // If "all" and no search, it's just the original socios
                    break; // No need to re-assign tempSocios here as it's already a copy of this.socios or filtered by search
                case true:
                    tempSocios = tempSocios.filter((item) => item.PossuiAtividade);
                    break;
                case false:
                    tempSocios = tempSocios.filter((item) => !item.PossuiAtividade);
                    break;
            }
            this.sociosFiltered = tempSocios;
            console.log(this.sociosFiltered);
        },
    },
    watch: {
        "filters.search"() {
            console.log(this.filters.search);
            this.filters.selected = "search"; // This might not be necessary if you handle search within filterSocios
            this.filterSocios();
        },
        "filters.selected"() { // Watch for changes in selected filter as well
            this.filterSocios();
        }
    },
};
</script>

<style scoped>

</style>