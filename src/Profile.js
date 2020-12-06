import React, { Component } from 'react';
import './Profile.css';
import img from './img.jpeg'


function ProfileInfo(propps) {
    const location = "Location: Las Cruces, New Mexico";
    const school = "School: Las Cruces High School";
    const subject = "Subject: Philosophy";

    return (
        <div>
            {location} <br></br>
            {school} <br></br>
            {subject} <br></br>
            <br></br>
        </div>
	);
}

class PostedMaterials extends Component {
    render() {
        const materials = "Posted Materials: ";

		return (
            <div>
                {materials}
                <ul>
				    <li><button onClick={() => alert('Joe')}>Metaphysics, Dr. Joe, Philosophy, Grade 10, Lecture, ⭐⭐⭐⭐⭐</button></li>
                </ul>
            </div>
			
		);
	}
}


class Profile extends Component{
    render(){
        return(
        <div className="Profile">
            <div className="profile-header">
                <img src={img} alt="Profile Picture" /> <br></br>
                Joe Nathan Lee
            </div>
            <div className="profile-info">
				<ProfileInfo />
			</div>
            <div className="profile-materials">
                <PostedMaterials />
            </div>
        </div>
        );
    }
}

export default Profile;