import React, { Component } from 'react';
import './Main.css';
import Dropdown from 'react-dropdown';
import 'react-dropdown/style.css';
import img from './img.jpeg'

function Filter(props) {
	const options = [
		'Author', 'Subject', 'Level of Education', 'Category', 'Rating'
	];

	return (
		<div>
			Filter by:
			<Dropdown options={options} onChange={() => alert('change!')} placeholder="Select a filter" />
		</div>
	);
}

function Profile(props) {

	return (
		<div>
			Hi, Jonathan
			<input type="image" src={img} onClick={() => alert('Profile')} />
		</div>
	);
}

class MaterialsList extends Component {
	render() {
		return (
			<ul>
				<li><button onClick={() => alert('Eddie Kong')}>Logisim Tutorial, Eddie Kong, CS, Grade 8, Lecture, ⭐⭐⭐⭐⭐</button></li>
				<li><button onClick={() => alert('Joe')}>Metaphysics, Dr. Joe, Philosophy, Grade 10, Lecture, ⭐⭐⭐⭐⭐</button></li>
			</ul>
		);
	}
}

function PostMaterial(props) {
	return (
		<button onClick={() => alert('post')}>Post material</button>
	);
}

class Main extends Component {
	render() {
		return (
			<div className="main">
				<div className="main-header">
					Name of App
				</div>
				<div className="main-profile">
					<Profile />
				</div>
				<div className="main-filter">
					<Filter />
				</div>
				<div className="main-materials">
					<MaterialsList />
				</div>
				<div className="main-postmaterial">
					<PostMaterial />
				</div>
			</div>
		);
	}
}

export default Main;