from ..Utils.executeRest import execute
from ..Utils.incapError import IncapError
import logging
import base64
from ..Utils.incapResponse import CertResponse


def u_certificate(args):
    param = vars(args)
    #action = param['do']
    output = 'Upload Certificate to: {0}'. format(args.site_id)
    logging.basicConfig(format='%(levelname)s - %(message)s',  level=getattr(logging, args.log.upper()))
    print(output)

    # param = {
    #     "api_id": args.api_id,
    #     "api_key": args.api_key,
    #     "site_id": args.site_id,
    #     "certificate": args.certificate,
    #     "private_key": args.private_key,
    #     "passphrase": args.passphrase
    # }

    result = upload(param)

    if int(result.get('res')) != 0:
        err = IncapError(result)
        err.log()
        return err
    else:
        cert = CertResponse(result)
        print('Added certificate to site ID: {} '.format(args.site_id))
        cert.log()
        return cert


def upload(params):
    resturl = 'sites/customCertificate/upload'
    if params:
        logging.debug(params)
        if "certificate" in params:
            cert_file = open(params['certificate'], 'rb')
            encoded_cert = base64.b64encode(cert_file.read())
            cert_file.close()
            params['certificate'] = encoded_cert
            if params["private_key"] is not None:
                key_file = open(params['private_key'], 'rb')
                encoded_key = base64.b64encode(key_file.read())
                key_file.close()
                params['private_key'] = encoded_key
            else:
                del params['private_key']
            if params['passphrase'] is None:
                del params['passphrase']
            return execute(resturl, params)
        else:
            logging.warning("No certificate parameter has been passed in for %s." % __name__)
    else:
        logging.error('No parameters where passed in.')