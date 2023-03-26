
<template>
  <!-- Form -->
  <div class="min-h-full bg-gray-100 flex flex-col justify-center py-5 px-6 lg:px-8">
    <div class="">
      <img class="mx-auto h-12 w-auto" src="https://tailwindui.com/img/logos/workflow-mark-indigo-600.svg" alt="Workflow" />
      <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">Add Driver</h2>      
    </div>

    <div class="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
      <div class="bg-white py-8 px-6 shadow rounded-lg sm:px-10">
        <form class="mb-0 space-y-6" @submit.prevent="">
          
          <div>
            <label class="block text-sm font-medium text-gray-700" >Name</label>
              <div class="mt-1 ">
                <input class="w-full form-control valid border-2 bg-white px-2 p-1 rounded " type="text" name="name" v-model="name" required/>                
              </div>
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700" >ID</label>
              <div class="mt-1 ">
                <input class="w-full form-control valid border-2 bg-white px-2 p-1 rounded " type="text" name="id" v-model="id" required/>                
              </div>
          </div>
          
          <div>
            <button
              @click="submitForm"              
              type="submit"
              class="w-full flex 
                  justify-center 
                  py-2 px-4 border 
                  border-transparent 
                  rounded-md shadow-sm 
                  text-sm font-medium 
                  text-white 
                  bg-indigo-600 
                  hover:bg-indigo-700 
                  focus:outline-none 
                  focus:ring-2 
                  focus:ring-offset-2
                  focus:ring-indigo-500"                
                >submit
              </button>
          </div>       

         

        </form>
      </div>
    </div>
  </div>
<!-- Form -->

</template>

<!-- <template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Add Driver</h1>
      </div>

      <div class="column is-12">
        <form @submit.prevent="submitForm">
          <div class="field">
            <label>Name</label>
            <div class="control">
              <input type="text" name="name" class="input" v-model="name" />
            </div>
          </div>

          <div class="field">
            <label>ID</label>
            <div class="control">
              <input type="text" name="id" class="input" v-model="id" />
            </div>
          </div>

          <div class="field">
            <div class="control">
              <button class="button is-success">Submit</button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template> -->

<script>
import axios from "axios";
export default {
  name: "AddDriver",
  data() {
    return {
      id: "",
      name: "",
    };
  },
  methods: {
    async submitForm() {
      // this.$store.commit('setIsLoading', true)
      console.log("Submit Form");
      console.log(this.name);
      // let config = {
      //   headers: {
      //   "Authorization": localStorage.getItem('Token '+'access_token') ,
      //   }
      //   }
      //   console.log(config);

      let config = {
        headers: {
          Authorization: "Bearer " + localStorage.getItem("access_token"),
          "Content-Type": "application/json",
        },
      };

      const driver = {
        name: this.name,
        national_id: this.id,
        customer_id: localStorage.getItem("customer_id"),
      };
      console.log(driver);
      await axios
        .post("/customer-driver/", driver, config)
        .then((response) => {
          console.log(response.data);
          //  toast({
          //     message: 'The Lead is Added',
          //     type: 'is-success',
          //     dismissible: true,
          //     pauseOnHover: true,
          //     duration: 2000,
          //     position: 'bottom-right',
          // })

          // this.$router.push("/");
        })
        .catch((error) => {
          console.log(error);
        });

      // this.$store.commit('setIsLoading', false)
    },
  },
};
</script>
