<template>
  <v-app>
		<div class="d-flex">
			<default-bar v-if="isLogged"/>
			<div class="d-flex">
				<default-top-bar v-if="isLogged"/>
			</div>
		</div>
		<default-view />
		<defout-footer v-if="isLogged"/>
		
  </v-app>
</template>

<script>
  import DefaultBar from './AppBar.vue'
  import DefaultView from './View.vue'
	import DefaultTopBar from './TopBar.vue';
	import DefoutFooter from './AppFooter.vue';

  import { useUserStore  } from '@/stores/user.store';

  const userStore = useUserStore();

  export default {
		components: {
			DefaultBar,
			DefaultView,
			DefaultTopBar,
			DefoutFooter,
		},
		computed: {
			isLogged() {
				return true; // userStore.isLogged;
				// return userStore.isLogged && userStore.getUser.isEmailVerified;
			},
		},
	};
</script>
