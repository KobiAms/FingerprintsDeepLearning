import React, {useCallback, useEffect, useState} from 'react';
import styles from './styles';
import Axios from "axios";
import {useToast} from '@chakra-ui/react'
import {ChakraProvider} from '@chakra-ui/react'
import ImagesZone from "./components/images-zone/ImagesZone";
import PredictionsZone from "./components/predictions-zone/PredictionsZone";

const apiURL = 'http://10.0.0.10:5000'

function App() {

    const [mainFile, setMainFile] = useState<File | undefined>()
    const [samePersonFile, setSamePersonFile] = useState<File | undefined>()
    const [data, setData] = useState<{}>({})
    const [loading, setLoading] = useState(false)
    const toast = useToast()


    const getPredictionsFromServer = (imagesReady: FormData) => {
        setLoading(true)

        // Axios({
        //     url: apiURL+'/api/predictImages',
        //     method: 'post',
        //     withCredentials: true,
        //     data: imagesReady,
        //     headers: {'Content-Type': 'multipart/form-data'}
        // }).then(res => {
        //     // setData(res.data)
        //     setLoading(false)
        // }).catch((err) => {
        //     toast({
        //         title: 'אופס... משהו השתבש',
        //         description: err,
        //         status: 'error',
        //         duration: 5000,
        //         isClosable: true,
        //     })
        //     setLoading(false)
        // })
        if (Math.random() > 0.5) {

            toast({
                title: 'הצחלה',
                description: 'Success',
                status: 'success',
                duration: 5000,
                isClosable: true,
            })
            setLoading(false)
        } else {
            toast({
                title: 'אופס... משהו השתבש',
                description: 'err',
                status: 'error',
                duration: 5000,
                isClosable: true,
            })
            setLoading(false)
        }
    }

    useEffect(() => {
        if (mainFile && samePersonFile) {
            const imagesReady = new FormData()
            imagesReady.append('MainFile', mainFile)
            imagesReady.append('SamePersonFile', samePersonFile)
            getPredictionsFromServer(imagesReady)
        } else if (mainFile) {
            const imagesReady = new FormData()
            imagesReady.append('MainFile', mainFile)
            getPredictionsFromServer(imagesReady)
        }
    }, [mainFile, samePersonFile])


    return (
        <ChakraProvider>
            <styles.App>
                <styles.Wrapper>
                    <ImagesZone loading={loading} setFile={setMainFile} file={mainFile}/>
                    <PredictionsZone setFile={setSamePersonFile} file={samePersonFile} data={data}/>
                </styles.Wrapper>
            </styles.App>
        </ChakraProvider>
    );
}

export default App;
