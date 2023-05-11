<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useApi } from "../resources/composables/useApi";
import { useAttrs } from 'vue'

const props = defineProps(['truck', 'trailer', 'open','transporter', 'driver_name', 'driver_epra', 'driver_id_no' , 'orderno'])
// const orderid = ref()
// onMounted(() => { 
//     console.log(orderid);
// });

const attrs = useAttrs()
console.log(attrs)



const submitForm = async (value) => {
    const orderid = attrs.orderid
    const payload = {
        order_status: value.target.value,
        
      };
      console.log(payload);
      await axios.put(`/scan-order/${orderid}/`, payload).then((response) => {
        console.log(response.data);
      });
    };
   
</script>

<template>
  
        <div class="h-screen w-full flex flex-col items-center justify-center font-sans" v-show="open">
            <div class="absolute bg-black opacity-70 inset-0 z-0"></div>
        <div class="w-full max-w-lg p-3 relative  bg-white opacity-100   justify-center"> 
        <div>
            <p class="mt-2 text-center text-lg text-gray-600 max-w">Order No.: {{orderno}}</p>
          <p class="mt-2 text-center text-lg text-gray-600 max-w">Truck Reg: {{truck}}</p>
          <p class="mt-2 text-center text-lg text-gray-600 max-w">Trailer Reg: {{trailer}}</p>
          <p class="mt-2 text-center text-lg text-gray-600 max-w">Transporter: {{transporter}}</p>
          <p class="mt-2 text-center text-lg text-gray-600 max-w">Driver Name: {{driver_name}}</p>
          <p class="mt-2 text-center text-lg text-gray-600 max-w">EPRA Driver: {{driver_epra}}</p>
          <p class="mt-2 text-center text-lg text-gray-600 max-w">Driver ID: {{driver_id_no}}</p>
          <!-- <p class="mt-2 text-center text-lg text-gray-600 max-w">Trailer Reg: {{trailer}}</p> -->
        </div>
            <div class="">
               <div>
              <button
              type="button"
                @click="$emit('close')"
                class="w-full flex 
                    justify-center 
                    py-2 px-4 border 
                    mb-6
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
                  >Close
                </button>
            </div>            
               
            <div>
              <button
              value="SAFETY"
               @click="submitForm"
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
                  >Scan
                </button>
            </div>
            </div>
        </div>
    
</div>
    
</template>
