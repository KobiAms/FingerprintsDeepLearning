import React from 'react';
import styles from './styles';
import { CircularProgress } from '@mui/material';
import {BsHandIndexThumb} from "react-icons/bs";



interface Props {
    title: string;
    percentage: number;
    icon?: any;
}
export const ResultItem = (props: Props) => {

    return(
        <styles.Wrapper>
            <styles.ResultAndIcon>
                <CircularProgress variant="determinate" color={'inherit'} value={props.percentage}/>
                <div style={{width: '20px'}}/>
                <BsHandIndexThumb/>
            </styles.ResultAndIcon>
            <styles.Title>
                {props.title}
            </styles.Title>
        </styles.Wrapper>
    )
}

export default ResultItem