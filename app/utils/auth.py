from fastapi import Header


async def get_email(x_goog_authenticated_user_email: str = Header(...)):
    return x_goog_authenticated_user_email.split(':')[1] if ':' in x_goog_authenticated_user_email else x_goog_authenticated_user_email