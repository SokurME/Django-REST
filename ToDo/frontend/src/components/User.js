import React from 'react';

const UserItem = ({user}) => {
    return (
        <tr>
            <td>{user.username}</td>
            <td>{user.firstname}</td>
            <td>{user.lastname}</td>
            <td>{user.email}</td>
        </tr>
    )
}

const UserList = ({users}) => {
    return (
        <table border = '1'>
            <tr>
                <th scope="col">Name</th>
                <th scope="col">First name</th>
                <th scope="col">Last Name</th>
                <th scope="col">E-mail</th>
            </tr>
            <tbody>{users.map((user) => <UserItem user={user}/>)}</tbody>
        </table>
    )
}
export default UserList