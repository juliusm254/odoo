import { createApp } from 'vue'
import './index.css'
// import Vue from "vue"
import App from "./App.vue";
import router from "./router";
import store from "./store";
import axios from "axios";

axios.defaults.baseURL = "http://127.0.0.1:8000/customers";

let refresh = false;

axios.interceptors.request.use((config) => {
    const authData = store.getters["auth/getAuthData"];
    console.log(authData)
    if (authData == null) {
      return config;
    }
  
    config.headers.common["Authorization"] = `Bearer ${authData.token}`;
    return config;
  });
  
  axios.interceptors.response.use(
    (response) => {
      return response;
    },
    async (error) => {
      if (error.response.status === 401 && !refresh) {
        refresh = true;
        const authData = store.getters["auth/getAuthData"];
        const payload = {
          access: authData.token,
          refresh: localStorage.getItem("refresh_token"),
        };

        // axios.interceptors.response.use(resp => resp, async error => {
        //     if (error.response.status === 401 && !refresh) {
        //         refresh = true;
        
                console.log(payload)
  
        var response = await axios.post(
          "api/token/refresh/", 
          payload
        );
        await store.dispatch("auth/actionUserToken", response);
        error.config.headers[
          "Authorization"
        ] = `Bearer ${response.data.access}`;
        return axios(error.config);
      } 
      // else {
      //   return Promise.reject(error);
      // }
      else {
        refresh = false;
        return Promise.reject(error);
      }
      
      
    }
    
  );

createApp(App).use(store).use(router, axios).mount("#app");
