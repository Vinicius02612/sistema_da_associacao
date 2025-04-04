<template>
  {{ formattedDate }}
</template>
  
<script>
  import moment from 'moment';
  
  export default {
    props: {
      date: {
        type: Date,
        required: true
      }
    },
    computed: {
      formattedDate() {
        return moment(this.date).format('DD/MM/YYYY [às] HH:mm');
      }
    }
  };
  </script>
  