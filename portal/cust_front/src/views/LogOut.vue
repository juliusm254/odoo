<!-- <template>
    <div class="container">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Log In</h1>

                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Email</label>
                        <div class="control">
                            <input type="email" name="email" class="input" v-model="username">
                        </div>
                    </div>

                    <div class="field">
                        <label>Password</label>
                        <div class="control">
                            <input type="password" name="password" class="input" v-model="password">
                        </div>
                    </div>
                
                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-success">Log In</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: 'LogIn',
        data() {
            return {
                username: '',
                password: '',
                errors: []
            }
        },
        methods: {
            async submitForm() {

                this.$store.commit('setIsLoading', true)

                axios.defaults.headers.common['Authorization'] = ''
                localStorage.removeItem('token')

                const formData = {
                    username: this.username,
                    password: this.password
                }

                await axios
                    .post('api/v1/token/login/', formData)
                    .then(response => {
                        const token = response.data.auth_token

                        this.$store.commit('setToken')

                        axios.defaults.headers.common['Authorization'] = 'Token ' + token

                        localStorage.setItem('token', token)

                        this.$router.push('/dashboard/my-account')
                    })
                    .catch(error => {
                        if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }
                        } else if (error.message) {
                            this.errors.push('Something Went Wrong. Please Try Again')
                        }
                    })

                this.$store.commit('setIsLoading', false)    
            }
        }
    }
</script> -->

<template>
  <div>
    <div class="container text-dark">
      <div class="row justify-content-md-center">
        <div class="col-md-5 p-3 login justify-md-center">
          <h1 class="h3 mb-3 font-weight-normal text-center">Please Sign In</h1>

          <p v-if="incorrectAuth">Incorrect Username</p>
          <form v-on:submit.prevent="login">
          <div class="field">
          <label>Username</label>
            <div class="form-group">
              <input
                type="text"
                name="username"
                id="user"
                v-model="username"
                class="input"
              />
            </div>
            </div>
            <div class="field">
            <label>Password</label>
            <div class="form-group">
              
              <input
                type="password"
                name="password"
                id="pass"
                v-model="password"
                class="input"
              />
            </div>
            </div>
            <div class="field">
            <div class="form-group">
              <button type="submit" class="btn btn-lg btn-primarybtn-block">
                Login
              </button>
            </div>
          </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  data() {
    return {
      username: "",
      password: "",
      type: "CUSTOMER",
      incorrectAuth: false,
    };
  },
  computed: {
    ...mapGetters("auth", {
      loginState: "getLoginState",
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

    async login() {
      console.log(this.username, this.password);

      let config = {
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "http://localhost:8000/",
        },
      };

      const payload = {
        username: this.username,
        password: this.password,
        type: this.type,
      };
      await this.actionLogin(payload, config);
      if (this.loginState == "success") {
        this.$router.push({ name: "Home" });
      } else {
        this.incorrectAuth = true;
      }
    },
  },
};
</script>
