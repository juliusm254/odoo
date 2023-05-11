<template>
  <div class="flex items-center justify-center">
       <!-- <h1 class="title">Leads</h1>

          <form @submit.prevent="getOrders">
            <div class="field has-addons">
              <div class="control">
                <input type="text" class="input" v-model="query" />
              </div>
              <div class="control">
                <button class="button is-success">Search</button>
              </div>
            </div>
          </form> -->

        <div>
          <h1 class="title">Orders</h1>

          <router-link :to="{ name: 'HomePage' }" class="button is-light mt-4"
            >Add Order</router-link
          >
        </div>

        <div>
          <table class="border-collapse border-2 border-gray-500">
            <thead>
              <tr>
                <th class="border border-gray-400 px-4 py-2 text-gray-800">Order No.</th>
                <th class="border border-gray-400 px-4 py-2 text-gray-800">Destination</th>
                <th class="border border-gray-400 px-4 py-2 text-gray-800">Driver</th>
                <th class="border border-gray-400 px-4 py-2 text-gray-800">Order Qty</th>
                <th class="border border-gray-400 px-4 py-2 text-gray-800">Trailer</th>
                <th class="border border-gray-400 px-4 py-2 text-gray-800">Truck</th>
                <th class="border border-gray-400 px-4 py-2 text-gray-800"> Status</th>
                <th class="border border-gray-400 px-4 py-2 text-gray-800">Created at</th>
                <th class="border border-gray-400 px-4 py-2 text-gray-800"> </th>
              </tr>
            </thead>

            <!-- <div>{{orders}}</div> -->

            <tbody>
              <tr v-for="order in this.orders" :key="order.id">
                <td class="border border-gray-400 px-4 py-2">{{ order.id }}</td>
                <td class="border border-gray-400 px-4 py-2">{{ order.destination }}</td>
                <td class="border border-gray-400 px-4 py-2">{{ order.driver_details.name }}</td>
                <td class="border border-gray-400 px-4 py-2">{{ order.order_quantity }}</td>
                <td class="border border-gray-400 px-4 py-2">{{ order.trailer_details.registration }}</td>
                <td class="border border-gray-400 px-4 py-2">{{ order.truck_details.registration }}</td>
                <td class="border border-gray-400 px-4 py-2">{{ order.order_status }}</td>
                <td class="border border-gray-400 px-4 py-2">{{ new Date(order.created_at).toLocaleString()}} </td>
              </tr>
            </tbody>

            <!-- <tbody>
              <tr v-for="order in orders">
                <td>{{ order.id }}</td>
                <td>{{ order.destination }}</td>
                <td>{{ order.order_quantity }}</td>
                <td>{{ order.status }}</td>
                <td>{{ order.truck }}</td>
                <td>{{ order.created_at }}</td>
                <td>
                  <router-link
                    :to="{ name: 'EditOrder', params: { id: order.id } }"
                    class="button is-light"
                    >Edit</router-link
                  >
                </td>
              </tr>
            </tbody> -->
          </table>

          <!-- <div class="buttons">
            <button
              class="button is-light"
              @click="goToPreviousPage()"
              v-if="showPreviousButton"
            >
              Prev
            </button>
            <button
              class="button is-light"
              @click="goToNextPage()"
              v-if="showNextButton"
            >
              Next
            </button>
          </div> -->
        </div>
      </div>
</template>

<script>
import axios from "axios";
export default {
  name: "About",
  data() {
    return {
      orders: "",
      showNextButton: false,
      showPreviousButton: false,
      currentPage: 1,
      query: "",
      // num_orders: 0,
    };
  },
  mounted() {
    this.getOrders();
  },
  methods: {
    // goToNextPage() {
    //   this.currentPage += 1;
    //   this.getOrders();
    // },
    // goToPreviousPage() {
    //   this.currentPage -= 1;
    //   this.getOrders();
    // },

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
        .get(`/order/`, config)
        .then((response) => {
          console.log(response.data);
          this.orders = response.data;
          console.log(Object.keys(this.orders));
          // this.num_orders = response.data.count;
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
</script>
