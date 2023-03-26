<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useApi } from "../resources/composables/useApi";
import { useRouter, useRoute } from 'vue-router';
const router = useRouter()

const { orderid, trailer, truck, labDetail, getTruck, getLabDetail } = useApi();

onMounted(() => {
  getLabDetail();
  getTruck()
});

const submitForm = async (value) => {
      const payload = {
        status: value.target.value,
        order: orderid.value,
      };
      console.log(payload);
      await axios.post(`/lab-results-create/`, payload).then((response) => {
        console.log(response.data);
      });
      router.push({
        name: 'LabVent',
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
        <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">Lab Vent Details</h2>
        <div>
          <p class="mt-2 text-center text-lg text-gray-600 max-w">Truck Reg: {{truck}}</p>
          <p class="mt-2 text-center text-lg text-gray-600 max-w">Trailer Reg: {{trailer}}</p>
        </div>
      </div>

      <div class="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
        <div class="bg-white py-8 px-6 shadow rounded-lg sm:px-10">
          <form class="mb-0 space-y-6" @submit.prevent="">
            
            <div>
              <label class="block text-sm font-medium text-gray-700">Oxygen</label>
              <div class="mt-1">
                <!-- <input id="password" name="password" type="password" autocomplete="current-password" required class="" /> -->
                <input class="w-full form-control valid bg-gray-200 px-2 pt-2 rounded " readonly="" type="text" v-model="labDetail.oxygen" />                
              </div>
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700">Pressure</label>
              <div class="mt-1">
                <input class="w-full form-control valid bg-gray-200 px-2 pt-2 rounded " readonly="" type="text" v-model="labDetail.pressure" />                
              </div>
            </div>


            <div>
              <label class="block text-sm font-medium text-gray-700">Nitrogen</label>
              <div class="mt-1">
                <input class="w-full form-control valid bg-gray-200 px-2 pt-2 rounded " readonly="" type="text" v-model="labDetail.nitrogen" />                
              </div>
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700">Methane</label>
              <div class="mt-1">
                <input class="w-full form-control valid bg-gray-200 px-2 pt-2 rounded " readonly="" type="text" v-model="labDetail.methane" />                
              </div>
            </div>
            
            <div>
              <button
                @click="submitForm"              
                type="submit"
                value="LOADING" 
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

            <div>
              <button
              @click="submitForm" 
                type="submit"
                value="REJECT" 
                class="w-full flex 
                    justify-center 
                    py-2 px-4 border 
                    border-transparent 
                    rounded-md shadow-sm 
                    text-sm font-medium 
                    text-white 
                    bg-red-600
                    hover:bg-indigo-700 
                    focus:outline-none 
                    focus:ring-2 
                    focus:ring-offset-2
                    focus:ring-indigo-500"                
                  >Reject
                </button>
            </div>

            <div>
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
            </div>

          </form>
        </div>
      </div>
    </div>
  <!-- Form -->
  
</template>
