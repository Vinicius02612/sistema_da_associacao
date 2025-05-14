<template>
	<v-container class="ma-0 fill-height align-start" max-width="100%">
		<v-row class="mt-0 ml-0 mr-0" :gutter="1">

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
							v-for="(item, index) in socios"
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

export default {
	name: 'Socios',
	components: {
		DateLabel,
	},
	data() {
		return {
			message: 'Hello, Vue!',
			socios: [
								{
									Id: 1,
									Nome: "Carlos Silva",
									CPF: "123.456.789-00",
									DataDeNascimento: "1985-06-15",
									PessoasNaFamilia: 4,
									Cargo: "Gerente",
									PossuiAtividade: true
								},
								{
									Id: 2,
									Nome: "Maria Oliveira",
									CPF: "234.567.890-11",
									DataDeNascimento: "1990-12-01",
									PessoasNaFamilia: 3,
									Cargo: "Secretario",
									PossuiAtividade: false
								},
								{
									Id: 3,
									Nome: "João Pereira",
									CPF: "345.678.901-22",
									DataDeNascimento: "1978-03-23",
									PessoasNaFamilia: 5,
									Cargo: "Presidente",
									PossuiAtividade: true
								},
								{
									Id: 4,
									Nome: "Ana Souza",
									CPF: "456.789.012-33",
									DataDeNascimento: "1988-09-10",
									PessoasNaFamilia: 2,
									Cargo: "Vice-presidente",
									PossuiAtividade: false
								},
								{
									Id: 5,
									Nome: "Roberto Lima",
									CPF: "567.890.123-44",
									DataDeNascimento: "1995-04-17",
									PessoasNaFamilia: 1,
									Cargo: "Diretor",
									PossuiAtividade: true
								},
								{
									Id: 6,
									Nome: "Fernanda Costa",
									CPF: "678.901.234-55",
									DataDeNascimento: "1982-01-30",
									PessoasNaFamilia: 4,
									Cargo: "Tesoureiro",
									PossuiAtividade: true
								},
								{
									Id: 7,
									Nome: "Marcelo Nunes",
									CPF: "789.012.345-66",
									DataDeNascimento: "1975-07-08",
									PessoasNaFamilia: 6,
									Cargo: "Associado",
									PossuiAtividade: false
								},
								{
									Id: 8,
									Nome: "Paula Ribeiro",
									CPF: "890.123.456-77",
									DataDeNascimento: "1993-11-21",
									PessoasNaFamilia: 2,
									Cargo: "Funcionário",
									PossuiAtividade: true
								},
								{
									Id: 9,
									Nome: "Eduardo Gomes",
									CPF: "901.234.567-88",
									DataDeNascimento: "1980-05-13",
									PessoasNaFamilia: 3,
									Cargo: "Suplente",
									PossuiAtividade: false
								},
								{
									Id: 10,
									Nome: "Juliana Martins",
									CPF: "012.345.678-99",
									DataDeNascimento: "1991-10-05",
									PessoasNaFamilia: 2,
									Cargo: "Fiscal",
									PossuiAtividade: true
								},
								{
									Id: 11,
									Nome: "Luciano Rocha",
									CPF: "112.233.445-56",
									DataDeNascimento: "1987-08-19",
									PessoasNaFamilia: 4,
									Cargo: "Gerente",
									PossuiAtividade: true
								},
								{
									Id: 12,
									Nome: "Renata Mendes",
									CPF: "223.344.556-67",
									DataDeNascimento: "1994-06-02",
									PessoasNaFamilia: 1,
									Cargo: "Secretario",
									PossuiAtividade: false
								},
								{
									Id: 13,
									Nome: "André Torres",
									CPF: "334.455.667-78",
									DataDeNascimento: "1976-12-29",
									PessoasNaFamilia: 5,
									Cargo: "Diretor",
									PossuiAtividade: true
								},
								{
									Id: 14,
									Nome: "Bruna Farias",
									CPF: "445.566.778-89",
									DataDeNascimento: "1997-03-14",
									PessoasNaFamilia: 2,
									Cargo: "Associado",
									PossuiAtividade: false
								},
								{
									Id: 15,
									Nome: "Ricardo Vieira",
									CPF: "556.677.889-90",
									DataDeNascimento: "1983-07-06",
									PessoasNaFamilia: 3,
									Cargo: "Funcionário",
									PossuiAtividade: true
								},
								{
									Id: 16,
									Nome: "Tatiane Alves",
									CPF: "667.788.990-01",
									DataDeNascimento: "1992-09-25",
									PessoasNaFamilia: 1,
									Cargo: "Suplente",
									PossuiAtividade: false
								},
								{
									Id: 17,
									Nome: "Leandro Batista",
									CPF: "778.899.001-12",
									DataDeNascimento: "1981-11-11",
									PessoasNaFamilia: 4,
									Cargo: "Presidente",
									PossuiAtividade: true
								},
								{
									Id: 18,
									Nome: "Camila Ferreira",
									CPF: "889.900.112-23",
									DataDeNascimento: "1989-05-18",
									PessoasNaFamilia: 3,
									Cargo: "Fiscal",
									PossuiAtividade: true
								},
								{
									Id: 19,
									Nome: "Felipe Barros",
									CPF: "990.011.223-34",
									DataDeNascimento: "1979-10-27",
									PessoasNaFamilia: 5,
									Cargo: "Vice-presidente",
									PossuiAtividade: false
								},
								{
									Id: 20,
									Nome: "Isabela Cardoso",
									CPF: "101.112.334-45",
									DataDeNascimento: "1996-02-09",
									PessoasNaFamilia: 2,
									Cargo: "Tesoureiro",
									PossuiAtividade: true
								},
								{
									Id: 21,
									Nome: "Daniel Moreira",
									CPF: "121.314.151-61",
									DataDeNascimento: "1986-04-12",
									PessoasNaFamilia: 3,
									Cargo: "Gerente",
									PossuiAtividade: true
								},
								{
									Id: 22,
									Nome: "Larissa Dias",
									CPF: "131.415.161-71",
									DataDeNascimento: "1991-07-30",
									PessoasNaFamilia: 4,
									Cargo: "Secretario",
									PossuiAtividade: false
								},
								{
									Id: 23,
									Nome: "Thiago Rezende",
									CPF: "141.516.171-81",
									DataDeNascimento: "1977-12-01",
									PessoasNaFamilia: 6,
									Cargo: "Diretor",
									PossuiAtividade: true
								},
								{
									Id: 24,
									Nome: "Beatriz Cunha",
									CPF: "151.617.181-91",
									DataDeNascimento: "1998-06-21",
									PessoasNaFamilia: 2,
									Cargo: "Associado",
									PossuiAtividade: true
								},
								{
									Id: 25,
									Nome: "Gustavo Sales",
									CPF: "161.718.191-02",
									DataDeNascimento: "1984-01-16",
									PessoasNaFamilia: 4,
									Cargo: "Funcionário",
									PossuiAtividade: false
								},
								{
									Id: 26,
									Nome: "Aline Queiroz",
									CPF: "171.819.202-13",
									DataDeNascimento: "1990-09-14",
									PessoasNaFamilia: 1,
									Cargo: "Suplente",
									PossuiAtividade: true
								}
							]
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