import { Container, Typography } from '@mui/material';
import * as React from 'react';

import PropTypes from 'prop-types';
import { useTheme } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableFooter from '@mui/material/TableFooter';
import TablePagination from '@mui/material/TablePagination';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import IconButton from '@mui/material/IconButton';
import FirstPageIcon from '@mui/icons-material/FirstPage';
import KeyboardArrowLeft from '@mui/icons-material/KeyboardArrowLeft';
import KeyboardArrowRight from '@mui/icons-material/KeyboardArrowRight';
import LastPageIcon from '@mui/icons-material/LastPage';
import TableHead from '@mui/material/TableHead';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import { useEffect } from 'react';
import { useState } from 'react';

function TablePaginationActions(props) {
    const theme = useTheme();
    const { count, page, rowsPerPage, onPageChange } = props;
  
    const handleFirstPageButtonClick = (event) => {
      onPageChange(event, 0);
    };
  
    const handleBackButtonClick = (event) => {
      onPageChange(event, page - 1);
    };
  
    const handleNextButtonClick = (event) => {
      onPageChange(event, page + 1);
    };
  
    const handleLastPageButtonClick = (event) => {
      onPageChange(event, Math.max(0, Math.ceil(count / rowsPerPage) - 1));
    };
  
    return (
      <Box sx={{ flexShrink: 0, ml: 2.5 }}>
        <IconButton
          onClick={handleFirstPageButtonClick}
          disabled={page === 0}
          aria-label="first page"
        >
          {theme.direction === 'rtl' ? <LastPageIcon /> : <FirstPageIcon />}
        </IconButton>
        <IconButton
          onClick={handleBackButtonClick}
          disabled={page === 0}
          aria-label="previous page"
        >
          {theme.direction === 'rtl' ? <KeyboardArrowRight /> : <KeyboardArrowLeft />}
        </IconButton>
        <IconButton
          onClick={handleNextButtonClick}
          disabled={page >= Math.ceil(count / rowsPerPage) - 1}
          aria-label="next page"
        >
          {theme.direction === 'rtl' ? <KeyboardArrowLeft /> : <KeyboardArrowRight />}
        </IconButton>
        <IconButton
          onClick={handleLastPageButtonClick}
          disabled={page >= Math.ceil(count / rowsPerPage) - 1}
          aria-label="last page"
        >
          {theme.direction === 'rtl' ? <FirstPageIcon /> : <LastPageIcon />}
        </IconButton>
      </Box>
    );
  }
  
  TablePaginationActions.propTypes = {
    count: PropTypes.number.isRequired,
    onPageChange: PropTypes.func.isRequired,
    page: PropTypes.number.isRequired,
    rowsPerPage: PropTypes.number.isRequired,
  };
  
  function createData(course, professor, as, bs, cs, ds, fs, GPA) {
    return { course, professor, as, bs, cs, ds, fs, GPA };
  }
  
  
  
  export default function ViewProfessor(){
      const [page, setPage] = React.useState(0);
      const [rowsPerPage, setRowsPerPage] = React.useState(5);
      const [courseData, setCourseData] = useState([]);
      const [filteredCourseData, setFilteredCourseData] = useState([]);
    
      // Avoid a layout jump when reaching the last page with empty rows.
      const emptyRows =
        page > 0 ? Math.max(0, (1 + page) * rowsPerPage - filteredCourseData.length) : 0;
    
      const handleChangePage = (event, newPage) => {
        setPage(newPage);
      };
    
      const handleChangeRowsPerPage = (event) => {
        setRowsPerPage(parseInt(event.target.value, 10));
        setPage(0);
      };
      const prof = useParams();
      const desired_prof = prof.profName
      useEffect(() => {
        // Make a GET request to your Flask back-end
        axios.get('http://127.0.0.1:5000/get-courses')
          .then(response => {
            setCourseData(response.data);
          })
          .catch(error => {
            console.error('Error fetching data:', error)
          });
      }, []);
      useEffect(() => {
        // Filter the courseData based on the selected course_id
        const filteredData = courseData.filter((row) => row.professor === desired_prof);
        setFilteredCourseData(filteredData);
      }, [desired_prof, courseData]);
      return( 
          <Container maxWidth="lg" sx={{ mt: 15 }}>
            <Typography textAlign="center" fontWeight="bold" fontSize="2rem" sx = {{lineHeight:{xs:1.2, s:1.2}, mb: 3}}>
              Grade Distributions for <span style={{ color: '#B43757' }}>{desired_prof}</span> 
            </Typography>
          <TableContainer component={Paper} maxWidth="lg" sx={{ mb: 4 }}>
          <Table sx={{ minWidth: 500 }} aria-label="custom pagination table">
            <TableHead>
              <TableRow sx = {{bgcolor: '#C32148'}} >
                <TableCell sx = {{fontSize: 16}}>Section</TableCell>
                <TableCell sx = {{fontSize: 16}}>Term</TableCell>
                <TableCell sx = {{fontSize: 16}}>% of As</TableCell>
                <TableCell sx = {{fontSize: 16}}>% of Bs</TableCell>
                <TableCell sx = {{fontSize: 16}}>% of Cs</TableCell>
                <TableCell sx = {{fontSize: 16}}>% of Ds</TableCell>
                <TableCell sx = {{fontSize: 16}}>% of Fs</TableCell>
                <TableCell sx = {{fontSize: 16}}>GPA</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {(rowsPerPage > 0
                ? filteredCourseData.slice(
                    page * rowsPerPage,
                    page * rowsPerPage + rowsPerPage
                  )
                : filteredCourseData
              ).map((row) => (
                <TableRow key={row.id}>
                  <TableCell component="th" scope="row">
                    {row.course}
                  </TableCell>
                  <TableCell>{row.term}</TableCell>
                  <TableCell>{row.perA}</TableCell>
                  <TableCell>{row.perB}</TableCell>
                  <TableCell>{row.perC}</TableCell>
                  <TableCell>{row.perD}</TableCell>
                  <TableCell>{row.perF}</TableCell>
                  <TableCell>{row.GPA}</TableCell>
                </TableRow>
              ))}
              {emptyRows > 0 && (
                <TableRow style={{ height: 53 * emptyRows }}>
                  <TableCell colSpan={6} />
                </TableRow>
              )}
            </TableBody>
            <TableFooter>
              <TableRow>
                <TablePagination
                  rowsPerPageOptions={[5, 10, 25, { label: 'All', value: -1 }]}
                  colSpan={8}
                  count={filteredCourseData.length}
                  rowsPerPage={rowsPerPage}
                  page={page}
                  SelectProps={{
                    inputProps: {
                      'aria-label': 'rows per page',
                    },
                    native: true,
                  }}
                  onPageChange={handleChangePage}
                  onRowsPerPageChange={handleChangeRowsPerPage}
                  ActionsComponent={TablePaginationActions}
                />
              </TableRow>
            </TableFooter>
          </Table>
        </TableContainer>
        </Container>
      )
  }