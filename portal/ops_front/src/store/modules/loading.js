// import axios from "axios";
// import { LOADING_SPINNER_SHOW_MUTATION } from './storeconstants';

const state = () => ({
  isLoading: false
});


const mutations = {
  setIsLoading(state, status) {
    state.isLoading = status
  },

//   [SET_USER_TOKEN_DATA_MUTATION](state, payload) {
//     state.user_id = payload.user_id;
//     state.customer_id = payload.customer_id;
//     state.refresh = payload.refresh;
//     state.access = payload.access;
//   },
//   initializeStore(state) {
//     if (localStorage.getItem("access_token")) {
//       state.access = localStorage.getItem("access_token");
//       state.customer_id = localStorage.getItem("customer_id");
//       state.user_id = localStorage.getItem("user_id");
//       state.refresh = localStorage.getItem("refresh");
//       state.loginState = true;
//     } else {
//       state.access = "";
//       state.loginState = false;
//     }
//   },
};

// };

export default {
  namespaced: true,

  state,

//   getters,

//   actions,

  mutations,
};
