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
