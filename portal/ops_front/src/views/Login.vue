<template>
  <div>
    <div class="container text-dark">
      <div class="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
        <div class="bg-white py-8 px-6 shadow rounded-lg sm:px-10">
          <h1 class="h3 mb-3 font-weight-normal text-center">Please Sign In</h1>

          <p v-if="incorrectAuth">Incorrect Username</p>
          <!-- <form v-on:submit.prevent="login"> -->
          <form class="mb-0 space-y-6" v-on:submit.prevent="submit">
            <div class="field">
              <label class="block text-sm font-medium text-gray-700">Username</label>
              <div class="mt-1">
                <input
                  type="text"
                  name="username"
                  id="user"
                  required
                  v-model="username"
                  class="w-full form-control valid border-2 bg-white px-2 p-1 rounded"
                />
              </div>
            </div>
            <div class="field">
              <label class="block text-sm font-medium text-gray-700">Password</label>
              <div class="mt-1">
                <input
                  type="password"
                  name="password"
                  id="pass"
                  v-model="password"
                  required
                  class="w-full form-control valid border-2 bg-white px-2 p-1 rounded"
                />
              </div>
            </div>

            <div>
              <button                             
                type="submit"                
                class="w-full flex 
                    justify-center 
                    py-2 px-4 border 
                    border-transparent 
                    rounded-md shadow-sm 
                    text-sm font-medium 
                    text-white 
                    bg-green-600 
                    hover:bg-indigo-700 
                    focus:outline-none 
                    focus:ring-2 
                    focus:ring-offset-2
                    focus:ring-indigo-400"                
                  >Submit
                </button>              
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { useRouter } from "vue-router";
import { mapActions, mapGetters } from "vuex";

export default {
  data() {
    return {
      username: "",
      password: "",
      type: "OPERATIONS",
      incorrectAuth: false,
    };
  },
  computed: {
    ...mapGetters("auth", {
      loginState: "getLoginStatus",
    }),
  },
  // created() {
  //     this.actionLogin();
  // },

  methods: {
    ...mapActions("auth", {
      actionLogin: "actionLogin",
    }),

    // ...mapActions(["actionLogin"]),

    async submit() {
      console.log(this.username, this.password);

      let config = {
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Credentials": true
        },
      };

      const payload = {
        username: this.username,
        password: this.password,
        type: this.type,
      };

      
      await this.actionLogin(payload, config,{          
        });
      if (this.loginState == "success") {
        this.$router.push({ name: "Home" });
      } else {
        this.incorrectAuth = true;
      }
    },
  }, 

};
</script>
