from chain import Chain
#import keyboard
import managechaintools
import maptools
import os

main_chain, RT_chain = Chain("Main Chain", maptools.gen_chain_map()), Chain("RT Chain", maptools.gen_RT_map())

chains = {"m":main_chain, "r":RT_chain}



while True:
    managechaintools.display_chains(main_chain, RT_chain)

    #key = keyboard.read_key().lower()
    key = input()

    if key == "q": break

    if not chains.get(key):
            continue
    managechaintools.manage_chain_selection(chains.get(key))

