<script setup>
import { onMounted } from 'vue'
import { useApi } from "../resources/composables/useApi";

const { safetyInspectionList, getSafetyInspectionList } = useApi();

onMounted(() => {
  //script
  getSafetyInspectionList()
})

</script>


<template>
  <div class="">
    <div class="">
      <div class="">
        <h1 class="title">Safety Inspection List</h1>
      </div>

      <!-- Table -->

      <div class="flex items-center justify-center">
        <table class="table-auto">
          <thead>
            <tr>
              <th class="border border-gray-400 px-4 py-2 text-gray-800">ID</th>
              <th class="border border-gray-400 px-4 py-2 text-gray-800">Truck</th>
              <th class="border border-gray-400 px-4 py-2 text-gray-800">Transporter</th>
              <th class="border border-gray-400 px-4 py-2 text-gray-800">Trailer</th>
              <th class="border border-gray-400 px-4 py-2 text-gray-800">Transporter</th>
              <th class="border border-gray-400 px-4 py-2 text-gray-800"></th>
            </tr>
          </thead>

          <tbody>
            <tr v-for="order in safetyInspectionList" v-bind:key="order.id">
              <td class="border border-gray-400 px-4 py-2 text-gray-800">{{ order.id }}</td>
              <td class="border border-gray-400 px-4 py-2 text-gray-800">{{ order.truck_details["registration"] }}</td>
              <td class="border border-gray-400 px-4 py-2 text-gray-800">{{ order.truck_details["transporter"] }}</td>
              <td class="border border-gray-400 px-4 py-2 text-gray-800">{{ order.trailer_details["registration"] }}</td>
              <td class="border border-gray-400 px-4 py-2 text-gray-800">{{ order.trailer_details["transporter"] }}</td>
              <td class="border border-gray-400 px-4 py-2 text-gray-800">              
                  <router-link class="btn-primary"
                    :to="`/safety-checklist/${order.id}`"
                    >Edit</router-link
                  >
              </td>
            </tr>
          </tbody>
        </table>
      </div>

       <!-- Table -->

    </div>
  </div>
</template>
<!-- 
<script setup>
import axios from "axios";






</script> -->

<!-- <script>
import axios from "axios";

// import { toast } from 'bulma-toast'

export default {
  name: "SafetyInspection",
  data() {
    return {
      orders: [],
      num_orders: "",
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

      await axios
        .get(`/checklist/`)
        .then((response) => {
          console.log(response.data);
          this.orders = response.data;
          // this.num_orders = response.data.count
          console.log(JSON.parse(JSON.stringify(response.data)));
        })

        // await axios
        //     .get(`/api/v1/leads/?page=${this.currentPage}&search=${this.query}`)
        //     .then(response => {
        //         this.leads = response.data.results
        //         console.log(response.data)

        //     // for (let i = 0; i < response.data.length; i++) {
        //     //     this.leads.push(response.data[i])

        //         if (response.data.next) {
        //             this.showNextButton = true
        //         }
        //         if (response.data.previous) {
        //             this.showPreviousButton = true
        //         }
        // })

        .catch((error) => {
          console.log(error);
        });
      // this.$store.commit('setIsLoading', false)
    },
  },
};
</script> -->
