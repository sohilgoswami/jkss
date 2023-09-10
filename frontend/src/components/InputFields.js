import * as React from 'react';
import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';
import { Grid, Container, Paper, Button, Card, CardMedia} from '@mui/material';
import { useNavigate } from 'react-router-dom';
import Box from '@mui/material';
import { useState } from 'react';

export default function InputFields() {
  const navigate = useNavigate();
  const [code, setCode] = useState('')
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
            options={courseSubject}
            renderInput={(params) => <TextField {...params} label="Subject"/>}
          />
        </Grid>
        <Grid item xs={12} sm={5.4}>
          <Autocomplete
            disablePortal
            value={code}
            onChange={(event, newValue) => {
              setCode(newValue.label);
            }}
            id="combo-box-demo"
            sx = {{bgcolor: '#FFFFFF'}}
            options={courseCodes}
            renderInput={(params) => <TextField {...params} label="Course Code" value={code} onChange={(e) => setCode(e.target.value)}/>}
          />
        </Grid>
        <Grid item xs={12} sm={1}>
            <Button variant="contained" sx = {{bgcolor: '#EA3B52'}}
              
              onClick={() =>{{navigate('/viewGrades/'+ code, {replace:true})} }}
            >
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

const courseSubject = [
  { label: 'CHEM' },
  { label: 'MATH'},
  { label: 'PHYS'},
];

const courseCodes= [
    { label: '107' },
    { label: '117'},
    { label: '119'},
    { label: '120'},
    { label: '150' },
    { label: '151'},
    { label: '152'},
    { label: '206'},
    { label: '207'},
    { label: '216'},
  ];

