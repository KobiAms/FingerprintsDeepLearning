import React, {useCallback, useEffect, useState} from 'react';
import styles from './styles';
import {useDropzone} from "react-dropzone";
import { IoFingerPrint } from 'react-icons/io5';

interface Props {
    file: File | undefined
    setFile: (prev:any) => void
}

export const ImagesZone = (props: Props) => {

    const {file, setFile} = props
    const [imageUri, setImageUri] = useState<string>('')

    const onDrop = useCallback((acceptedFiles:any) => {
        setFile(acceptedFiles[0])
    }, [])

    const {getRootProps, getInputProps} = useDropzone({onDrop})

    useEffect(() => {
        if(file){
            let reader = new FileReader();
            reader.onload = function(){
                setImageUri(reader.result as string);

            };
            reader.readAsDataURL(file as File)
        }
    }, [file])


    return(
        <styles.Wrapper>
            <styles.Dropzone {...getRootProps()}>
                <input {...getInputProps()} />
                {
                    file ?
                        <styles.FingerPrintImage src={imageUri}/>
                        :
                <>
                    <styles.Text>
                        גרור דגימות לכאן
                    </styles.Text>
                    <div style={{height: '20px'}}/>
                    <styles.Text size={'16px'}>
                        או
                    </styles.Text>
                    <div style={{height: '20px'}}/>
                    <styles.FakeButton>
                        העלה תמונות מהמחשב
                    </styles.FakeButton>
                </>
                }
            </styles.Dropzone>
            <IoFingerPrint size={'40px'} color={'white'}/>
            <styles.Text size={'12px'}>
                Developed by Kobi Amsellem  and Zohar Kedem
            </styles.Text>
        </styles.Wrapper>
    )

}


export default ImagesZone