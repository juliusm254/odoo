<template>
  <nav>
    <!-- Desktop -->
    <div class="bg-indigo-600">
      <div class="max-w-7xl mx-auto">
        <div class="w-full mt-2 lg:inline-flex lg:w-auto lg:mt-0">
          <!-- Menu -->
          <div class="hidden md:flex flex-row w-full space-y-2  lg:w-auto lg:flex-row lg:space-y-0 lg:space-x-2">
            <!-- Logo -->
            <a href="" class="flex items-center space-x-2 py-5 px-2">
                <svg 
                xmlns="http://www.w3.org/2000/svg" 
                fill="none" 
                viewBox="0 0 24 24" 
                stroke-width="1.5" 
                stroke="currentColor" 
                class="w-8 h-8 text-white">
                <path 
                stroke-linecap="round" 
                stroke-linejoin="round" 
                d="M7.5 7.5h-.75A2.25 2.25 0 004.5 9.75v7.5a2.25 2.25 0 002.25 2.25h7.5a2.25 2.25 0 002.25-2.25v-7.5a2.25 2.25 0 00-2.25-2.25h-.75m0-3l-3-3m0 0l-3 3m3-3v11.25m6-2.25h.75a2.25 2.25 0 012.25 2.25v7.5a2.25 2.25 0 01-2.25 2.25h-7.5a2.25 2.25 0 01-2.25-2.25v-.75" 
                /></svg>              
              <span class="text-2xl font-extrabold text-white"
              >AGOL</span>
              </a>
            <!-- Menu -->
            <div class="relative">
              <a href="/" class="py-5 px-2 text-indigo-200 hover:text-indigo-400">Home</a>
              <a href="/orderscan" class="py-5 px-2 text-indigo-200 hover:text-indigo-400">Scan Order</a>
              <!-- <a href="/print-safety" class="py-5 px-2 text-indigo-200 hover:text-indigo-400">Safety</a> -->

              <!-- Safety Dropdown -->

              <!-- <div class="navbar-right  relative"> -->
              <button class="py-5 px-2 text-indigo-200 hover:text-indigo-400" @click="dropdownOpenSafety= !dropdownOpenSafety">
                Safety <i class="fa fas fa-sort-down"></i>
              </button>
              <button v-if="dropdownOpenSafety" @click="dropdownOpenSafety = false" tabindex="-1" class="fixed top-0 inset-0 h-full w-full bg-black opacity-0 cursor-default"></button>
              <div v-if="dropdownOpenSafety" class="right-0 p-2 mt-1 bg-white rounded-md shadow lg:absolute">
                  <a href="" class="text-sm text-gray-900 hover:bg-blue-600 hover:text-white block px-4 py-2 cursor-pointer">Account Settings</a>
                  <a href="" class="text-sm text-gray-900 hover:bg-blue-600 hover:text-white block px-4 py-2 cursor-pointer">Support</a>
                  <a class="text-sm text-gray-900 hover:bg-blue-600 hover:text-white block px-4 py-2 cursor-pointer">Sign Out</a>
              </div>
              <!-- </div> -->
              <!-- Safety Dropdown -->

              <!-- Lab Dropdown -->

              <!-- <div class="navbar-right  relative"> -->
              <button class="py-5 px-2 text-indigo-200 hover:text-indigo-400" @click="dropdownOpenLab = !dropdownOpenLab">
                Lab <i class="fa fas fa-sort-down"></i>
              </button>
              <button v-if="dropdownOpenLab" @click="dropdownOpenLab = false" tabindex="-1" class="group fixed top-0 inset-0 h-full w-full bg-black opacity-0 cursor-default"></button>
              <div v-if="dropdownOpenLab" class="group-hover:display block  right-0 p-2 mt-1 bg-white rounded-md shadow lg:absolute">
                  <a href="" class="text-sm text-gray-900 hover:bg-blue-600 hover:text-white block px-4 py-2 cursor-pointer">Account Settings</a>
                  <a href="" class="text-sm text-gray-900 hover:bg-blue-600 hover:text-white block px-4 py-2 cursor-pointer">Support</a>
                  <a class="text-sm text-gray-900 hover:bg-blue-600 hover:text-white block px-4 py-2 cursor-pointer">Sign Out</a>
              </div>
              <!-- </div> -->
                <!-- Lab Dropdown -->
              <!-- <a href="/" class="py-5 px-2 text-indigo-200 hover:text-indigo-400">Lab</a> -->
              <a href="/" class="py-5 px-2 text-indigo-200 hover:text-indigo-400">Loading</a>
              <!-- <a href="/" class="py-5 px-2 text-indigo-200 hover:text-indigo-400">Settings</a>
              <a href="/" class="py-5 px-2 text-indigo-200 hover:text-indigo-400">Settings</a>
              <a href="/" class="py-5 px-2 text-indigo-200 hover:text-indigo-400">Settings</a>
              <a href="/" class="py-5 px-2 text-indigo-200 hover:text-indigo-400">Settings</a> -->
            </div>
          </div>
          <!-- Login -->
          <div class="hidden md:flex flex-col w-full space-y-2  lg:w-auto lg:flex-row lg:space-y-0 lg:space-x-2">
            <a href="/" class="py-5 px-2 text-indigo-200 hover:text-indigo-400">Login</a>
              
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
        </div>

      </div>

    </div>
    <!-- Mobile Menu -->
    <div class="md:hidden bg-indigo-600" v-show="showMobileMenu">
      <a href="/" class="block py-2 px-4 hover:bg-indigo-700 hover:text-indigo-400">Settings</a>
      <a href="/" class="block py-2 px-4 hover:bg-indigo-700 hover:text-indigo-400">Safety</a>
      <a href="/" class="block py-2 px-4 hover:bg-indigo-700 hover:text-indigo-400">Lab</a>
      <a href="/" class="block py-2 px-4 hover:bg-indigo-700 hover:text-indigo-400">Loadings</a>
    </div>
  </nav>
</template>

<script setup>
import {ref} from "vue";

const showMobileMenu = ref(false)
const dropdownOpenSafety = ref(false)
const dropdownOpenLab = ref(false)

</script>

<style>

</style>

<!-- <router-link to="/orderscan">Scan Order</router-link> |
    <router-link to="/">Home</router-link> |
    <router-link to="/safety-inspection">Safety Inspection</router-link> |
    <router-link to="/lab-inspection">LabInspection</router-link> |
    <router-link to="/lab-results">Lab Results</router-link> |
    <router-link to="/lab-vent">Lab Vent</router-link> |
    <router-link to="/loading">Loading</router-link> |
    
    <router-link to="/about">About</router-link> |
    
    <router-link to="/login">Login</router-link> | -->