import * as React from 'react';
import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';
<<<<<<< Updated upstream
import { Grid, Container, Paper, Button, Card, CardMedia} from '@mui/material';
import { useNavigate } from 'react-router-dom';
import Box from '@mui/material';
=======
import { Grid, Container, Paper, Button} from '@mui/material';
>>>>>>> Stashed changes

export default function InputFields() {
  return (
    <React.Fragment>
    <Container maxWidth="lg" sx={{ mb: 4 }}>
    <Paper variant="outlined" sx={{ my: { xs: 3, md: 6 }, p: { xs: 2, md: 3 }, bgcolor: '#9e2b56'}} >
    <Grid container spacing = {3}>
        <Grid item xs={12} sm={5.4}>
          <Autocomplete
            disablePortal
            id="combo-box-demo"
            sx = {{bgcolor: '#FFFFFF'}}
            options={top100Films}
            renderInput={(params) => <TextField {...params} label="Subject" />}
          />
        </Grid>
        <Grid item xs={12} sm={5.4}>
          <Autocomplete
            disablePortal
            id="combo-box-demo"
            sx = {{bgcolor: '#FFFFFF'}}
            options={top100Films}
            renderInput={(params) => <TextField {...params} label="Course Code" />}
          />
        </Grid>
        <Grid item xs={12} sm={1}>
            <Button variant="contained" sx = {{bgcolor: '#EA3B52'}}>
                Search
            </Button>
        </Grid>
    </Grid>
    </Paper>
    </Container>
    <Container>
        <Card>
          <CardMedia
           component="img"
           src= 'https://i.ibb.co/wsqJ2hK/REV-PNG-CROPPED.png" alt="REV-PNG-CROPPED'
          />
        </Card>
    </Container>
    </React.Fragment>
  );
}

// Top 100 films as rated by IMDb users. http://www.imdb.com/chart/top
const top100Films = [
  
];