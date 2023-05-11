import { createRouter, createWebHistory } from "vue-router";
import axios from "axios";
import store from "../store";
import Home from "../views/Home.vue";
import OrderScan from "../views/OrderScan.vue";
import SafetyInspection from "../views/SafetyInspection.vue";
import Safetyform from "../components/Safetyform.vue";
import LabDetails from "../components/LabDetails.vue";
import Login from "../views/Login.vue";
import LabInspection from "../views/LabInspection.vue";
import LabResults from "../views/LabResults.vue";
import LabResultsDetails from "../components/LabResultsDetails.vue";
import LabVent from "../views/LabVent.vue";
import LabVentDetails from "../components/LabVentDetails.vue";
import Loading from "../views/Loading.vue";
import LoadingDetails from "../components/LoadingDetails.vue";
import PrintSafetyInspectionList from "../views/PrintSafetyInspectionList.vue";
import PrintSafetyDetails from "../components/PrintSafetyDetails.vue";
import LabSeal from "../views/LabSeal.vue";
import LabSealDetails from "../components/LabSealDetails.vue";
<<<<<<< Updated upstream
=======
import CustomerAdd from "../views/CustomerAdd.vue";
>>>>>>> Stashed changes

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
    meta: { requiredAuth: true }
  },
  {
    path: "/orderscan",
    name: "OrderScan",
    component: OrderScan,
    meta: { requiredAuth: true }
  },
  {
    path: "/safety-inspection",
    name: "SafetyInspection",
    component: SafetyInspection,
    meta: { requiredAuth: true }
  },
  {
    path: "/safety-checklist/:id",
    name: "Safetyform",
    component: Safetyform,
    meta: { requiredAuth: true }
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/lab-inspection",
    name: "LabInspection",
    component: LabInspection,
    meta: { requiredAuth: true }
  },
  {
    path: "/lab-details/:id",
    name: "LabDetails",
    component: LabDetails,
    meta: { requiredAuth: true }
  },
  {
    path: "/lab-results",
    name: "LabResults",
    component: LabResults,
    meta: { requiredAuth: true }
  },
  {
    path: "/lab-results/:id",
    name: "LabResultsDetails",
    component: LabResultsDetails,
    meta: { requiredAuth: true }
  },
  {
    path: "/lab-seal/",
    name: "LabSeal",
    component: LabSeal,
    meta: { requiredAuth: true }
  },
  {
    path: "/lab-seal/:id",
    name: "LabSealDetails",
    component: LabSealDetails,
    meta: { requiredAuth: true }
  },
  {
    path: "/lab-vent/",
    name: "LabVent",
    component: LabVent,
    meta: { requiredAuth: true }
  },
  {
    path: "/lab-vent/:id",
    name: "LabVentDetails",
    component: LabVentDetails,
    meta: { requiredAuth: true }
  },
  {
    path: "/loading",
    name: "Loading",
    component: Loading,
    meta: { requiredAuth: true }
  },
  {
    path: "/loading/:id",
    name: "LoadingDetails",
    component: LoadingDetails,
<<<<<<< Updated upstream
    meta: { requiredAuth: true }
=======
    // meta: { requiredAuth: true }
>>>>>>> Stashed changes
  },
  {
    path: "/print-safety",
    name: "PrintSafetyInspectionList",
    component: PrintSafetyInspectionList,
    meta: { requiredAuth: true }
  },
  {
    path: "/print-safety/:id",
    name: "PrintSafetyDetails",
    component: PrintSafetyDetails,
    meta: { requiredAuth: true }
  },
  {
<<<<<<< Updated upstream
=======
    path: "/add-customer",
    name: "CustomerAdd",
    component: CustomerAdd,
    // meta: { requiredAuth: true }
  },
  {
>>>>>>> Stashed changes
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
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
