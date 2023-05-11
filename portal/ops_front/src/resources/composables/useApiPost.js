export function useApiPost() {
    let payload = ref({
        order:"",
        truck:"",
        trailer:"",
        truck_pressure:"",
        oxygen_content:"",
        methane_content:"",
        name: "",
        email: "",
        phone: "",
        message: "",
    });
    // let loading = ref(false);
    // let successMessage = ref("");
    let errors = ref({});
  
    async function submitForm() {
    //   loading.value = true;
      await axios .post(`/lab-results/`, payload)
        .then(res => {
        //   successMessage.value = res.data.message;
          errors.value = {};
          payload.value = {};
        })
        .catch(err => {
          if (err.response.status === 422) {
            errors.value = err.response.data.errors;
          }
        })
        // .finally(() => loading.value = false)
    }
  
    function getError(key) {
      return errors.value[key] ? errors.value[key][0] : null;
    }
  
    return {
        payload,
    //   loading,
    //   successMessage,
      submitForm,
      getError,
    }
  }