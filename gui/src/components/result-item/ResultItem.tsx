import React from 'react';
import styles from './styles';
import { CircularProgress, CircularProgressLabel } from '@chakra-ui/react'



interface Props {
    title: string;
    percentage: number;
    icon?: any;
    top?: boolean
}
export const ResultItem = (props: Props) => {

    const colors = [
        'red.600',
        'red.500',
        'red.400',
        'yellow.600',
        'yellow.500',
        'yellow.400',
        'green.300',
        'green.400',
        'green.500',
        'green.600']


    return(
        <styles.Wrapper>
            <styles.ResultAndIcon>
                <CircularProgress value={props.percentage} color={colors[Math.floor(props.percentage/10)]}>
                    <CircularProgressLabel>{props.percentage}%</CircularProgressLabel>
                </CircularProgress>
                <div style={{width: '20px'}}/>
                {props.icon && <props.icon/>}
            </styles.ResultAndIcon>
            <styles.Title top={props.top}>
                {props.title}
            </styles.Title>
        </styles.Wrapper>
    )
}

export default ResultItem