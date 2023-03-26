<template>
  <div  class="flex items-center justify-center">
        

        <div>
          <div >      
          <h1 class="">BulkBalance</h1>
          <button
                class="w-full flex 
                    justify-center 
                    py-2 px-4 border 
                    mb-2
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
                  ><router-link :to="{ name: 'HomePage' }">New Order</router-link>
                </button>

        </div>
          <table class="border-collapse border-2 border-gray-500">
            <thead>
              <tr>
                <th class="border border-gray-400 px-4 py-2 text-gray-800">Order No</th>
                <th class="border border-gray-400 px-4 py-2 text-gray-800">Product</th>
                <th class="border border-gray-400 px-4 py-2 text-gray-800">Quantity</th>                
              </tr>
            </thead>
            <tbody>
              <tr v-for="order in this.orders" :key="order.id">
                <td class="border border-gray-400 px-4 py-2">{{ order.id }}</td>
                <td class="border border-gray-400 px-4 py-2">{{ order.product }}</td>
                <td class="border border-gray-400 px-4 py-2">{{ order.quantity }}</td>
                <!-- <td>{{ order.driver_details.name }}</td>
                <td>{{ order.order_quantity }}</td>
                <td>{{ order.status }}</td>
                <td>{{ order.trailer_details.registration }}</td>
                <td>{{ order.truck_details.registration }}</td> -->
              </tr>
            </tbody>
          </table>
        </div>
      </div>    
</template>

<script>
import axios from "axios";
export default {
  name: "BulkBalance",
  data() {
    return {
      orders: "",      
      query: "",
    };
  },
  mounted() {
    this.getOrders();
  },
  methods: {
    async getOrders() {
      // this.$store.commit('setIsLoading', true)
      this.showNextButton = false;
      this.showPreviousButton = false;

      let config = {
        headers: {
          Authorization: "Bearer " + localStorage.getItem("access_token"),
          "Content-Type": "application/json",
        },
      };

      await axios
        .get(`/bulk-order/`, config)
        .then((response) => {
          console.log(response.data);
          this.orders = response.data;
          console.log(Object.keys(this.orders));
          // this.num_orders = response.data.count;
        })
        .catch((error) => {
          console.log(error);
        });
      // this.$store.commit('setIsLoading', false)
    },
  },
};
</script>
