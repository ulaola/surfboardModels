##RESIZES

#6'0" = 1.83
#6'2" = 1.88
#6'4" = 1.93
#6'6" = 1.98
#6'8" = 2.03

originMainPath = 'modelFiles'
destinationMainPath = 'modelAllSizes'
config = {
  'stuby' : {
    'origin': [
        'stuby/gcode_stuby64/0-bottom_FINAL.gcode',
        'stuby/gcode_stuby64/1-top_FINAL.gcode'
    ],
    'destination': [
        '0-bottom_FINAL.gcode',
        '1-top_FINAL.gcode'
    ],
    'resizes': {
      '6and4': [ 1, 1, 1 ],
      '6and6': [ 1.0259, 1, 1 ]
    }
  }
}
