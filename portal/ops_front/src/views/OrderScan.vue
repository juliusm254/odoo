<script setup>
import OrderScanModal from "./OrderScanDetails.vue"
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useApi } from "../resources/composables/useApi";

const { } = useApi();

// onMounted(() => {
//   getLabDetail();
//   getTruck()
// });

const orderno = ref("");
const isOpen = ref(false)
const truck = ref("");
const trailer = ref("");
const transporter = ref("");
const driver_name = ref("");
const driver_epra = ref("");
const driver_id_no = ref("");

const submitForm = async (value) => {
      const payload = {
        order_status: "SAFETY",
        
      };
      console.log(payload);
      await axios.get(`/order/${orderno.value}/`).then((response) => {
        console.log(response.data);
        truck.value = response.data.truck_details.registration;
        transporter.value = response.data.trailer_details.transporter;  
        trailer.value = response.data.trailer_details.registration;
        driver_name.value = response.data.driver_details.name;
        driver_epra.value = response.data.driver_details.epra_no;
        driver_id_no.value = response.data.driver_details.national_id;        
        
      })  
    };
</script>

Modal to confirm truck details before accepting truck



<template>
  <OrderScanModal 
  class="absolute "
    :trailer="trailer"
    :transporter="transporter"
    :driver_name="driver_name"
    :driver_epra="driver_epra"
    :driver_id_no="driver_id_no"
    :orderno="orderno"
    :truck="truck"
    :open="isOpen" 
    :orderid="orderno" 
    @close="isOpen = !isOpen"
    />
    <!-- Form -->
    <div class="min-h-full bg-gray-100 flex flex-col justify-center py-5 px-6 lg:px-8">
      <div class="">
        <img class="mx-auto h-12 w-auto" src="https://tailwindui.com/img/logos/workflow-mark-indigo-600.svg" alt="Workflow" />
        <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">Scan Order</h2>
        <!-- <div>
          <p class="mt-2 text-center text-lg text-gray-600 max-w">Truck Reg: {{truck}}</p>
          <p class="mt-2 text-center text-lg text-gray-600 max-w">Trailer Reg: {{trailer}}</p>
        </div> -->
      </div>

      <div class="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
        <div class="bg-white py-8 px-6 shadow rounded-lg sm:px-10">
          <form class="mb-0 space-y-6" @submit.prevent="submitForm(orderno)">
            <div>
            <label class="block text-sm font-medium text-gray-700" >Order No.</label>
              <div class="mt-1 mb-6">
                <input class="w-full form-control valid border-2 bg-white px-2 p-1 rounded " type="text" name="order_id" required v-model="orderno" />                
              </div>
            </div>

            <div>
              <button
              type="submit"
               @click="isOpen = true"
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
                    focus:ring-indigo-500"                
                  >Scan
                </button>
            </div>
            

            <!-- <div>
              <button
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
                    focus:ring-indigo-500"                
                  ><router-link to="/lab-vent/">Back</router-link>
                </button>
            </div> -->

          </form>
        </div>
      </div>
    </div>
  <!-- Form -->
  
</template>


<!-- <template>
  <div class="">
    <div class="">
      <div class="">
        <h1 class="title">Scan Order</h1>
      </div>

      <div class="flex items-center justify-center">
        <form @submit.prevent="submitForm">
          <div class="field">
            <label>Order No.</label>
            <div class="control">
              <input
                type="text"
                name="company"
                class="input"
                v-model="order_no"
              />
            </div>
          </div>

          <div class="field">
            <div class="control">
              Step 4 — Creating Custom Events
When developing applications in Vue.js, there will be times when you need to pass 

data up to a parent component via a custom event. Props are read-only data that are 
passed down to a child from the parent, but a custom action via an $emit is the opposite of that. 
To create the most reusable components, it’s best to think of these as functions. 

You pass data down through props (arguments), and emit values back up to the parent 
(a return value).

To emit an event from the child component to the parent, you use the $emit function.
 Before implementing this, this tutorial will guide you through an example to
  demonstrate how this works.

The $emit function accepts two arguments: 
the action name (a string), and the value to pass up to the parent. 
In the following example, when the user clicks on the button, you are 
sending the value CVG to the parent component under the action favoriteAirport: 

                            <button @click="$emit('favoriteAirport', 'CVG')" class="button is-success">Submit</button>

              <button value="SAFETY" class="button is-success">Submit</button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template> -->
<!-- 
<script>
import axios from "axios";

// import { toast } from 'bulma-toast'

export default {
  name: "OrderScan",
  data() {
    return {
      status: "SAFETY",
      order_no: "",
      order: {},
    };
  },
  methods: {
    async submitForm() {
      const order_no = this.order_no;
      const statusdata = JSON.stringify({
        order_status: this.status,
      });
      console.log(this.status);
      await axios
        .put(`/scan-order/${order_no}/`, statusdata)
        .then((response) => {
          //  toast({
          //     message: 'The Lead is Added',
          //     type: 'is-success',
          //     dismissible: true,
          //     pauseOnHover: true,
          //     duration: 2000,
          //     position: 'bottom-right',
          // })
          console.log(response.data);
          // this.order = (response.data)
          // console.log(this.order)
          // this.$router.push('/dashboard/leads/')
        })
        .catch((error) => {
          console.log(error);
        });
      // this.$store.commit('setIsLoading', false)
    },
  },
};
</script> -->
