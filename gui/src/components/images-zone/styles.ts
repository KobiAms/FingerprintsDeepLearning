import styled from 'styled-components';


export namespace styles {

    export const Wrapper = styled.div`
      flex: 1;
      background-color: #000874;
      box-shadow: 0px 3px 6px #4D470029;
      padding: 5%;
      z-index: 1;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: space-evenly;
    `
    export const Dropzone = styled.div`
      width: 100%;
      height: 60%;
      border: 2px dashed #A8E7FF;
      border-radius: 48px;
      padding:10px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
    `

    export const Text = styled.div<{size?: string}>`
      color: white;
      font-size: ${props => props.size ? props.size : '20px'};
      width: max-content;
    `
    export const FakeButton = styled.div<{size?: string}>`
      background-color: white;
      font-size: ${props => props.size ? props.size : '20px'};
      border-radius: 20px;
      width: max-content;
      padding: 7px 30px;
    `
    export const FingerPrintImage = styled.img`
      height: 100%;
      width: 100%;
      border-radius: 40px;
      overflow: hidden;
    `
}

export default styles