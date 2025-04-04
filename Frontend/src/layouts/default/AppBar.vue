<template>
  <v-navigation-drawer
    :rail="!isLocked"
    permanent
    elevation="0"
    app
    :expand-on-hover="!isLocked  && !$vuetify.display.mobile"
  >
	<v-divider></v-divider>
	<v-list density="compact" nav>
		<v-list-item prepend-icon="mdi-robot" :title="$t('menu.connections')" to="/connections" active-class="custon-active-iten"></v-list-item>
		<!-- <v-list-item prepend-icon="mdi-calendar" :title="$t('events.header')" to="/events" active-class="custon-active-iten"></v-list-item>
		<v-list-item prepend-icon="mdi-bell" :title="$t('alerts.header')" to="/alerts" active-class="custon-active-iten"></v-list-item> -->
		<!-- <v-list-item prepend-icon="mdi-tools" :title="$t('menu.testes')" to="/testes" active-class="custon-active-iten"></v-list-item>  -->
		<v-divider></v-divider>
      <v-list-item prepend-icon="mdi-exit-to-app" :title="$t('menu.exit')" @click="logout"></v-list-item>
    </v-list>

    <template v-slot:append>
      <v-list density="compact" nav class="d-none d-md-block">
        <v-list-item 
					:prepend-icon="lockMenuIcon"
					:title="lockMenuText"
					value="fixed"
					@click="toggleFixed"
					:active="isLocked"
					active-class="custon-active-iten"
				>
				</v-list-item>
			</v-list>
			
			<!-- <div class="d-flex flex-row">				
				<span v-if="isLocked">{{ "Versão: " }}</span><DefaultFooter/>
			</div> -->
    </template>
	</v-navigation-drawer>
</template>
<script>
	import DefaultFooter from '@/layouts/default/AppFooter.vue';
  import { useUserStore  } from '@/stores/user.store';
  import { createCheckout } from '@/services/checkout.service';

  const userStore = useUserStore();

  export default {
		components: {
			DefaultFooter,
		},
    data () {
      return {
        drawer: true,
        rail: true,
        isLocked: false,
      }
    },

    methods: {
      toggleRail () {
        this.rail = !this.rail
      },

      toggleFixed () {
        this.isLocked = !this.isLocked
        this.rail = this.isLocked;
      },

      logout() {
        localStorage.clear();
        userStore.isLogged = false;
				window.location = '/';
      },

      async checkout() {
        const data = await createCheckout();
        window.location = data.url;
      }
    },

    computed: {
			
      lockMenuIcon() {
        return this.isLocked ? 'mdi-pin-off' : 'mdi-pin'
      },

      lockMenuText() {
        return !this.isLocked ? this.$t('menu.fixMenu') : this.$t('menu.fixedMenu')
      },
    }
  }
</script>
<style scoped>
	.custon-active-iten {
		background-color: rgba(41, 213, 58, 0.2) !important;

	}
</style>