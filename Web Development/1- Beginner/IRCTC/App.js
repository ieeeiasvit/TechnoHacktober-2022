import './App.css';
import Box from './Components/Box';
import Form from './Components/Form';
import Msg from './Components/Msg';
import img from './Assets/Group 2.svg';
import ss from './Assets/Frame 6.png';
import { ReactMic } from 'react-mic';
import { useState } from 'react';

function App() {
	const onData = (recordedBlob) => {
		console.log('chunk of real-time data is: ', recordedBlob);
	};
	const [scam, setScam] = useState(false);
	const onStop = (recordedBlob) => {
		console.log('recordedBlob is: ', recordedBlob);
	};
	const [rec, setRec] = useState(false);
	const clickHandler = () => {
		setScam(true);
	};
	return (
		<div className='App'>
			{scam ? (
				<>
					<img
						src={ss}
						style={{
							width: '100vw',
							height: '100vh',
							position: 'fixed',
						}}
					/>
				</>
			) : (
				<>
					<div
						style={{
							height: '15%',
							width: '100%',
							display: 'flex',
							justifyContent: 'center',
							alignItems: 'center',
						}}>
						<div className='as'>INDIAN RAILWAYS</div>
					</div>

					<Box>
						<Form scam={rec} clickHandler={clickHandler} />
						<Msg />
					</Box>
					<div
						style={{
							position: 'fixed',
							bottom: '5%',
							right: '5%',
							width: '30vw',
							display: 'flex',
						}}>
						<ReactMic
							record={rec}
							className={`sound-wave ${rec ? '' : 'ded'}`}
							onStop={onStop}
							onData={onData}
							strokeColor='#ffffff'
							backgroundColor='#000000'
						/>
						<img
							src={img}
							style={{ cursor: 'pointer' }}
							onClick={() => setRec((prev) => !prev)}
						/>
					</div>
				</>
			)}
		</div>
	);
}

export default App;
