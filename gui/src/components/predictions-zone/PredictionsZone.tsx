import React from 'react';
import styles from './styles';
import PredictionWindow from "../prediction-window/PredictionWindow";
import SamePersonPrediction from "../same-person-prediction/SamePersonPrediction";
import {IoHandLeft, IoHandRight, IoShapesSharp} from 'react-icons/io5';
import {BsGenderAmbiguous, BsShieldCheck} from 'react-icons/bs';
import {BiFemaleSign, BiMaleSign} from "react-icons/bi";
import { GiBarracksTent, GiWhirlwind} from "react-icons/gi";
import { RiRainbowLine} from "react-icons/ri";
import { TbArrowLoopLeft, TbArrowLoopRight} from "react-icons/tb";

interface Props {
    file: File | undefined;
    setFile: (prev:any) => void;
    data: any;
}

export const PredictionsZone = (props: Props) => {

    return (
        <styles.Wrapper>
            <styles.FingerSameSection>
                <PredictionWindow flexRatio={4} data={props.data.fingerName} title={'אצבע'} icons={[IoHandLeft, IoHandRight]} labels={FingerNames}/>
                <SamePersonPrediction file={props.file} setFile={props.setFile}/>
            </styles.FingerSameSection>
            <styles.GenderShapeQualitySection>
                <PredictionWindow flexRatio={1} data={props.data.gender} title={'מגדר'} icons={[BsGenderAmbiguous]} labels={Genders} labelsIcons={GenderIcons}/>
                <PredictionWindow flexRatio={1} data={props.data.shape} title={'צורה'} icons={[IoShapesSharp]} labels={Shapes} labelsIcons={ShapesIcons}/>
                <PredictionWindow flexRatio={1} data={props.data.quality} title={'איכות'} icons={[BsShieldCheck]} labels={Qualities}/>
            </styles.GenderShapeQualitySection>
        </styles.Wrapper>
    )

}

export default PredictionsZone


const FingerNames = [
    '1 - אגודל ימין',
    '2 - אצבע ימין',
    '3 - אמה ימין',
    '4 - קמיצה ימין',
    '5 - זרת ימין',
    '6 - אגודל שמאל',
    '7 - אצבע שמאל',
    '8 - אמה שמאל',
    '9 - קמיצה שמאל',
    '10 - זרת שמאל',
]

const Genders = [
    'נקבה',
    'זכר'
]

const GenderIcons = [
    BiMaleSign,
    BiFemaleSign
]

const Shapes = [
    'לולאה שמאל',
    'מערבולת',
    'לולאה ימין',
    'אוהל/קשת',
    'אוהל'
]

const ShapesIcons = [
    TbArrowLoopLeft,
    GiWhirlwind,
    TbArrowLoopRight,
    RiRainbowLine,
    GiBarracksTent
]


const Qualities = [
    '0 - גרוע מאוד',
    '1 - גרוע',
    '2 - בינוני',
    '3 - טוב',
    '4 - טוב ביותר',
]