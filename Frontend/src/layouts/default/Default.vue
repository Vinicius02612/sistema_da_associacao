<template>
  <v-app>
		<default-top-bar v-if="isLogged"/>
    <default-bar v-if="isLogged"/>
    <default-view />
  </v-app>
</template>

<script>
  import DefaultBar from './AppBar.vue'
  import DefaultView from './View.vue'
	import DefaultTopBar from './TopBar.vue';
  import { useUserStore  } from '@/stores/user.store';

  const userStore = useUserStore();

  export default {
		components: {
			DefaultBar,
			DefaultView,
			DefaultTopBar,
		},
		computed: {
			isLogged() {
				return userStore.isLogged && userStore.getUser.isEmailVerified;
			},
		},
	};
</script>
