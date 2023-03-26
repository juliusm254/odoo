import { createRouter, createWebHistory } from "vue-router";
import HomePage from "../views/HomePage.vue";
import LogIn from "../views/LogIn.vue";
import OrderEdit from "../views/OrderEdit.vue";
import TruckAdd from "../views/TruckAdd.vue";
import DriverAdd from "../views/DriverAdd.vue";
import TraillerAdd from "../views/TraillerAdd.vue";
import DriverList from "../views/DriverList.vue";
import OrderBulk from "../views/OrderBulk.vue";
import store from "../store";

const routes = [
  {
    path: "/",
    name: "HomePage",
    component: HomePage,
  },
  {
    path: "/login",
    name: "LogIn",
    component: LogIn,
  },
  {
    path: "/add-driver",
    name: "DriverAdd",
    component: DriverAdd,
  },

  {
    path: "/edit-order",
    name: "OrderEdit",
    component: OrderEdit,
  },
  {
    path: "/add-truck",
    name: "TruckAdd",
    component: TruckAdd,
  },
  {
    path: "/add-trailer",
    name: "TraillerAdd",
    component: TraillerAdd,
  },
  {
    path: "/drivers",
    name: "DriverList",
    component: DriverList,
  },
  {
    path: "/bulk-balance",
    name: "OrderBulk",
    component: OrderBulk,
  },
  {
    path: "/orders",
    name: "OrderList",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import( "../views/OrderList.vue"),
  },
];


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;

router.beforeEach(async (to, from, next) => {
  console.log(store.getters["auth/getAuthData"].token);
  if (!store.getters["auth/getAuthData"].token) {
    const access_token = localStorage.getItem("access_token");
    const refresh_token = localStorage.getItem("refresh_token");
    if (access_token) {
      const data = {
        access: access_token,
        refresh: refresh_token,
      };
      store.commit("auth/setUserToken", data);
    }
  }
  let auth = store.getters["auth/isTokenActive"];

  // if (!auth) {
  //   const authData = store.getters["auth/getAuthData"];
  //   if (authData.token) {
  //     const payload = {
  //       access: authData.token,
  //       refresh: localStorage.getItem("refresh_token"),
  //     };
  //     console.log(payload);
  //     const refreshResponse = await axios.post(
  //       "api/token/refresh/",
  //       payload
  //     );
  //     store.commit("auth/setRefreshToken", refreshResponse.data);
  //     auth = true;
  //   }
  // }

  if (to.fullPath == "/") {
    return next();
  } else if (auth && !to.meta.requiredAuth) {
    // return next({ path: "/" });
    return next();
  } else if (!auth && to.meta.requiredAuth) {
    return next({ path: "/login" });
  }

  return next();
});
