import React from "react";
import {Link} from "react-router-dom";


const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>{project.id}</td>
            <td><Link to={`/projects/${project.id}/`} className={'link'}>{project.name}</Link></td>
            <td>{project.repoLink}</td>
            <td>{project.users.map(user => user.username).join(', ')}</td>
        </tr>
    )
}

const ProjectList = ({projects}) => {
    return (
        <table className={'tab'}>
            <thead>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Repository link</th>
                <th>Users</th>
            </tr>
            </thead>
            <tbody>
            {projects.map((project) => <ProjectItem key={project.id} project={project}/>)}
            </tbody>
        </table>
    )
}
export default ProjectList;
