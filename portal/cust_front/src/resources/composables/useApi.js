import { ref } from "vue";
import axios from "axios";
import { useRoute } from "vue-router";
import store from "../../store";

const driverList = ref([]);
// const labInspectionList = ref([]);
// const labResultsList = ref([]);
// const labResultsDetail = ref([]);
// const labSealList = ref([]);
// const labDetail = ref([]);
// const labVentList = ref("");
// const loadingList = ref([]);
// const trailer = ref("");
// const truck = ref("");




export const useApi = () => {
    // const authData = store.getters["auth/getLoginStatus"].access_token;
    // const authData = localStorage.getItem("access_token");

    

    // const config = {
    //     headers: {
    //       "Authorization": `Bearer ${authData}`,
    //     },
    //   };

    //   console.log(config)



    const route = useRoute();
    const orderid = ref(route.params.id);


    const getDriverList = async () => {
        const response = await axios.get(`/customer-driver/`);
        driverList.value = response.data
    };
    
    
    // getSafetyList();
    // getLabResultsList();    
    return {driverList,
            getDriverList,
    };
};