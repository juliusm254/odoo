<template>

    <!-- Form -->
    <div class="min-h-full bg-gray-100 flex flex-col justify-center py-5 px-6 lg:px-8">
      <div class="">
        <img class="mx-auto h-12 w-auto" src="https://tailwindui.com/img/logos/workflow-mark-indigo-600.svg" alt="Workflow" />
        <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">Create New Order</h2>
       
      </div>

      <div class="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
        <div class="bg-white py-8 px-6 shadow rounded-lg sm:px-10">
          <form class="mb-0 space-y-6" @submit.prevent="">
            
            <div>
              <label class="block text-sm font-medium text-gray-700">Truck</label>
              <div class="mt-1">                
               <select v-model="truck" class="w-full bg-gray-200 px-2 pt-2 rounded "  >
                  <option  disabled value="selected">Select Truck</option>
                  <option class="dropdown"
                    v-for="truck in trucks"
                    v-bind:key="truck"
                    :value="truck.truck"
                  >
                    {{ truck.registration }}
                  </option>
                </select>
              
              </div>
            </div>
            

            <div>
              <label class="block text-sm font-medium text-gray-700">Trailer</label>
              <div class="mt-1">                
               <select v-model="trailer" class="w-full bg-gray-200 px-2 pt-2 rounded "  >
                  <option  disabled value="selected">Select Trailer</option>
                  <option class="dropdown"
                  v-for="trailer in trailers"
                  v-bind:key="trailer.id"
                  :value="trailer.trailer"
                >
                  {{ trailer.registration }}
                  </option>
                </select>
              
              </div>
            </div>


            <div>
              <label class="block text-sm font-medium text-gray-700">Driver</label>
              <div class="mt-1">                
               <select v-model="driver" class="w-full bg-gray-200 px-2 pt-2 rounded "  >
                  <option  disabled value="selected">Select Driver</option>
                  <option class="dropdown"
                  v-for="driver in drivers"
                  v-bind:key="driver.id"
                  :value="driver.id"
                >
                  {{ driver.name }}
                  </option>
                </select>
              
              </div>
            </div>


          <div class="field">
            <label>Quantity (KG)</label>
            <div class="control">
              <input type="text" class="w-full bg-gray-200 px-2 pt-2 rounded" v-model="order_quantity" />
            </div>
          </div>

          <div class="field">
            <label>Destination</label>
            <div class="control">
              <input type="text" class="w-full bg-gray-200 px-2 pt-2 rounded" v-model="destination" />
            </div>
          </div>

          <div class="field">
            <label>Reference</label>
            <div class="control">
              <input
                type="text"
                name="company"
                class="w-full bg-gray-200 px-2 pt-2 rounded"
                v-model="reference"
              />
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
                  >Proceed
                </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  <!-- Form -->

<!-- 
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">New Order</h1>
      </div>

      <div class="column is-12">
        <form @submit.prevent="submitForm">
          <div class="field">
            <label>Truck</label>
            <div class="control">
              <select v-model="truck">
                <option class="input" disabled value="selected">Select Truck</option>
                <option class="dropdown"
                  v-for="truck in trucks"
                  v-bind:key="truck"
                  :value="truck.truck"
                >
                  {{ truck.registration }}
                </option>
              </select>
              </div>
          </div>

          <div class="field">
            <label>Trailer</label>
            <div class="control">
              <select v-model="trailer">
                <option disabled value="selected">Select Trailer</option>
                <option class="dropdown"
                  v-for="trailer in trailers"
                  v-bind:key="trailer.id"
                  :value="trailer.trailer"
                >
                  {{ trailer.registration }}
                </option>
              </select>
            </div>
          </div>

          <div class="field">
            <label>Driver</label>
            <div class="control">
              <select v-model="driver">
                <option disabled value="selected">Select Driver</option>
                <option class="dropdown"
                  v-for="driver in drivers"
                  v-bind:key="driver.id"
                  :value="driver.driver.id"
                >
                  {{ driver.name }}
                </option>
              </select>
            </div>
          </div>

          <div class="field">
            <label>Quantity (KG)</label>
            <div class="control">
              <input type="text" class="input" v-model="order_quantity" />
            </div>
          </div>

          <div class="field">
            <label>Destination</label>
            <div class="control">
              <input type="text" class="input" v-model="destination" />
            </div>
          </div>

          <div class="field">
            <label>Reference</label>
            <div class="control">
              <input
                type="text"
                name="company"
                class="input"
                v-model="reference"
              />
            </div>
          </div>

          <div class="field">
            <div class="control">
              <button class="button">Submit</button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div> -->
</template>

<script>
import axios from "axios";

// import { toast } from 'bulma-toast'

export default {
  name: "Home",
  data() {
    return {
      trucks: [],
      trailers: [],
      drivers: [],
      driver: "",
      truck: "",
      order_quantity: "",
      trailer: "",
      destination: "",
      reference: "",
    };
  },
  mounted() {
    this.getTrucks();
    this.getDrivers();
    this.getTrailers();
  },

  methods: {
    async getTrucks() {
      let config = {
        headers: {
          Authorization: "Bearer " + localStorage.getItem("access_token"),
          "Content-Type": "application/json",
        },
      };
      // this.$store.commit('setIsLoading', true)
      this.showNextButton = false;
      this.showPreviousButton = false;

      await axios
        .get(`/customer-truck/`, config)
        .then((response) => {
          console.log(response.data);
          this.trucks = response.data;
          // this.num_orders = response.data.count
        })

        // await axios
        //     .get(`/api/v1/leads/?page=${this.currentPage}&search=${this.query}`)
        //     .then(response => {
        //         this.leads = response.data.results
        //         console.log(response.data)

        //     // for (let i = 0; i < response.data.length; i++) {
        //     //     this.leads.push(response.data[i])

        //         if (response.data.next) {
        //             this.showNextButton = true
        //         }
        //         if (response.data.previous) {
        //             this.showPreviousButton = true
        //         }
        // })

        .catch((error) => {
          console.log(error);
        });
      // this.$store.commit('setIsLoading', false)
    },
    async getTrailers() {
      let config = {
        headers: {
          Authorization: "Bearer " + localStorage.getItem("access_token"),
          "Content-Type": "application/json",
        },
      };
      // this.$store.commit('setIsLoading', true)
      this.showNextButton = false;
      this.showPreviousButton = false;

      await axios
        .get(`/customer-trailer/`, config)
        .then((response) => {
          console.log(response.data);
          this.trailers = response.data;
          // this.num_orders = response.data.count
        })

        // await axios
        //     .get(`/api/v1/leads/?page=${this.currentPage}&search=${this.query}`)
        //     .then(response => {
        //         this.leads = response.data.results
        //         console.log(response.data)

        //     // for (let i = 0; i < response.data.length; i++) {
        //     //     this.leads.push(response.data[i])

        //         if (response.data.next) {
        //             this.showNextButton = true
        //         }
        //         if (response.data.previous) {
        //             this.showPreviousButton = true
        //         }
        // })

        .catch((error) => {
          console.log(error);
        });
      // this.$store.commit('setIsLoading', false)
    },

    async getDrivers() {
      // this.$store.commit('setIsLoading', true)
      this.showNextButton = false;
      this.showPreviousButton = false;
      let config = {
        headers: {
          Authorization: "Bearer " + localStorage.getItem("access_token"),
          "Content-Type": "application/json",
        },
      };

      await axios
        .get(`/customer-driver/`, config)
        .then((response) => {
          console.log(response.data);
          this.drivers = response.data;
          // this.num_orders = response.data.count
        })

        // await axios
        //     .get(`/api/v1/leads/?page=${this.currentPage}&search=${this.query}`)
        //     .then(response => {
        //         this.leads = response.data.results
        //         console.log(response.data)

        //     // for (let i = 0; i < response.data.length; i++) {
        //     //     this.leads.push(response.data[i])

        //         if (response.data.next) {
        //             this.showNextButton = true
        //         }
        //         if (response.data.previous) {
        //             this.showPreviousButton = true
        //         }
        // })

        .catch((error) => {
          console.log(error);
        });
      // this.$store.commit('setIsLoading', false)
    },
    async submitForm() {
      // this.$store.commit('setIsLoading', true)
      console.log("Submit Form");
      console.log(this.truck);
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

      const order = {
        driver: this.driver,
        truck: this.truck,
        trailer: this.trailer,
        order_quantity: this.order_quantity,
        destination: this.destination,
        customer: localStorage.getItem("customer_id"),
      };
      console.log(order);
      await axios
        .post("/order/", order, config)
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

          this.$router.push("/");
        })
        .catch((error) => {
          console.log(error);
        });

      // this.$store.commit('setIsLoading', false)
    },
  },
};
</script>
