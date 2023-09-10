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

const rows = [
  createData('CHEM 107', 'Altemose A','27.86%', '38.71%','25.81','5.28%','2.35%','2.844'),
  createData('CHEM 107', 'Goodey J','22.12%', '36.87%','29.49%','5.99%','5.53%','2.640'),
  createData('CHEM 107', 'Wang X','23.68%', '31.58%','23.68','15.79%','5.26%','2.844'),
].sort((a, b) => (a.calories < b.calories ? -1 : 1));

export default function ViewGrades(){
    const [page, setPage] = React.useState(0);
    const [rowsPerPage, setRowsPerPage] = React.useState(5);
  
    // Avoid a layout jump when reaching the last page with empty rows.
    const emptyRows =
      page > 0 ? Math.max(0, (1 + page) * rowsPerPage - rows.length) : 0;
  
    const handleChangePage = (event, newPage) => {
      setPage(newPage);
    };
  
    const handleChangeRowsPerPage = (event) => {
      setRowsPerPage(parseInt(event.target.value, 10));
      setPage(0);
    };
    return( 
        <Container maxWidth="lg" sx={{ mt: 4 }}>
        <TableContainer component={Paper} maxWidth="lg" sx={{ mb: 4 }}>
        <Table sx={{ minWidth: 500 }} aria-label="custom pagination table">
          <TableHead>
            <TableRow sx = {{bgcolor: '#C32148'}} >
              <TableCell sx = {{fontSize: 16}}>Course</TableCell>
              <TableCell sx = {{fontSize: 16}}>Professor</TableCell>
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
              ? rows.slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
              : rows
            ).map((row) => (
              <TableRow key={row.name}> 
                <TableCell component="th" scope="row">
                  {row.course}
                </TableCell>
                <TableCell  align="right">
                  {row.professor}
                </TableCell>
                <TableCell  align="right">
                  {row.as}
                </TableCell>
                <TableCell align="right">
                  {row.bs}
                </TableCell>
                <TableCell align="right">
                  {row.cs}
                </TableCell>
                <TableCell align="right">
                  {row.ds}
                </TableCell>
                <TableCell align="right">
                  {row.fs}
                </TableCell>
                <TableCell align="right">
                  {row.GPA}
                </TableCell>
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
                count={rows.length}
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