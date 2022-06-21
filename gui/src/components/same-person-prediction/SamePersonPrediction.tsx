import React, {useCallback, useEffect, useState} from 'react';
import styles from './styles';
import {GoLink} from "react-icons/go";
import {useDropzone} from "react-dropzone";
import {CircularProgress, CircularProgressLabel} from "@chakra-ui/react";

interface Props {
    file: File | undefined
    setFile: (prev: any) => void
    data: any[];
}

export const SamePersonPrediction = (props: Props) => {

    const {file, setFile} = props
    const [imageUri, setImageUri] = useState<string>('')

    const colors = [
        'red.600',
        'red.500',
        'red.400',
        'yellow.600',
        'yellow.500',
        'yellow.400',
        'green.300',
        'green.400',
        'green.500',
        'green.600']

    const onDrop = useCallback((acceptedFiles: any) => {
        setFile(acceptedFiles[0])
    }, [])

    const {getRootProps, getInputProps} = useDropzone({onDrop})

    useEffect(() => {
        if (file) {
            let reader = new FileReader();
            reader.onload = function () {
                setImageUri(reader.result as string);
            };
            reader.readAsDataURL(file as File)
        }
    }, [file])


    return (
        <styles.Wrapper>
            <styles.PredictionWindow>
                <styles.Header>
                    <div>
                        <GoLink color={'rgb(115, 115, 115)'}/>
                    </div>
                    <div>
                        {'התאמה'}
                    </div>
                </styles.Header>
                <styles.Content>
                    <styles.Dropzone {...getRootProps()}>
                        <input {...getInputProps()} />
                        {
                            file ?
                                <styles.FingerPrintImageWrapper>
                                    <div style={{opacity: '0'}}>
                                        <CircularProgress value={15} color={colors[Math.floor(15 / 10)]}>
                                            <CircularProgressLabel>{15}%</CircularProgressLabel>
                                        </CircularProgress>
                                    </div>
                                    <styles.FingerPrintImage src={imageUri}/>
                                    <CircularProgress value={15} color={colors[Math.floor(15 / 10)]}>
                                        <CircularProgressLabel>{15}%</CircularProgressLabel>
                                    </CircularProgress>
                                </styles.FingerPrintImageWrapper>
                                :
                                <>
                                    <styles.Text>
                                        גרור דגימות הנה
                                    </styles.Text>
                                    <div style={{height: '20px'}}/>
                                    <styles.Text>
                                        לבדיקת התאמה
                                    </styles.Text>
                                </>
                        }
                    </styles.Dropzone>
                </styles.Content>
            </styles.PredictionWindow>
        </styles.Wrapper>
    )
}

export default SamePersonPrediction