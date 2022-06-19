import React from 'react';
import styles from './styles';
import {BsGenderAmbiguous} from "react-icons/bs";


export const GenderPrediction = () => {


    return(
        <styles.Wrapper>
            <styles.PredictionWindow>
                <styles.Header>
                    <div>
                        <BsGenderAmbiguous color={'rgb(115, 115, 115)'}/>
                    </div>
                    <div>
                        מגדר
                    </div>
                </styles.Header>
                <styles.Content>

                </styles.Content>
            </styles.PredictionWindow>
        </styles.Wrapper>
    )
}

export default GenderPrediction