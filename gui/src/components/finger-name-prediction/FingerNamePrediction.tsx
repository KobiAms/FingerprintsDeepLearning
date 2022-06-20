import React from 'react';
import {IoHandLeft, IoHandRight} from 'react-icons/io5';
import styles from './styles';
import ResultItem from "../result-item/ResultItem";


export const FingerNamePrediction = () => {


    const tmparr = [
        {percentage: 70, title: 'אצבע ימין'},
        {percentage: 20, title: 'אצבע שמאל'},
        {percentage: 10, title: 'אגודל ימין'},
    ]


    return(
        <styles.Wrapper>
            <styles.PredictionWindow>
            <styles.Header>
                <div>
                    <IoHandLeft color={'rgb(115, 115, 115)'}/>
                    <IoHandRight color={'rgb(115, 115, 115)'}/>
                </div>
                <div>
                    אצבע
                </div>
            </styles.Header>
            <styles.Content>
                {
                    tmparr.map((item, index) => {
                        return(
                            <ResultItem {...item}/>
                        )
                    })
                }
            </styles.Content>
            </styles.PredictionWindow>
        </styles.Wrapper>
    )
}

export default FingerNamePrediction