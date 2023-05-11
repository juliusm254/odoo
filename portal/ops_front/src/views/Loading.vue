<script setup>
import { onMounted } from 'vue'
import { useApi } from "../resources/composables/useApi";

const { loadingList, getLoadingList } = useApi();

onMounted(() => {
  //script
  getLoadingList()
})

</script>



<template>
  <div class="min-h-full bg-gray-100 flex flex-col justify-center py-5 px-6 lg:px-8">
        <img class="mx-auto h-12 w-auto" src="https://tailwindui.com/img/logos/workflow-mark-indigo-600.svg" alt="Workflow" />
        <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">Loading List</h2>
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
          <tr v-for="order in loadingList" v-bind:key="order.id">
            <td class="border border-gray-400 px-4 py-2">{{ order.id }}</td>
            <td class="border border-gray-400 px-4 py-2">{{ order.truck_details["registration"] }}</td>
            <td class="border border-gray-400 px-4 py-2">{{ order.truck_details["transporter"]  }}</td>
            <td class="border border-gray-400 px-4 py-2">{{ order.trailer_details["registration"] }}</td>
            <td class="border border-gray-400 px-4 py-2">
              <router-link
                      :to="`/loading/${order.id}`"
                      class="button is-light"
                      >Edit</router-link>
              </td>
            <!-- <td class="border border-gray-400 px-4 py-2">{{ order.id }}</td> -->
          </tr>            
        </tbody>
      </table>
    </div>
    <!-- Table -->
  </div> 
</template>
