import styled from 'styled-components';


export namespace styles {

    export const Wrapper = styled.div`
      flex: 3;
      background-color: transparent;
      padding: 10px;
      display: flex;
    `
    export const PredictionWindow = styled.div`
      flex: 1;
      background-color: #FDFDFD;
      display: flex;
      flex-direction: column;
      box-shadow: 1px 5px 10px #00000030;
      border-radius: 10px;
      overflow: hidden;
    `

    export const Header = styled.div`
      flex: 1;
      padding: 10px;
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: space-between;
      background-color: #FDFDFD;
      box-shadow: 0px 3px 6px #00000017;
      z-index: 1;
    `

    export const Content = styled.div`
      flex: 7;
      padding: 20px;
      background-color: #FDFDFD;
      display: flex;
      z-index: 0;
    `

    export const Dropzone = styled.div`
      width: 100%;
      height: 100%;
      max-height: 100%;
      max-width: 100%;
      border: 4px dashed #aaa;
      border-radius: 5px;
      padding: 10px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      min-height: 0;
    `

    export const Text = styled.div<{size?: string}>`
      color: black;
      font-size: ${props => props.size ? props.size : '20px'};
      width: max-content;
    `

    export const FingerPrintImage = styled.img`
      border-radius: 10px;
      height: 150px;
      width: 150px;
    `

}

export default styles