var tour = new Tour({
    steps: [
      {
        element: "#tourIntro",
        title: "Instrucciones",
        content: "Vamos a repasar las partes importantes del formulario."
      },
      {
        element: "#player",
        title: "Audio",
        content: "Primero tenés que reproducir el audio y escucharlo hasta el final."
      },
      {
        element: "#tourGeneral",
        title: "Primera evaluación general",
        content: "Luego tenés que calificar el trabajo en equipo según lo que escuchaste, e indicar qué tan seguro estas de tu respuesta."
      },
      {
        element: "#tourDims",
        title: "Dimensiones utilizadas para definir tu respuesta",
        content: "Tenés que indicar qué componentes fueron las más influyentes para definir tu respuesta. Acá podes ver la lista de dimensiones propuestas. Si marcás una dimensión, tenés que indicar de que manera influyo en tu decisión (positiva o negativamente). Por ejemplo, esta anotación indicaria que el liderazgo influyó positivamente. <b>Recordá que solo tenes que marcar las dimensiones que te parezcan reelevantes (almenos una)</b>"
      },
      {
        element: "#tourOtras",
        title: "Otras preguntas",
        content: "Por último, tenés que responder estas tres preguntas."
      },
      {
        element: "#tourComments",
        title: "Comentarios",
        content: "Si querés dejar algún comentario en alguna anotación, podes acceder a una caja de comentarios desde acá."
      },
      {
        element: "#tourNav",
        title: "Barra de navegación",
        content: "En la barra de navegación vas a tener una pestaña en donde vas a poder acceder a todos los audios de un mismo bloque, entre otras opciones. Esto te va a permitir volver a algún audio del bloque por si querés modificar alguna anotación que hayas realizado."
      },
      {
        element: "#tourEnd",
        title: "Comenzar a anotar",
        content: "Eso es todo! Lo siguiente es definir con mayor precisión los conceptos que estamos utilizando para evaluar el trabajo en equipo. Hace click en Continuar para avanzar a la siguiente página."
      }
    ],
    template : "<div class='popover tour'>\
    <div class='arrow'></div>\
    <h3 class='popover-title'></h3>\
    <div class='popover-content'></div>\
    <div class='popover-navigation'>\
    <button class='btn btn-secondary' data-role='prev'>« Anterior</button>\
    <span data-role='separator'> </span>\
    <button class='btn btn-secondary' data-role='next'>Siguiente »</button>\
    <button class='btn btn-success' data-role='end'> Fin </button>\
    </div>\
    </div>",
    backdrop: true,
    storage: false,
});
    
  tour.init();
  tour.start();

  function showText(dim_name) {
    
    // Get the checkbox
    var checkBox = document.getElementById(dim_name).getElementsByClassName('form-check')[1];
    // Get the output text
    var text = document.getElementById(dim_name).getElementsByClassName('dim-text')[0];
    // If the checkbox is checked, display the output text
    if (text.style.display == "none"){
      text.style.display = "block";
    } else {
      text.style.display = "none";
    }
  }


document.querySelectorAll('.arrow').forEach(item => {
  item.addEventListener('click', event => {
    //handle click
    showText(event.target.parentNode.parentNode.id);
    //event.target.classList.toggle('down');
    event.target.parentNode.getElementsByClassName('arrow')[0].classList.toggle('down');
  })
})