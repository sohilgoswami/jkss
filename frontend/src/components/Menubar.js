import React from "react";
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import '@fontsource/caveat-brush';
import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/icons-material/Menu';
import HouseIcon from '@mui/icons-material/House';
import Image from 'mui-image'
import useScrollTrigger from "@mui/material/useScrollTrigger";

function Menubar(){
  const trigger = useScrollTrigger({
    disableHysteresis: true,
    threshold: 0,
  });
    return(
      <AppBar sx = {{bgcolor: '#6a1d3a',  borderBottom: trigger ? "1px solid rgba(0, 0, 0, 0.12)" : "none" }}>
      <Toolbar>
        <Button href="/" sx={{ ml: '15px' }}>
          <Box
            component="img"
            sx={{
              height: 65,
              width: 65,
            }}
            
            src= "https://i.ibb.co/Dzv59KK/MAROON-REV.png"
          />
        </Button>
        <Typography variant="h6" component="div" sx={{ flexGrow: 0.85, fontFamily: 'Caveat Brush', fontSize:32, textAlign: 'center'}}>
          JKSS Grade Distributions
        </Typography>
      </Toolbar>
      </AppBar>
    )
}
export default Menubar