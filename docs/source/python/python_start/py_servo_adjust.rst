.. note::

    Hola, bienvenido a la comunidad de entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _py_servo_adjust:

Ajuste de Servos (Importante)
===========================================

El rango de ángulo del servo es de -90° a 90°, pero el ángulo configurado de fábrica es aleatorio; puede ser 0°, 45° u otro valor. Si lo ensamblamos directamente con dicho ángulo, podría provocar un movimiento desordenado al ejecutar el código en el robot, o peor aún, podría hacer que el servo se bloquee y se queme.

Por ello, es necesario configurar todos los servos en 0° antes de instalarlos, para que el ángulo del servo esté centrado y no haya problemas al girar en ambas direcciones.

#. Para asegurarte de que el servo está correctamente ajustado a 0°, primero inserta el brazo del servo en el eje del servo y luego gira suavemente el brazo a un ángulo diferente. Este brazo de servo es solo para que puedas verificar claramente la rotación del servo.

   .. image:: img/servo_arm.png
       :align: center
   
#. A continuación, ejecuta ``servo_zeroing.py`` en la carpeta ``examples/``.

   .. raw:: html
   
       <run></run>
   
   .. code-block::
   
       cd ~/pidog/examples
       sudo python3 servo_zeroing.py
   
#. Luego, conecta el cable del servo al puerto P11 como se muestra a continuación. Al mismo tiempo, verás que el brazo del servo gira a una posición (esta es la posición de 0°, que es una ubicación aleatoria y puede que no sea vertical o paralela).

   .. image:: img/servo_pin11.jpg
   
#. Ahora, retira el brazo del servo, asegurándote de que el cable del servo permanezca conectado y no apagues la alimentación. Luego, continúa el montaje siguiendo las instrucciones en papel.

.. note::

    * No desconectes el cable del servo antes de fijarlo con el tornillo del servo; puedes desconectarlo después de fijarlo.
    * No gires el servo mientras esté encendido para evitar daños; si el eje del servo no está insertado en el ángulo correcto, sácalo e insértalo nuevamente.
    * Antes de ensamblar cada servo, debes conectar el cable del servo en el pin PWM y encender el dispositivo para ajustar su ángulo a 0°.
