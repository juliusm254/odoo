<template>
  <div>
    <div class="navbar-brand"></div>

    <div class="">
      <div class="">
        <router-link to="/Drivers" class="">Delete</router-link> |
        <!-- <router-link to="../Trucks" class="">Trucks</router-link> |
                <router-link to="../Trailers" class="">Trailers</router-link> -->

        <div class="navbar-item">
          <div class="buttons">
            <template v-if="!$store.state.auth.user_id">
              <router-link to="/sign-up" class="button is-success"
                ><strong>Sign Up</strong></router-link
              >
              |
              <router-link to="/log-in" class="button is-light"
                >Log In</router-link
              >
            </template>

            <template v-else>
              <router-link to="/dashboard/log-out" class="button is-info"
                >Log Out</router-link
              >
              |
              <router-link to="/dashboard/my-account" class="button is-info"
                >Account Details</router-link
              >
            </template>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Account",
};
</script>
