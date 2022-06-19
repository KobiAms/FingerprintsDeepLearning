import React from 'react';
import {IoHandLeft, IoHandRight} from 'react-icons/io5';
import styles from './styles';


export const FingerNamePrediction = () => {


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

            </styles.Content>
            </styles.PredictionWindow>
        </styles.Wrapper>
    )
}

export default FingerNamePrediction