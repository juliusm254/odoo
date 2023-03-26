import { ref } from "vue";
import axios from "axios";
import { useRoute } from "vue-router";
import store from "../../store";

const safetyList = ref([]);
const safetyInspectionList = ref([]);
const labInspectionList = ref([]);
const labResultsList = ref([]);
const labResultsDetail = ref([]);
const labSealList = ref([]);
const labDetail = ref([]);
const labVentList = ref("");
const loadingList = ref([]);
const trailer = ref("");
const truck = ref("");




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


    const getPrintSafetyList = async () => {
        const response = await axios.get(`/printsafety/`);
        safetyList.value = response.data
    };

    const getSafetyInspectionList = async () => {
        const response = await axios.get(`/checklist/`);
        safetyInspectionList.value = response.data
    };

    const getLabInspectionList = async () => {
        const response = await axios.get(`/lab-inspection/`);
        labInspectionList.value = response.data

    };

    const getLabResultsList = async () => {
        const response = await axios.get(`/lab-results/`);
        labResultsList.value = response.data
    };
    // Repeated in labdeta
    const getLabResultsDetail = async () => {
        let response = await axios.get(`/lab-results/${orderid.value}`);
        console.log(response.data);
        labResultsDetail.value = response.data[0];
    };

    const getLabSealList = async () => {
        const response = await axios.get(`/lab-seal/`);
        labSealList.value = response.data
    };
    const getLabDetail = async () => {
        let response = await axios.get(`/lab-results/${orderid.value}`);
        console.log(response.data);
        labDetail.value = response.data[0];
    };

    const getLabVentList = async () => {
        const response = await axios.get(`/lab-vent/`)
        labVentList.value = response.data
    };
    const getLoadingList = async () => {
        const response = await axios.get(`/loading-list/`);
        loadingList.value = response.data
    };

    const getTruck = async () => {
        const response = await axios.get(`/order/${orderid.value}`);
        console.log(response.data);    
        truck.value = response.data.truck_details.registration;
        trailer.value = response.data.trailer_details.registration;    
    };
    
    
    // getSafetyList();
    // getLabResultsList();    
    return {safetyList,
            safetyInspectionList,
            labInspectionList,
            labResultsList,
            labResultsDetail,
            labSealList,
            labDetail,
            labVentList,
            loadingList,
            truck,
            trailer,
            orderid,
            getPrintSafetyList,
            getSafetyInspectionList,
            getLabInspectionList,
            getLabResultsList,
            getLabResultsDetail,
            getLabSealList,
            getLabDetail,
            getLabVentList,
            getLoadingList,
            getTruck
    };
};