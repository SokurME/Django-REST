import React from 'react';

const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>{project.name}</td>
            <td>{project.link}</td>
            <td>{project.users}</td>
        </tr>
    )
}

const ProjectList = ({projects}) => {
    return (
        <table border = '1'>
            <tr>
                <th scope="col" style={{'width': '25%'}}>Name</th>
                <th scope="col">Link</th>
                <th scope="col">Users</th>
            </tr>
            <tbody>{projects.map((project) => <ProjectItem project={project}/>)}</tbody>
        </table>
    )
}
export default ProjectList