# Ula Ola Surfboard models
From: http://ulaola.site


## The models
Ula Ola surfboards are designed with BoardCad, edited in Rhinoceros3D and final GCode is generated with MeshCam.

All files of the design process models are in "modelFiles" Folder. 

## The Gcode resized software
This small python software that generates all the surfboard GCode sizes fron the original model Gcode.
The usage is very simple.

Edit the file **modelsConf.py**  to add your own gcodes (bottom and top) and define on it all the sizes

```Python
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
      '6\'0\"': [ 1, 0.9481,  1 ],
      '6\'2\"': [ 1, 0.9740, 1 ],
      '6\'4\"': [ 1, 1, 1 ], ## The original size
      '6\'6\"': [ 1, 1.0259, 1 ],
      '6\'8\"': [ 1, 1.0518, 1 ]
    }
  }
}
```
This configuration will generate all gcode sizes, from 6'0" to 6'8"

To generate all gcodes, you have to execute **resizer.py**. Rememeber add +x permissions

```Bash
./resizer.py stuby
```

I wish you Enjoy it :)
