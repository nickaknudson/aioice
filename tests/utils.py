import asyncio


async def invite_accept(conn_a, conn_b):
    # invite
    await conn_a.gather_candidates()
    conn_b.remote_candidates = conn_a.local_candidates
    conn_b.remote_username = conn_a.local_username
    conn_b.remote_password = conn_a.local_password

    # accept
    await conn_b.gather_candidates()
    conn_a.remote_candidates = conn_b.local_candidates
    conn_a.remote_username = conn_b.local_username
    conn_a.remote_password = conn_b.local_password


def run(coro):
    return asyncio.get_event_loop().run_until_complete(coro)
