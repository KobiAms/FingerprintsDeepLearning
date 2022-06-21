import React from 'react';
import styles from './styles';
import ResultItem from "../result-item/ResultItem";
import {IconType} from "react-icons";


interface Props {
    title: string;
    icons: IconType[];
    data: any[];
    flexRatio: number;
}

export const FingerNamePrediction = (props: Props) => {





    return(
        <styles.Wrapper flexRatio={props.flexRatio}>
            <styles.PredictionWindow>
            <styles.Header>
                <div style={{display: "flex", flexDirection: 'row'}}>
                    {
                        props.icons.map((Icon, i) => {
                            return <Icon key={i} color={'rgb(115, 115, 115)'}/>
                        })
                    }
                    {/*<IoHandLeft color={'rgb(115, 115, 115)'}/>*/}
                    {/*<IoHandRight color={'rgb(115, 115, 115)'}/>*/}
                </div>
                <div>
                    {props.title}
                </div>
            </styles.Header>
            <styles.Content>
                {
                    props.data
                        .sort((a, b) => b.percentage-a.percentage)
                        .map((item, index) => {
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