<script setup>
import { useApi } from "../resources/composables/useApi";
import DriverDeleteModal from "./DriverDeleteModal.vue"
import { onMounted, ref } from 'vue'

const { driverList,getDriverList } = useApi();

const isOpen = ref(false)
const driver_name = ref("");
const driver_epra = ref("");
const driver_id_no = ref("");
const driver_id = ref("");


onMounted(() => {
  getDriverList()
})

const openModal = (driver) => {
      driver_id.value = driver.id;
      driver_name.value = driver.name;
      driver_epra.value = driver.driver_details.epra_no;
      driver_id_no.value = driver.driver_details.national_id
      isOpen.value = true;
    };



</script>




<template>
  <DriverDeleteModal 
  class="absolute"  
    :driver_id="driver_id"  
    :driver_name="driver_name"
    :driver_epra="driver_epra"
    :driver_id_no="driver_id_no"    
    :open="isOpen" 
    @close="isOpen = !isOpen"
    @closeDelete="getDriverList"
    /> 
  <div class="">
    <h1 class="">Driver List</h1>
  </div>

  <!-- Table -->
  <div class="flex items-center justify-center">
    <table class="border-collapse border-2 border-gray-500">
      <thead>
        <tr>
          <th class="border border-gray-400 px-4 py-2 text-gray-800">ID</th>
          <th class="border border-gray-400 px-4 py-2 text-gray-800">Name</th>
          <th class="border border-gray-400 px-4 py-2 text-gray-800">EPRA No.</th>
          <th class="border border-gray-400 px-4 py-2 text-gray-800">ID No.</th>
          <th class="border border-gray-400 px-4 py-2 text-gray-800"></th>
          <!-- <th class="border border-gray-400 px-4 py-2 text-gray-800">Order No.</th>
          <th class="border border-gray-400 px-4 py-2 text-gray-800">Truck</th> -->
        </tr>
      </thead>
      <tbody>
        <tr v-for="driver in driverList" v-bind:key="driver.driver">
          <td class="border border-gray-400 px-4 py-2">{{ driver.id }}</td>
          <td class="border border-gray-400 px-4 py-2">{{ driver.name }}</td>
          <td class="border border-gray-400 px-4 py-2">{{ driver.driver_details.epra_no }}</td>
          <td class="border border-gray-400 px-4 py-2">{{ driver.driver_details.national_id }}</td>
          <!-- <td class="border border-gray-400 px-4 py-2"> -->
            <!-- <button
                @click="isOpen = true"
                :to="`/`"
                class="w-full flex 
                    justify-center 
                    py-2 px-4 border 
                    border-transparent 
                    shadow-sm 
                    text-sm font-medium 
                    text-white 
                    bg-red-600 
                    hover:bg-indigo-700   
                    focus:outline-none 
                    focus:ring-2 
                    focus:ring-offset-2
                    focus:ring-indigo-400"         
                >Delete</button> -->
                <button
                @click="openModal(driver)"
                :to="`/`"
                class="w-full flex 
                    justify-center 
                    py-2 px-4 border 
                    border-transparent 
                    shadow-sm 
                    text-sm font-medium 
                    text-white 
                    bg-red-600 
                    hover:bg-indigo-700   
                    focus:outline-none 
                    focus:ring-2 
                    focus:ring-offset-2
                    focus:ring-indigo-400"         
                >Delete</button>
            <!-- </td> -->
          <!-- <td class="border border-gray-400 px-4 py-2">{{ order.id }}</td> -->
        </tr>            
      </tbody>
    </table>
  </div>
  <!-- Table -->
</template>