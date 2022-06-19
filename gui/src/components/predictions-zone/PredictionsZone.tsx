import React from 'react';
import styles from './styles';
import FingerNamePrediction from "../finger-name-prediction/FingerNamePrediction";
import SamePersonPrediction from "../same-person-prediction/SamePersonPrediction";
import GenderPrediction from "../gender-prediction/GenderPrediction";
import ShapePrediction from "../shape-prediction/ShapePrediction";
import QualityPrediction from "../quality-prediction/QualityPrediction";


export const PredictionsZone = () => {





    return(
        <styles.Wrapper>
            <styles.FingerSameSection>
                <FingerNamePrediction/>
                <SamePersonPrediction/>
            </styles.FingerSameSection>
            <styles.GenderShapeQualitySection>
                <GenderPrediction/>
                <ShapePrediction/>
                <QualityPrediction/>
            </styles.GenderShapeQualitySection>
        </styles.Wrapper>
    )

}


export default PredictionsZone