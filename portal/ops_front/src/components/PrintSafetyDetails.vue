<script>
import useSafetyInspectionForm from "../resources/composables/checklistpdf";
import { onMounted } from "vue";
export default {
  setup() {
    const { getInspectionPrintout } = useSafetyInspectionForm();

    onMounted(getInspectionPrintout());
    return {};
  },
};
</script>

<template>
  <div></div>
</template>
