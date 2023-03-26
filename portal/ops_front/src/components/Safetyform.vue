<script>
import axios from "axios";
import useSafetyForm from "../resources/composables/trucks";
import { onMounted } from "vue";
import { useRouter, useRoute } from 'vue-router';

export default {
  setup() {
    const {
      truck,
      trailer,
      truckid,
      trailerid,
      orderid,
      questions,
      getTruck,
      getQuestions,
    } = useSafetyForm();

    onMounted(getTruck(), getQuestions());

    return {
      truckid,
      trailerid,
      orderid,
      truck,
      trailer,
      questions,
    };
  },
  methods: {
    async submitForm() {
      const payload = {
        order: this.orderid,
        questions: this.questions,
        truck: this.truckid,
        trailer: this.trailerid,
      };
      console.log(payload);
      await axios.post(`/checklistcreate/`, payload).then((response) => {
        console.log(response.data);
      });
      this.router.push({
        name: 'SafetyInspection',
        // query: {
        //   ...route.query,
        // },
      })
    },
    
  },
};
</script>

<template>  <div class="min-h-full bg-gray-100 flex flex-col justify-center py-5 px-6 lg:px-8">
  <div class="">
      <img class="mx-auto h-12 w-auto" src="https://tailwindui.com/img/logos/workflow-mark-indigo-600.svg" alt="Workflow" />
      <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">Lab Details</h2>
      <div>
        <p class="mt-2 text-center text-lg text-gray-600 max-w">Truck Reg: {{truck}}</p>
        <p class="mt-2 text-center text-lg text-gray-600 max-w">Trailer Reg: {{trailer}}</p>
      </div>
  </div>
<div class="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
    <div class="bg-white py-8 px-6 shadow rounded-lg sm:px-10">
      <form @submit.prevent="submitForm">
      <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">Safety Inspection</h2>

      <div v-for="question in questions" v-bind:key="question.id">
        <p>{{ question.question_desc }}</p>
        <div class="text-center font-extrabold text-gray-900">
          <input
          type="radio"
          :id="question.id"
          value="Yes"
          :name="question.id"
          v-model="question.value"
        />
        <label for="yes">Yes</label>
        <br />
        <input
          type="radio"
          :id="question.id"
          value="No"
          :name="question.id"
          v-model="question.value"
        />
        <label for="no">No</label>

        </div>

      </div>
      <div>
            <button                             
              type="submit"                
              class="w-full flex 
                  justify-center 
                  py-2 px-4 border 
                  border-transparent 
                  rounded-md shadow-sm 
                  text-sm font-medium 
                  text-white 
                  bg-green-600 
                  hover:bg-indigo-700 
                  focus:outline-none 
                  focus:ring-2 
                  focus:ring-offset-2
                  focus:ring-indigo-400"                
                >Submit
              </button>
          </div>

      <!-- <button type="submit">Submit</button> -->
      </form>

    </div>
</div>

</div>

</template>