<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useApi } from "../resources/composables/useApi";
import { useRouter, useRoute } from 'vue-router';
const router = useRouter()

const { orderid, trailer, truck, getTruck } = useApi();

onMounted(() => {
  getTruck()
});

const gross_weight = ref("");
const net_weight = ref("");
const tare_weight = ref("");

// order: this.orderid,
//         truck: this.truckid,
//         trailer: this.trailerid,
//         gross_weight: this.gross_weight,
//         net_weight: this.net_weight,
//         tare_weight: this.tare_weight,


const submitForm = async (value) => {
      const payload = {
        // status: value.target.value,
        order: orderid.value,
        truck: truck.value,
        trailer: trailer.value,
        gross_weight: gross_weight.value,
        net_weight: net_weight.value,
        tare_weight: tare_weight.value,

      };
      console.log(payload);
      await axios.post(`/loading/`, payload).then((response) => {
        console.log(response.data);
      });
      router.push({
        name: 'Loading',
        // query: {
        //   ...route.query,
        // },
      })
    };
</script>

<template>
  <!-- Form -->
  <div class="min-h-full bg-gray-100 flex flex-col justify-center py-5 px-6 lg:px-8">
      <div class="">
        <img class="mx-auto h-12 w-auto" src="https://tailwindui.com/img/logos/workflow-mark-indigo-600.svg" alt="Workflow" />
        <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">Lab Details</h2>
        <div>
          <p class="mt-2 text-center text-lg text-gray-600 max-w">Truck Reg: {{truck}}</p>
          <p class="mt-2 text-center text-lg text-gray-600 max-w">Trailer Reg: {{trailer}}</p>
        </div>
      </div>

      <div class="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
        <div class="bg-white py-8 px-6 shadow rounded-lg sm:px-10">
          <form class="mb-0 space-y-6" @submit.prevent="submitForm">  

            
            <div>
            <label class="block text-sm font-medium text-gray-700" >Gross Weight</label>
              <div class="mt-1 ">
                <input class="w-full form-control valid border-2 bg-white px-2 p-1 rounded " type="text" name="gross_weight" required v-model="gross_weight" />                
              </div>
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700">Tare Weight</label>
              <div class="mt-1 ">
                <input class="w-full form-control valid border-2 bg-white px-2 p-1 rounded " type="text" name="tare_weight" v-model="tare_weight" required />                
              </div>
            </div>

            
            <div>
              <label class="block text-sm font-medium text-gray-700">Net Weight</label>
              <div class="mt-1 ">
                <input class="w-full form-control valid border-2 bg-white px-2 p-1 rounded " type="text" name="net_weight" v-model="net_weight" required/>                
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
  <!-- Form -->


</template>


<!-- 
<script>
import axios from "axios";
import useSafetyForm from "../resources/composables/trucks";
import { onMounted } from "vue";

export default {
  setup() {
    const {
      gross_weight,
      net_weight,
      tare_weight,
      truck,
      trailer,
      truckid,
      trailerid,
      orderid,
      getTruck,
    } = useSafetyForm();

    onMounted(getTruck());

    return {
      truckid,
      trailerid,
      orderid,
      truck,
      trailer,
      gross_weight,
      net_weight,
      tare_weight,
    };
  },
  data() {
    return {
      // questions:[{question: '', value:''}]
    };
  },
  methods: {
    async submitForm() {
      const payload = {
        order: this.orderid,
        truck: this.truckid,
        trailer: this.trailerid,
        gross_weight: this.gross_weight,
        net_weight: this.net_weight,
        tare_weight: this.tare_weight,
      };
      console.log(payload);
      await axios.post("/loading/", payload).then((response) => {
        console.log(response.data);
      });
    },
  },
};
</script>

<template>
  <div>
    <h4>Truck Reg: {{ truck }}</h4>
    <h4>Trailer Reg: {{ trailer }}</h4>
  </div>
  <form @submit.prevent="submitForm">
    <h3>Post Loading Details</h3>

    <div class="field">
      <label>Gross Weight</label>
      <div class="control">
        <input
          type="number"
          name="gross_weight"
          class="input"
          v-model="gross_weight"
        />
      </div>
    </div>

    <div class="field">
      <label>Tare Weight</label>
      <div class="control">
        <input
          type="number"
          name="tare_weight"
          class="input"
          v-model="tare_weight"
        />
      </div>
    </div>

    <div class="field">
      <label>Net Weight</label>
      <div class="control">
        <input
          type="number"
          name="net_weight"
          class="input"
          v-model="net_weight"
        />
      </div>
    </div>
    <button type="submit">Submit</button>
  </form>
</template> -->
