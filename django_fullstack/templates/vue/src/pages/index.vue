<template>
  <div>
    <DjangoHeader :version="version" />
    <DjangoMain :version="version" />
    <DjangoFooter :version="version" />
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import DjangoHeader from '../components/DjangoHeader.vue';
import DjangoMain from '../components/DjangoMain.vue';
import DjangoFooter from '../components/DjangoFooter.vue';

export default defineComponent({
  components: {
    DjangoHeader,
    DjangoMain,
    DjangoFooter,
  },
  data() {
    return {
      version: '0.4.0',
    };
  },
});
</script>
