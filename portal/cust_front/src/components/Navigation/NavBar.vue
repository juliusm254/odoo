<template>
  <nav>
    <div class="bg-indigo-600">
      <div class="max-w-7xl mx-auto">
        <div class="w-full mt-2 lg:inline-flex lg:w-auto lg:mt-0">
          <!-- <h1 class="text-lg font-md">Website logo</h1> -->
            <div class="hidden md:flex flex-row w-full space-y-2  lg:w-auto lg:flex-row lg:space-y-0 lg:space-x-2">     
              
              <!-- Logo -->
              <a href="" class="flex items-center space-x-2 py-4 px-2">
                  <svg 
                  xmlns="http://www.w3.org/2000/svg" 
                  fill="none" 
                  viewBox="0 0 24 24" 
                  stroke-width="1.5" 
                  stroke="currentColor" 
                  class="w-8 h-9 text-white">
                  <path 
                  stroke-linecap="round" 
                  stroke-linejoin="round" 
                  d="M7.5 7.5h-.75A2.25 2.25 0 004.5 9.75v7.5a2.25 2.25 0 002.25 2.25h7.5a2.25 2.25 0 002.25-2.25v-7.5a2.25 2.25 0 00-2.25-2.25h-.75m0-3l-3-3m0 0l-3 3m3-3v11.25m6-2.25h.75a2.25 2.25 0 012.25 2.25v7.5a2.25 2.25 0 01-2.25 2.25h-7.5a2.25 2.25 0 01-2.25-2.25v-.75" 
                  /></svg>              
                <span class="text-2xl font-extrabold text-white"
                >Oil & Gas</span>
              </a>
              
              <!-- Logo -->
              
              <!-- Menu Links -->
              <div class="flex items-center py-5 px-2">
              <router-link :to="`/orders`" class="text-white text-lg hover:text-indigo-400 font-semibold py-5 px-4 rounded inline-flex items-center">Orders</router-link>
                <router-link :to="`/bulk-balance`" class="text-white text-lg hover:text-indigo-400 font-semibold py-5 px-4 rounded inline-flex items-center">Bulk Balance</router-link>
                <!-- <a href="/orderscan" class="text-white text-lg hover:text-indigo-400 font-semibold py-5 px-4 rounded inline-flex items-center">Scan Order</a> -->
              </div>
              
              <!-- Menu Links -->
              
              <!-- Drivers Dropdown -->

              <div class="flex items-center py-5 px-2">
                <div class="group inline-block relative">
                  <button
                    class=" text-white text-lg hover:text-indigo-400 font-semibold rounded px-2 inline-flex items-center"
                  >
                    <span class="mr-1">Drivers</span>
                    <svg
                      class="fill-current h-4 w-4 mr-2"
                      xmlns="http://www.w3.org/2000/svg"
                      viewBox="0 0 20 20"
                    >
                      <path
                        d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"
                      />
                    </svg>
                  </button>
                  <ul class="absolute hidden rounded-t font-semibold drop-shadow-xl bg-white text-gray-700 pt-0 group-hover:block">
                    <li class="">
                      <router-link
                        class="rounded-t  hover:bg-indigo-400 hover:text-white py-2 px-4 block whitespace-pre"
                        :to="`/add-driver`"
                        >Add Driver</router-link>
                    </li>
                    <li class="">                      
                      <router-link
                      :to="`/drivers`"
                      class= "rounded-b hover:text-white hover:bg-indigo-400 py-2 px-4 block whitespace-pre"
                      >Driver List
                      </router-link>
                    </li>
                  </ul>
                </div>
              </div>

              <!-- Driver Dropdown -->

              <!-- Trucks Dropdown -->

              <div class="flex items-center py-5 px-2">
                <div class="group inline-block relative">
                  <button
                    class=" text-white text-lg hover:text-indigo-400 font-semibold rounded px-2 inline-flex items-center"
                  >
                    <span class="mr-1">Trucks</span>
                    <svg
                      class="fill-current h-4 w-4 mr-2"
                      xmlns="http://www.w3.org/2000/svg"
                      viewBox="0 0 20 20"
                    >
                      <path
                        d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"
                      />
                    </svg>
                  </button>
                  <ul class="absolute hidden rounded-t font-semibold drop-shadow-xl bg-white text-gray-700 pt-0 group-hover:block">
                    <li class="">
                      <router-link
                        class="rounded-t  hover:bg-indigo-400 hover:text-white py-2 px-4 block whitespace-pre"
                        :to="`/add-truck`"
                        >Add Truck</router-link>
                    </li>
                    <li class="">                      
                      <router-link
                      :to="`/drivers`"
                      class= "rounded-b hover:text-white hover:bg-indigo-400 py-2 px-4 block whitespace-pre"
                      >Truck List
                      </router-link>
                    </li>
                  </ul>
                </div>
              </div>

              <!-- Driver Dropdown -->
              

              <div class="flex items-center py-5 px-2">
                <router-link :to="`/orders`" class="text-white text-lg hover:text-indigo-400 font-semibold py-5 px-4 rounded inline-flex items-center">Orders</router-link>
                <router-link :to="`/login`" class="text-white text-lg hover:text-indigo-400 font-semibold py-5 px-4 rounded inline-flex items-center">Login</router-link>
                <!-- <a href="/orderscan" class="text-white text-lg hover:text-indigo-400 font-semibold py-5 px-4 rounded inline-flex items-center">Scan Order</a> -->
              </div>
              
                              
            </div>
        </div>

        <!-- Button Show Mobile menu -->
        <div class="md:hidden flex items-center">        
            <button @click="showMobileMenu = !showMobileMenu" class="py-5 px-2">
              <svg xmlns="http://www.w3.org/2000/svg" 
              fill="none" 
              viewBox="0 0 24 24" 
              stroke-width="1.5" 
              stroke="currentColor" 
              class="w-8 h-8 text-white">
                <path 
                stroke-linecap="round" 
                stroke-linejoin="round" 
                d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
              </svg>

            </button>
          </div> 
                <!-- Button Show Mobile menu -->
      
          <!-- <section class="h-full flex justify-items-center">
            <p class="m-auto">This is some placeholder content</p>
          </section> -->
          <!-- Mobile Menu -->
          <div class="md:hidden bg-indigo-600" v-show="showMobileMenu">
            <a href="/" class="block py-2 px-4 hover:bg-indigo-700 hover:text-indigo-400">Settings</a>
            <a href="/" class="block py-2 px-4 hover:bg-indigo-700 hover:text-indigo-400">Safety</a>
            <a href="/" class="block py-2 px-4 hover:bg-indigo-700 hover:text-indigo-400">Lab</a>
            <a href="/" class="block py-2 px-4 hover:bg-indigo-700 hover:text-indigo-400">Loadings</a>
          </div>
          <!-- End of mobile -->
      </div>
    </div>
  </nav>
</template>

<script setup>
import {ref} from "vue";

const showMobileMenu = ref(false)
const dropdownOpenSafety = ref(false)
const dropdownOpenLab = ref(false)

</script>
