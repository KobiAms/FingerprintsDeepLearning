import React from 'react';
import styles from './styles';
import {BsShieldCheck} from "react-icons/bs";

export const QualityPrediction = () => {

    return(
        <styles.Wrapper>
            <styles.PredictionWindow>
                <styles.Header>
                    <div>
                        <BsShieldCheck color={'rgb(115, 115, 115)'}/>
                    </div>
                    <div>
                        איכות
                    </div>
                </styles.Header>
                <styles.Content>

                </styles.Content>
            </styles.PredictionWindow>
        </styles.Wrapper>
    )
}

export default QualityPrediction