from setuptools import setup



setup( 
    name = 'pakages',
    version = '1.0.Chanante',
    descripcion = 'Esto es un paquete de agencia de viajes',
    author = ['kike-l'],
    author_mail = 'tuemail@gmail.com',
    url = 'https\\www.cosaweb.com',
    packages = ['pakages',
                'pakages.gestion_costumers',
                'pakages.gestion_destino',
                'pakages.gestion_mostrar',
                'pakages.gestion_reservas'
                'pakages.gestion_UI',
                'pakages.gestion_id'
                  ],
    scripts = [] 
    )