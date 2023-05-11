import { SET_USER_TOKEN_DATA_MUTATION } from "./storeconstants";
import axios from "axios";
import login from '../../interceptors/login.js'
import jwtInterceptor from '../../interceptors/jwt.js'
import { jwtDecrypt, tokenAlive } from "../../shared/jwtHelper";

const state = () => ({
    authData: {
      token: "",
      tokenExp: "",
      userId: "",
      customer_id: "",  
      refreshToken: "",
    },
    loginStatus: "",
  });
  
  const getters = {
    getLoginStatus(state) {
      return state.loginStatus;
    },
    getAuthData(state) {
      return state.authData;
    },
    isTokenActive(state) {
      if (!state.authData.tokenExp) {
        return false;
      }
      return tokenAlive(state.authData.tokenExp);
    },
  };

const actions = {
  async actionLogin({ commit }, payload, config) {
    const response = await login
      .post("/login/", payload, config)
      .catch((err) => {
        console.log(err);
      });

    if (response && response.data) {
        console.log(response.data)
      localStorage.setItem("isAuthenticated", "true");
    //   localStorage.setItem("access_token", response.data.access);
    //   localStorage.setItem("customer_id", response.data.customer);
    //   localStorage.setItem("refresh", response.data.refresh);
    //   localStorage.setItem("user_id", response.data.user);

//       commit("setloginStatus", "success");
//       commit("setaccessToken",response.data.access );
//       commit("setaccessToken",response.data.access );
//       user_id: response.data.user,
// //         customer_id: response.data.customer,
// //         refresh: response.data.refresh,
// //         access: response.data.access,
//     } else {
//       commit("setloginStatus", "failed");
//     }
          commit("setUserToken", response.data);
    
          commit("setloginStatus", "success");
        } else {
          commit("setloginStatus", "failed");
        }
  },
  actionUserToken({ commit },response ) {
    console.log(response)
    commit("setRefreshToken", response.data);

  },

  async userProfile({ commit }) {
    const response = await jwtInterceptor
      .get("http://localhost:3000/user-profile", {
        withCredentials: true,
        credentials: "include",
      })
      .catch((err) => {
        console.log(err);
      });

    if (response && response.data) {
      commit("setUserProfile", response.data);
    }
  },

  async userLogout({ commit }) {
    const response = await axios
      .get("http://localhost:3000/logout", {
        withCredentials: true,
        credentials: "include",
      })
      .catch((err) => {
        console.log(err);
      });

    if (response && response.data) {
      commit("setLogout", true);
      localStorage.removeItem("isAuthenticated");
    } else {
      commit("setLogout", false);
    }
  },
};

const mutations = {
    setloginStatus(state, data) {
    state.loginStatus = data;
  },
  setUserToken(state, data) {
    console.log(data)

    localStorage.setItem("access_token", data.access);
    localStorage.setItem("refresh_token", data.refresh);
    localStorage.setItem("userId", data.user);
    localStorage.setItem("customer_id", data.customer);

    const jwtDecodedValue = jwtDecrypt(data.access);
    const newTokenData = {
      token: data.access,
      // refreshToken:localStorage.getItem("refresh_token"),
      tokenExp: jwtDecodedValue.exp,
      userId: jwtDecodedValue.user_id,
      customer_id: jwtDecodedValue.customer_id,
    };
      console.log(newTokenData)
    state.authData = newTokenData;
  },
  setRefreshToken (state, data) {
    console.log(data)

    localStorage.setItem("access_token", data.access);
    localStorage.setItem("userId", data.user);
    localStorage.setItem("customer_id", data.customer);

    const jwtDecodedValue = jwtDecrypt(data.access);
    const newTokenData = {
      token: data.access,
      // refreshToken:localStorage.getItem("refresh_token"),
      tokenExp: jwtDecodedValue.exp,
      userId: jwtDecodedValue.user_id,
      customer_id: jwtDecodedValue.customer_id,
    };
      console.log(newTokenData)
    state.authData = newTokenData;
  },

  
//   setRefreshToken (state, data) {
//     const authData = {
//         userId:data.user_id,
//         customer_id:data.customer_id,
//         refreshToken:data.refresh,
//         token:data.access,
//     }
//     state.authData = authData;
        
//       },

  setUserProfile(state, data) {
    const userProfile = {
      id: data.id,
      lastName: data.lastName,
      firstName: data.firstName,
      email: data.email,
      phone: data.phone,
    };
    state.userProfile = userProfile;
  },

  setLogout(state, payload) {
    state.logOut = payload;
  }
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};