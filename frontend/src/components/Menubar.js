import React from "react";
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/icons-material/Menu';
import HouseIcon from '@mui/icons-material/House';

function Menubar(){
    return(
      <AppBar position="static" sx = {{bgcolor: '#6a1d3a'}}>
      <Toolbar>
        <Typography variant="h5" component="div" sx={{ flexGrow: 1 }}>
          JKSS Grade Distributions
        </Typography>
        <IconButton
          id="basic-button"
          size = 'large'
          color = 'inherit'
          style={{ marginLeft: "auto" }} 
          href = '/'
        >
          <HouseIcon/>
        </IconButton>
      </Toolbar>
      </AppBar>
    )
}
export default Menubar