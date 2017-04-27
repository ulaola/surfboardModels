##RESIZES
#6'0" = 1.83
#6'2" = 1.88
#6'4" = 1.93
#6'6" = 1.98
#6'8" = 2.03


config = {
  'stuby' : {
    'resizes': {
      '6and4': [ 1, 1, 1 ],
      '6and6': [ 1.028, 1, 1 ]
    }
  }
}

selectedModel = 'stuby'


if selectedModel in config:
    for sizeKey in config['stuby']['resizes']:
        print config['stuby']['resizes'][sizeKey]
else:
    print 'model not found: '+ selectedModel
