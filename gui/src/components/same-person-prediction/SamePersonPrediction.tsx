import React from 'react';
import styles from './styles';
import {GoLink} from "react-icons/go";


export const SamePersonPrediction = () => {


    return(
        <styles.Wrapper>
            <styles.PredictionWindow>
                <styles.Header>
                    <div>
                        <GoLink color={'rgb(115, 115, 115)'}/>
                    </div>
                    <div>
                        התאמה
                    </div>
                </styles.Header>
                <styles.Content>

                </styles.Content>
            </styles.PredictionWindow>
        </styles.Wrapper>
    )
}

export default SamePersonPrediction