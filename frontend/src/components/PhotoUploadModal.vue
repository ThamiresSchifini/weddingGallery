<script>
export default {
  name: 'PhotoUploadModalComponent',
  methods: {
    onUpload($event) {
      this.$emit('upload', $event, this.author, this.description, this.file);
    },
    close() {
      this.$emit('close');
    },
    handleFileUpload($event) {
      this.file = $event.target.files[0];
    }
  },
  data() {
    return {
      author: '',
      description: '',
      file: '',
    }
  }
};
</script>

<template>
  <transition name="modal-fade">
    <div class="modal-backdrop">
      <div class="modal w-75 h-50 mx-auto position-relative"
           role="dialog"
      >
        <header
            class="modal-header text-primary"
            id="modalTitle"
        >
          <h1>Upload your beautiful photo!</h1>
          <button
              type="button"
              class="btn-close"
              @click="close"
              aria-label="Close modal"
          >
            x
          </button>
        </header>

        <section
            class="modal-body"
            id="modalDescription"
        >

          <div class="input-group my-2">
            <input type="text" class="form-control" v-model="author" placeholder="Author">
          </div>

          <div class="input-group my-2">
            <input type="text" class="form-control" v-model="description" placeholder="Description">
          </div>

          <div class="input-group my-2">
            <input type="file" @change="handleFileUpload"/>
          </div>
        </section>

        <footer class="modal-footer">
          <button
              type="button"
              class="btn btn-primary"
              @click="onUpload"
              aria-label="Login button"
          >
            Upload
          </button>
        </footer>
      </div>
    </div>
  </transition>
</template>

<style>
</style>
