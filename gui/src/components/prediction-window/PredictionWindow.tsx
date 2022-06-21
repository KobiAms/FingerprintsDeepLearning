import React from 'react';
import styles from './styles';
import ResultItem from "../result-item/ResultItem";
import {IconType} from "react-icons";


interface Props {
    title: string;
    icons: IconType[];
    data: any[];
    flexRatio: number;
    labels: string[];
    labelsIcons?: IconType[];
}

export const PredictionWindow = (props: Props) => {



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
                </div>
                <div>
                    {props.title}
                </div>
            </styles.Header>
            <styles.Content>
                {
                    props.data?.map((a, i) => ({a: a, i:i}))
                        .sort((a, b) => b.a-a.a)
                        .map(({a, i}, index) => {
                        return(
                            <ResultItem
                                top={index == 0}
                                key={index}
                                icon={props.labelsIcons && props.labelsIcons[i]}
                                title={props.labels[i]}
                                percentage={Math.floor(a*100)}/>
                        )
                    })
                }
            </styles.Content>
            </styles.PredictionWindow>
        </styles.Wrapper>
    )
}

export default PredictionWindow