Dropzone.autoDiscover=false;
const myDropzone= new Dropzone('#my-dropzone',{
    url:'upload/file',
    maxFiles:5,
    maxFilesize:2,
    acceptedFiles:'.jpg',
})