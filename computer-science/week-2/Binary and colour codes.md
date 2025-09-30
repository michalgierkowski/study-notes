# Binary and colour 

One of binary uses is to define colour
- Each pixel is assigned a specific binary code (so a unique sequence of 0s and 1s)
- It defines the intensity levels of each colour in the 24-bit RGB "true colour model"

**True colour model**
- 24-bit RGB system
- Role: 
- To define how much of RGB (red,green,blue) is needed to display a certain colour
- e.g. (125,50,250) would make violet
- Each colour channel insists of 8 bits of data (binary data to be exact)
- This makes a total of 24-bits

**How is intensity measured?**
- Measured in decimal (denary)
- Uses scale of 0 - 255
- 0 being no appearance of colour
- 255 being maximum
- For example, (255,0,0) --> this would be show 100% of red, no green (off) and no blue (off)

**32-bit RGB model**
- RGBA --> red,green,blue and alpha
- Extra 8-bits channel for "alpha"
- Alpha represents the opacity of the pixel (not the colour, but affects the colour as a side effect)
- Uses scale of 0 - 1 in denary
- 0 being transparent, and 1 being opaque 