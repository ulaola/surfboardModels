##RESIZES

#5'0" = 152
#5'2" = 157
#5'4" = 163
#5'6" =	168
#5'8" =	173
#5'10" =178
#6'0" = 183
#6'2" = 188
#6'4" = 193
#6'6" = 198
#6'8" = 203
#7'0" = 213
#8'0" = 243



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
      '6\'0\"': [ 1, 0.9481, 1 ],
      '6\'2\"': [ 1, 0.9740, 1 ],
      '6\'4\"': [ 1, 1, 1 ], ## The original size
      '6\'6\"': [ 1, 1.0259, 1 ],
      '6\'8\"': [ 1, 1.0518, 1 ]
    }
  },


  'minimal' : {
    'origin': [
        'minimal/manimal8-gcode/1-bottom_mal8FINAL.gcode',
        'minimal/manimal8-gcode/2-top_mal8FINAL.gcode'
    ],
    'destination': [
        '0-bottom_FINAL.gcode',
        '1-top_FINAL.gcode'
    ],
    'resizes': {

      '6\'6\"': [ 1, 0.81481, 1 ],
      '7\'0\"': [ 1, 0.87654, 1 ],
      '8\'0\"': [ 1, 1, 1 ] ##  The original size
    }
  }
}
