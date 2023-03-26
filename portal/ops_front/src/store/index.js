import { createStore } from "vuex";
import authModule from "./modules/auth";
import loadingModule from "./modules/loading";

const store = createStore({
  modules: {
    auth: authModule,
    loading: loadingModule
  },
});

export default store;
