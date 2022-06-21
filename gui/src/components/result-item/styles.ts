import styled from 'styled-components';


export namespace styles {

    export const Wrapper = styled.div`
      width: 100%;
      height: min-content;
      background-color: transparent;
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: space-between;
      border-bottom: 0.5px #0002 solid;
    `
    export const ResultAndIcon = styled.div`
      flex: 1;
      padding: 10px;
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: start;
    `
    export const Title = styled.div<{top?: boolean}>`
      flex: 3;
      padding: 10px;
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: end;
      font-size: ${props => props.top ? '40px' : '20px'};
      font-weight: ${props => props.top ? 'bold' : null};
      color: black;
      direction: ltr
      
    `
}

export default styles