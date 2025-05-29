<template>
	<v-container class="ma-0 fill-height align-start" max-width="100%">
		<v-row class="mt-0 ml-0 mr-0" :gutter="1">
			<v-col cols="12">
				<span class="ml-4 text-h5">Seus atalhos</span>
				<div>
					<v-hover v-slot:default="{ isHovering, props }">
						<v-btn
							v-bind="props"
							class="ma-4 text-h6"
							prepend-icon="mdi-account-plus"
							:color="isHovering ? 'primary' : ''"
							size="x-large"
							stacked
							to="/socios/adicionar"
						>
							Adicionar sócio
						</v-btn>
					</v-hover>
					<v-hover v-slot:default="{ isHovering, props }">
						<v-btn
							v-bind="props"
							class="ma-4 text-h6"
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
							prepend-icon="mdi-plus-circle-outline"
							:color="isHovering ? 'primary' : ''"
							size="x-large"
							stacked
							to="/projetos/adicionar"
						>
							Novo Projeto
						</v-btn>
					</v-hover>
				</div>
			</v-col>

			<v-col cols="12">
				<v-card>
					<v-card-title>
						Projetos em andamento
					</v-card-title>
					<v-card-text>

					</v-card-text>
				</v-card>
			</v-col>
		</v-row>
	</v-container>	
</template>

<script>

export default {
	name: 'Home',
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