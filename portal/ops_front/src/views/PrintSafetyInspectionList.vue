<script setup>
import { onMounted } from 'vue'
import { useApi } from "../resources/composables/useApi";

const { safetyList, getPrintSafetyList } = useApi();

onMounted(() => {
  //script
  getPrintSafetyList()
})

</script>



<template>
   <div class="">
    <div class="">
      <div class="">
        <h1 class="title">Print Safety Inspection List</h1>
      </div> 

      <!-- <div class="flex items-center justify-center h-screen w-screen">
        <table class="border-collapse border-2 border-gray-500">
          <thead>
            <tr>
              <th class="border border-gray-400 px-4 py-2 text-gray-800">State</th>
              <th class="border border-gray-400 px-4 py-2 text-gray-800">City</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="border border-gray-400 px-4 py-2">Indiana</td>
              <td class="border border-gray-400 px-4 py-2">Indianapolis</td>
            </tr>
            <tr>
              <td class="border border-gray-400 px-4 py-2">Ohio</td>
              <td class="border border-gray-400 px-4 py-2">Columbus</td>
            </tr>
            <tr>
              <td class="border border-gray-400 px-4 py-2">Michigan</td>
              <td class="border border-gray-400 px-4 py-2">Detroit</td>
            </tr>
          </tbody>
        </table>
      </div> -->

      <div class="flex items-center justify-center">
        <table class="border-collapse border-2 border-gray-500">
          <thead>
            <tr>
              <th class="border border-gray-400 px-4 py-2 text-gray-800">Order No.</th>
              <th class="border border-gray-400 px-4 py-2 text-gray-800">Truck</th>
              <th class="border border-gray-400 px-4 py-2 text-gray-800">Transporter</th>
              <th class="border border-gray-400 px-4 py-2 text-gray-800">Trailer</th>
              <!-- <th class="border border-gray-400 px-4 py-2 text-gray-800">Order No.</th>
              <th class="border border-gray-400 px-4 py-2 text-gray-800">Truck</th> -->
            </tr>
          </thead>
          <tbody>
            <tr v-for="order in safetyList" v-bind:key="order.id">
              <td class="border border-gray-400 px-4 py-2">{{ order.id }}</td>
              <td class="border border-gray-400 px-4 py-2">{{ order.truck_details["registration"] }}</td>
              <td class="border border-gray-400 px-4 py-2">{{ order.truck_details["transporter"]  }}</td>
              <td class="border border-gray-400 px-4 py-2">{{ order.trailer_details["registration"] }}</td>
              <td class="border border-gray-400 px-4 py-2">
                <router-link
                    :to="`/print-safety/${order.id}`"
                    class="button is-light"
                    >Print</router-link>
                </td>
              <!-- <td class="border border-gray-400 px-4 py-2">{{ order.id }}</td> -->
            </tr>            
          </tbody>
        </table>
      </div>

      <!-- <div class="column is-12">
        <table class="table is-fullwidth">
          <thead>
            <tr>
              <th>ID</th>
              <th>Truck</th>
              <th>Transporter</th>
              <th>Trailer</th>
              <th>Transporter</th>

              <th></th>
            </tr>
          </thead>

          <tbody>
            <tr v-for="order in safetyList" v-bind:key="order.id">
              <td>{{ order.id }}</td>
              <td>{{ order.truck_details["registration"] }}</td>
              <td>{{ order.truck_details["transporter"] }}</td>
              <td>{{ order.trailer_details["registration"] }}</td>
              <td>{{ order.trailer_details["transporter"] }}</td>

              <td>        
                 

                  <router-link
                    :to="`/print-safety/${order.id}`"
                    class="button is-light"
                    >Print</router-link
                  >
                  
              </td>
            </tr>
          </tbody>
        </table>
      </div> -->
    </div>
  </div>
</template>