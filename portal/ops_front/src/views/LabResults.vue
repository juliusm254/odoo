<script setup>
import { onMounted } from 'vue'
import { useApi } from "../resources/composables/useApi";

const { labResultsList, getLabResultsList } = useApi();

onMounted(() => {
  //script
  getLabResultsList()
})



</script>




<template>  
  <div class="">
    <h1 class="">Lab Results</h1>
  </div>

  <!-- Table -->
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
        <tr v-for="order in labResultsList" v-bind:key="order.id">
          <td class="border border-gray-400 px-4 py-2">{{ order.id }}</td>
          <td class="border border-gray-400 px-4 py-2">{{ order.truck_details["registration"] }}</td>
          <td class="border border-gray-400 px-4 py-2">{{ order.truck_details["transporter"]  }}</td>
          <td class="border border-gray-400 px-4 py-2">{{ order.trailer_details["registration"] }}</td>
          <td class="border border-gray-400 px-4 py-2">
            <router-link
                :to="`/lab-results/${order.id}`"
                class="button is-light"
                >Edit</router-link>
            </td>
          <!-- <td class="border border-gray-400 px-4 py-2">{{ order.id }}</td> -->
        </tr>            
      </tbody>
    </table>
  </div>
  <!-- Table -->
</template>

