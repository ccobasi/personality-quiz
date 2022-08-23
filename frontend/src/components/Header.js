import React from 'react';
import {makeStyles} from "@material-ui/core/styles";
import { AppBar, Toolbar, Typography } from '@material-ui/core';

const useStyles = makeStyles((theme) => ({
    root:{
        flexGrow:1,
    },

    toolbarTitle:{
        flexGrow:1,
    }
}));

const Header = () => {
    const classes = useStyles();
  return (
    <div className={classes.root}>
        <AppBar position="static" color="primary" elevation={0}>
            <Toolbar>
                <Typography variant="h6" color="inherit" className={classes.toolbarTitle}>
                    Personality Quiz
                </Typography>
            </Toolbar>
        </AppBar>
    </div>
  )
}

export default Header