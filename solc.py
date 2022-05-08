import solcx

solcx.install_solc('latest')
solcx.install_solc('0.6.6')
solcx.compile_source('', solc_version='0.6.6')