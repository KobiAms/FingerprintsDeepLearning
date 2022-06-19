import React from 'react';
import styles from './styles';
import {IoShapesSharp} from "react-icons/io5";


export const ShapePrediction = () => {


    return(
        <styles.Wrapper>
            <styles.PredictionWindow>
                <styles.Header>
                    <div>
                        <IoShapesSharp color={'rgb(115, 115, 115)'}/>
                    </div>
                    <div>
                        צורה
                    </div>
                </styles.Header>
                <styles.Content>

                </styles.Content>
            </styles.PredictionWindow>
        </styles.Wrapper>
    )
}

export default ShapePrediction