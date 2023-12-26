<template>
  <header class="border-b-2 border-gray-200 py-5 flex justify-between items-end px-4">
    <a
      href="https://pypi.org/project/django-fullstack/"
      target="_blank"
      rel="noopener"
      class="font-bold mb-2 sm:mb-0 text-l sm:text-3xl text-red-700"
    >
      django-fullstack
    </a>
    <p class="text-sm sm:text-xl">
      version {{ version }}
      <a
        href="https://github.com/RajaSunrise/django-fullstack"
        target="_blank"
        rel="noopener"
        class="text-blue-500 hover:underline"
      >
        release notes
      </a>
    </p>
  </header>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  props: {
    version: {
      type: String,
      required: true,
    },
  },
});
</script>
