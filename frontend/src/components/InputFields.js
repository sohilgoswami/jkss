import * as React from 'react';
import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';
import { Grid, Container, Paper, Button, Card, CardMedia} from '@mui/material';
import { useNavigate } from 'react-router-dom';
import Box from '@mui/material';
import { useState } from 'react';
import Typography from '@mui/material/Typography';
import CardActionArea from '@mui/material/CardActionArea';
import CardContent from '@mui/material/CardContent';
import axios from 'axios';
import { useEffect } from 'react';

export default function InputFields() {
  const navigate = useNavigate();
  const [courseData, setCourseData] = useState([]);
  const [code, setCode] = useState('')
  const [courseSubject, setCourseSubject] = useState([]);
  const [courseCodes, setCourseCodes] = useState([]);
  const [selectedSubject, setSelectedSubject] = useState(null);
  const [selectedCode, setSelectedCode] = useState('');
  const [professors, setProfessors] = useState([]);
  const [selectedProfessor, setSelectedProfessor] = useState('');
  useEffect(() => {
    // Fetch course data
    axios.get('http://127.0.0.1:5000/get-course-numbers')
      .then(response => {
        setCourseData(response.data);
        // Extract unique subjects and codes
        const subjectsSet = new Set(response.data.map(item => item.subject));
        const codes = [...new Set(response.data.map(item => item.number))];

        // Convert Set back to array
        const subjects = [...subjectsSet];

        setCourseSubject(subjects);
        setCourseCodes(codes);
      })
      .catch(error => {
        console.error('Error fetching course data:', error);
      });
  }, []);
  useEffect(() => {
    if (selectedSubject) {
      const filteredCodes = courseData
        .filter(item => item.subject === selectedSubject)
        .map(item => item.number);

      setCourseCodes(filteredCodes);
      setSelectedCode('');
    }
  }, [selectedSubject, courseData]);
  useEffect(() => {
    // Fetch professor data from your API
    axios.get('http://127.0.0.1:5000/get-professors')
      .then(response => {
        setProfessors(response.data);
      })
      .catch(error => {
        console.error('Error fetching professor data:', error);
      });
  }, []);

  return (
    <React.Fragment>
    <Container maxWidth="lg" sx={{ mb: 4,mt:15}}>
    <Typography textAlign="center" fontWeight="bold" fontSize="3rem" sx = {{lineHeight:{xs:1.2, s:1.2},}}>
          Choose the best professor <span style={{ color: '#B43757' }}>for you</span>!
    </Typography>
    <Paper sx = {{mt:3}}>
      <Grid container spacing={0}>
          {/* Adjust the width of the Grid container */}
          <Grid item xs={12} sm={12} md={6}>
            <Typography fontSize="1.5rem" variant='h4' textAlign="left" sx={{ marginLeft: 5, my:1, marginTop:3, marginBottom:{sm:0, md:-5}}}>
              Search for grade distributions based on course
            </Typography>
          </Grid>
          <Grid item xs={12} sm={12} md={6} sx = {{ml:2}}>
            <Paper variant="outlined" sx={{ my: { xs: 3, md: 6 }, p: { xs: 2, md: 3 }, bgcolor: '#9e2b56'}}>
              <Grid container spacing={3}>
                {/* Subject Field */}
                <Grid item xs={12} sm={12} md={12}>
                  <Autocomplete
                    disablePortal
                    id="combo-box-demo"
                    sx={{ bgcolor: '#FFFFFF',}}
                    options={courseSubject}
                    value={selectedSubject}
                    onChange={(event, newValue) => {
                      setSelectedSubject(newValue);
                    }}
                    renderInput={(params) => <TextField {...params} label="Subject" />}
                  />
                </Grid>

                {/* Course Code Field */}
                <Grid item xs={12} sm={12} md={12}>
                  <Autocomplete
                    disablePortal
                    id="combo-box-demo"
                    sx={{ bgcolor: '#FFFFFF' }}
                    options={courseCodes}
                    value={selectedCode}
                    onChange={(event, newValue) => {
                      setSelectedCode(newValue);
                    }}
                    renderInput={(params) => <TextField {...params} label="Course Code" value={code} onChange={(e) => setCode(e.target.value)} />}
                  />
                </Grid>

                {/* Search Button */}
                <Grid item xs={12} sm={12} md={12}>
                  <Button
                    variant="contained"
                    sx={{ bgcolor: '#EA3B52' }}
                    onClick={() => {
                      navigate('/viewGrades/' + selectedSubject + '/' + selectedCode, { replace: true });
                    }}
                  >
                    Search
                  </Button>
                </Grid>
              </Grid>
            </Paper>
          </Grid>
          <Grid item xs={12} sm={12} md={5.5}>
              <Card sx = {{marginLeft:8}}>
                <CardMedia
                  component="img"
                  src='https://i.ibb.co/wsqJ2hK/REV-PNG-CROPPED.png" alt="REV-PNG-CROPPED'
                />
              </Card>
        </Grid>
        </Grid>
      </Paper>
        {/* Second Paper */}
        <Paper sx={{ mt: 3 }}>
          <Grid container spacing={0} sx = {{mt:5}}>
            {/* Adjust the width of the Grid container */}
            <Grid item xs={12} sm={12} md={5.5} sx={{mt:3, mb:3}}>
              <Card sx={{ marginLeft: 3 }}>
                <CardMedia
                  component="img"
                  src='https://i.ibb.co/8768hh4/SIT-REV.png" alt="SIT-REV'
                />
              </Card>
            </Grid>
            <Grid item xs={12} sm={12} md={6}>
              <Typography fontSize="1.5rem" variant="h4" textAlign="right" sx={{ my: 1, marginTop: {sm:3, md:8}, marginBottom: { sm: 0, md: -5 }, mr: {md:0, sm:5} }}>
                Search for grade distributions based on professor
              </Typography>
            </Grid>
            <Grid item xs={12} sm={12} md={6} sx={{ml:'auto', mr:2, marginTop:{md:-45}}}>
              <Paper variant="outlined" sx={{ my: { xs: 3, md: 6 }, p: { xs: 2, md: 3 }, bgcolor: '#9e2b56' }}>
                <Grid container spacing={3}>
                  {/* Subject Field */}
                  <Grid item xs={12} sm={12} md={12}>
                    <Autocomplete
                      disablePortal
                      id="combo-box-demo"
                      sx={{ bgcolor: '#FFFFFF',}}
                      options={professors.map((professor) => professor.name)}
                      value={selectedProfessor}
                      onChange={(event, newValue) => {
                        setSelectedProfessor(newValue);
                      }}
                      renderInput={(params) => <TextField {...params} label="Professor"  />}
                    />
                  </Grid>
                  <Grid item xs={12} sm={12} md={12}>
                    <Autocomplete
                      disablePortal
                      id="combo-box-demo"
                      sx={{ bgcolor: '#FFFFFF',}}
                      options={courseSubject}
                      value={selectedSubject}
                      onChange={(event, newValue) => {
                        setSelectedSubject(newValue);
                      }}
                      renderInput={(params) => <TextField {...params} label="Department"  />}
                    />
                  </Grid>
                  {/* Search Button */}
                  <Grid item xs={12} sm={12} md={12}>
                    <Button
                      variant="contained"
                      sx={{ bgcolor: '#EA3B52' }}
                      onClick={() => {
                        navigate('/viewProfessor/' + selectedProfessor + '/' + selectedSubject, { replace: true });
                      }}
                    >
                      Search
                    </Button>
                  </Grid>
                </Grid>
              </Paper>
            </Grid>
          </Grid>
        </Paper>
    </Container>
    </React.Fragment>
  );
}