from celery.task import task
from simple_salesforce import Salesforce

from django.conf import settings
from django.utils import log
import json

logger = log.getLogger(__name__)

INTERVAL = 10 * 60  # 10 minutes
MAX_RETRIES = 100


class SFDCException(Exception):
    pass


@task
def send_signup_info(name, email, address=''):
    if not settings.SFDC_ACCOUNT:
        return
    try:
        res = None
        payload = {'donorName': name, 'email': email, 'donorAddress': ''}
        sf = Salesforce(
            username=settings.SFDC_ACCOUNT,
            security_token=settings.SFDC_TOKEN,
            password=settings.SFDC_PASSWORD
        )
        logger.info('send sign-up to SFDC with data: %s', payload)
        res = sf.apexecute(settings.SFDC_REVOLV_SIGNUP, method='POST', data=payload)
        if res.lower() != 'success':
            raise SFDCException(res)
        logger.info('SFDC sign-up: sucess.')
    except Exception as e:
        logger.error('SFDC sign-up: ERROR for name: %s and data: %s, res: %s', name, payload, res, exc_info=True)
        #send_signup_info.retry(args=[name, email, address], countdown=INTERVAL, exc=e, max_retries=MAX_RETRIES)

@task
def send_nonprofit_info(firstnamedt, lastnamedt, emaildt, orgnamedt, orgaddressdt, orgstatedt, zipcodedt, websitedt, affiliatedt, phonenumberdt, headsourcedt, solarinstallerdt, systemsizedt, epcgrosscostdt, epcyearproductiondt, additionalnotesdt):

    if not settings.SFDC_ACCOUNT:
        return
    try:
        res = None
        payload = {'lastName': 'nonprofitlead', 'company': 'leadNonprpfit', 'email': 'nonprofitformdata4@re-volv.org' }
        sf = Salesforce(
            username=settings.SFDC_ACCOUNT,
            security_token=settings.SFDC_TOKEN,
            password=settings.SFDC_PASSWORD
        )

        sf.Lead.create({'FirstName':firstnamedt, 'LastName':lastnamedt, 'Email': emaildt, 'Company': orgnamedt, 'Street': orgaddressdt,   'Solar_Installer__c': solarinstallerdt, 'System_Size__c': systemsizedt, 'Gross_Cost__c': epcgrosscostdt, 'First_Year_Production__c': epcyearproductiondt, 'Additional_Notes__c': additionalnotesdt, 'State': orgstatedt, 'Country': 'United States',  'PostalCode': zipcodedt, 'Website' : websitedt, 'Title': affiliatedt, 'Phone': phonenumberdt, 'How_did_you_hear_about_us__c': headsourcedt })
        
        logger.info('send sign-up to SFDC with data: %s', payload)
        #res = sf.apexecute('lead', method='POST', data=payload)
        if res.lower() != 'success':
            raise SFDCException(res)
        logger.info('SFDC sign-up: sucess.')
    except Exception as e:
        logger.error('SFDC sign-up: ERROR for name: %s and data: %s, res: %s', emaildt, payload, res, exc_info=True)

@task
def send_volunteer_info(firstnamedt, lastnamedt, emaildt, zipcodedt, colstudentdt, headsourcedt, orgnamedt, orgaddressdt, orgstatedt, websitedt, affiliatedt, phonenumberdt, schoolLocdt, colteamdt, schoolTeamdt):

    if not settings.SFDC_ACCOUNT:
        return
    try:
        res = None
        payload = {'lastName': 'nonprofitlead', 'company': 'leadNonprpfit', 'email': 'nonprofitformdata4@re-volv.org' }
        sf = Salesforce(
            username=settings.SFDC_ACCOUNT,
            security_token=settings.SFDC_TOKEN,
            password=settings.SFDC_PASSWORD
        )

        if orgnamedt == '':
            orgnamedt = 'Solar Ambassador'
        elif orgnamedt == None:
            orgnamedt = 'Solar Ambassador'


        volunteer_type = 'Community Champion'

        if colstudentdt == 'Yes':
            volunteer_type = 'College Fellow'
        elif colstudentdt == 'No':
            volunteer_type = 'Community Champion'

        sf.Lead.create({'FirstName':firstnamedt, 'LastName':lastnamedt, 'Email': emaildt, 'Solar_Ambassador_University__c': schoolLocdt, 'College_Student__c': colstudentdt, 'Existing_Team__c': schoolTeamdt, 'Joining_Existing_Team__c': colteamdt,  'npsp__CompanyPostalCode__c': zipcodedt, 'Company': orgnamedt, 'Volunteer_Type__c': volunteer_type, 'Referral_Type__c': headsourcedt, 'Street': orgaddressdt, 'State': orgstatedt, 'Website' : websitedt, 'Title': affiliatedt,  'Phone': phonenumberdt, 'How_did_you_hear_about_us__c': headsourcedt })
             
        logger.info('send sign-up to SFDC with data: %s', payload)
        #res = sf.apexecute('lead', method='POST', data=payload)
        if res.lower() != 'success':
            raise SFDCException(res)
        logger.info('SFDC sign-up: sucess.')
    except Exception as e:
        logger.error('SFDC sign-up: ERROR for name: %s and data: %s, res: %s', emaildt, payload, res, exc_info=True)

@task
def fetch_user_by_email(email):

    sf = Salesforce(
        username=settings.SFDC_ACCOUNT,
        security_token=settings.SFDC_TOKEN,
        password=settings.SFDC_PASSWORD
    )

    query = "select id, name from Contact where Email = '"+ email +"'"

    loaded = sf.query(query)
    
    output_dict = json.loads(json.dumps(loaded))

    emailName = ''

    for k in output_dict:
        for x in output_dict['records']:
            for key, value in x.items():
                if key == 'Name':
                    emailName = value


    return emailName

def send_donation_info(name, amount,email, project, projectmain, postalcode, state, streetaddress, addressunit, city, emailaddress, firstname, lastname, address=''):
    if not settings.SFDC_ACCOUNT:
        return
    try:
        res = None
        payload = {'donorName': name, 'donorEmail':email, 'projectName': 'Solar Seed Fund', 'donationAmount': amount, 'donorAddress': ''}
        sf = Salesforce(
            username=settings.SFDC_ACCOUNT,
            security_token=settings.SFDC_TOKEN,
            password=settings.SFDC_PASSWORD
        )

        existing_name = fetch_user_by_email(email)

        campaigns = ['Purdue University','UC Santa Barbara','UW Milwaukee''American University','UC Santa Cruz','Coastal Carolina University','The Claremont Colleges','USC','Yale University','University of Dayton','University of Oregon','Solar Seed Fund']

        description = 'Donation for ' + project

        if existing_name == '':

            # if campaign title is one of the static campaign in the array pass through, else use static Solar Seed Fund for sub campaigns
            if any(project in s for s in campaigns):
                payload = {'donorName': name, 'donorEmail':email, 'projectName': project, 'donationAmount': amount, 'projectTitle': description, 'postalCode': postalcode, 'monthlyDonor': 'No','donorAddress': '' ,  'billingState': state, 'billingAddress': streetaddress, 'billingAddressUnit': addressunit, 'billingCity': city, 'billingEmail': emailaddress, 'billingFirstName': firstname, 'billingLastName': lastname }
            elif project == 'Monthly Donations':
                payload = {'donorName': name, 'donorEmail':email, 'projectName': project, 'donationAmount': amount, 'projectTitle': description, 'postalCode': postalcode, 'monthlyDonor': 'Yes', 'donorAddress': ''  ,   'billingState': state, 'billingAddress': streetaddress, 'billingAddressUnit': addressunit, 'billingCity': city, 'billingEmail': emailaddress, 'billingFirstName': firstname, 'billingLastName': lastname}
            else:
                payload = {'donorName': name, 'donorEmail':email, 'projectName': projectmain, 'donationAmount': amount, 'projectTitle': description, 'postalCode': postalcode, 'monthlyDonor': 'No','donorAddress': ''  ,  'billingState': state, 'billingAddress': streetaddress, 'billingAddressUnit': addressunit, 'billingCity': city, 'billingEmail': emailaddress, 'billingFirstName': firstname, 'billingLastName': lastname }

        else:
            
            if any(project in s for s in campaigns):
                payload = {'donorName': existing_name, 'donorEmail':email, 'projectName': project, 'donationAmount': amount, 'projectTitle': description, 'postalCode': postalcode, 'monthlyDonor': 'No','donorAddress': ''  ,   'billingState': state, 'billingAddress': streetaddress, 'billingAddressUnit': addressunit, 'billingCity': city, 'billingEmail': emailaddress, 'billingFirstName': firstname, 'billingLastName': lastname}
            elif project == 'Monthly Donations':
                payload = {'donorName': existing_name, 'donorEmail':email, 'projectName': project, 'donationAmount': amount, 'projectTitle': description, 'postalCode': postalcode, 'monthlyDonor': 'Yes', 'donorAddress': ''   ,   'billingState': state, 'billingAddress': streetaddress, 'billingAddressUnit': addressunit, 'billingCity': city, 'billingEmail': emailaddress, 'billingFirstName': firstname, 'billingLastName': lastname}
            else:
                payload = {'donorName': existing_name, 'donorEmail':email, 'projectName': projectmain, 'donationAmount': amount, 'projectTitle': description, 'postalCode': postalcode, 'monthlyDonor': 'No','donorAddress': ''  ,  'billingState': state, 'billingAddress': streetaddress, 'billingAddressUnit': addressunit, 'billingCity': city, 'billingEmail': emailaddress, 'billingFirstName': firstname, 'billingLastName': lastname}


        if existing_name == '':
            send_signup_info(name, email, address='')
        else: 
            send_signup_info(existing_name, email, address='')

        logger.info('send donation to SFDC with data: %s', payload)
        res = sf.apexecute(settings.SFDC_REVOLV_DONATION, method='POST', data=payload)
        if res.lower() != 'success':
            raise SFDCException(res)
        logger.info('SFDC donation: success.')
    except Exception as e:
        logger.error('SFDC donation: ERROR for name: %s and data: %s, res: %s', name, payload, res, exc_info=True)
        # send_donation_info.retry(args=[name, amount, project, address], countdown=INTERVAL, exc=e,
        #                          max_retries=MAX_RETRIES)