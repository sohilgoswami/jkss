import * as React from 'react';
import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';
import { Grid, Container, Paper, Button} from '@mui/material';
import { useNavigate } from 'react-router-dom';

export default function InputFields() {
  const navigate = useNavigate();
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
            renderInput={(params) => <TextField {...params} label="Subject" />}
          />
        </Grid>
        <Grid item xs={12} sm={5.4}>
          <Autocomplete
            disablePortal
            id="combo-box-demo"
            sx = {{bgcolor: '#FFFFFF'}}
            options={courseCodes}
            renderInput={(params) => <TextField {...params} label="Course Code" />}
          />
        </Grid>
        <Grid item xs={12} sm={1}>
            <Button variant="contained" sx = {{bgcolor: '#EA3B52'}}
              href = '/viewGrades'
            >
                Search
            </Button>
        </Grid>
    </Grid>
    </Paper>
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

