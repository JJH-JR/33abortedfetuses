
<script>
      var i = 0;
      var txt = "I am J-Bot, be not afraid.";
      var speed = 50;

      function typeWriter() {
        if (i < txt.length) {
          
          document.getElementById("JJ").innerHTML += txt.charAt(i);
          i++;
          setTimeout(typeWriter, speed);
        }
      }
      </script>