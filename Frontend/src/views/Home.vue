<template>
	<div class="home">
		<v-card class="d-flex align-center justify-center">
			<v-card-text>
				<v-img src="@/assets/Logo1.png" max-width="400px"></v-img>
				<h1>Welcome to the Home Page</h1>
			</v-card-text>
		</v-card>
	</div>
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
	}
};
</script>

<style scoped>
.home {
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: center;
	text-align: center;
	margin-top: 50px;
}
</style>