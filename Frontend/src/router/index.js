// Composables
import { createRouter, createWebHistory } from "vue-router";
import { useUserStore } from "@/stores/user.store";

const routes = [
  {
    path: "/",
    component: () => import("@/layouts/default/Default.vue"),
    children: [
      {
        path: "",
        name: "Home",
        component: () => import("@/views/Home.vue"),
        meta: { requiresAuth: true, preload: true },
      },
			{
				path: "/login",
				name: "LoginView",
				component: () => import("@/views/Login.vue"),
				meta: { requiresAuth: false, preload: true },
			},
    ],
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
  scrollBehavior() {
    document.getElementById("app").scrollIntoView({ behavior: "smooth" });
  },
});

// router.beforeEach((to, from, next) => {
//   const userStore = useUserStore();

//   if (!userStore.getIsLogged) {
//     if (
//       to.name === "Login" ||
//       to.name === "Register" ||
//       to.name === "ResetPassword" ||
//       to.name === "ForgotPassword" ||
//       to.name === "ConfirmPasswordEmail"
//     ) {
//       next();
//     } else if (to.meta.requiresAuth) {
//       next({ name: "Login" });
//     } else {
//       next();
//     }
//   } else {
//     if (to.name === "Home") {
//       next({ name: "Connections" });
//     }
//     next();
//   }
// });

export default router;
