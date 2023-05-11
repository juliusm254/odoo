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

const truck_pressure = ref("");
const oxygen_content = ref("");
const methane_content = ref("");
const nitrogen_content = ref("")


const submitForm = async (value) => {
      const payload = {
        // status: value.target.value,
        order: orderid.value,
        truck: truck.value,
        trailer: trailer.value,
        truck_pressure: truck_pressure.value,
        oxygen_content: oxygen_content.value,
        methane_content: methane_content.value,
        nitrogen_content: nitrogen_content.value
      };
      console.log(payload);
      await axios.post(`/lab-create/`, payload).then((response) => {
        console.log(response.data);
      });
      router.push({
        name: 'LabInspection',
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
            <label class="block text-sm font-medium text-gray-700" >Oxygen content % Volume</label>
              <div class="mt-1 ">
                <input class="w-full form-control valid border-2 bg-white px-2 p-1 rounded " type="text" name="oxygen_content" required v-model="oxygen_content" />                
              </div>
            </div>


            <div>
              <label class="block text-sm font-medium text-gray-700">Pressure</label>
              <div class="mt-1 ">
                <input class="w-full form-control valid border-2 bg-white px-2 p-1 rounded " type="text" name="truck_pressure" v-model="truck_pressure" />                
              </div>
            </div>

            
            <div>
              <label class="block text-sm font-medium text-gray-700">Nitrogen</label>
              <div class="mt-1 ">
                <input class="w-full form-control valid border-2 bg-white px-2 p-1 rounded " type="text" name="truck_pressure" v-model="nitrogen_content" />                
              </div>
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700">Methane content % Volume</label>
              <div class="mt-1 ">
                <input class="w-full form-control valid border-2 bg-white px-2 p-1 rounded " type="text" name="truck_pressure" v-model="methane_content" />                
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
