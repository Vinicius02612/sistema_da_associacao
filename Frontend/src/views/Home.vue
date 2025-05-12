<template>
	<v-container class="ma-0 fill-height" max-width="100%">
		<v-row>
			<v-col cols="12">
				<span class="ml-4 text-h5">Seus atalhos</span>
				<div>
					<v-hover v-slot:default="{ isHovering, props }">
						<v-btn 
							class="ma-4 text-h6"
							@click=""
							prepend-icon="mdi-account-plus"
							:color="isHovering ? 'primary' : ''"
							size="x-large"
							stacked>
							Adicionar sócio
						</v-btn>
						<v-btn class="ma-4 text-h6" @click="" prepend-icon="mdi-calendar-month" size="x-large" stacked>Mensalidades</v-btn>
						<v-btn class="ma-4 text-h6" @click="" prepend-icon="mdi-plus-circle-outline" size="x-large" stacked>Novo Projeto</v-btn>
					</v-hover>
				</div>
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