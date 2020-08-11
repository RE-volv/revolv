import json
import logging
from decimal import Decimal
from json import load
from urllib2 import urlopen

import stripe
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import JsonResponse
from django.http.response import HttpResponseBadRequest, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods, require_POST
from django.views.generic import CreateView, DetailView, UpdateView, TemplateView
from django.views.generic.edit import FormView
from revolv.base.models import RevolvUserProfile
from revolv.base.users import UserDataMixin
from revolv.base.utils import is_user_reinvestment_period
from revolv.lib.mailer import send_revolv_email
from revolv.payments.forms import CreditCardDonationForm
from revolv.payments.models import UserReinvestment, Payment, PaymentType, Tip, ReferralSourceTrack
from revolv.payments.services import PaymentService
from revolv.project import forms
from revolv.project.models import Category, Project, ProjectUpdate, ProjectMatchingDonors, AnonymousUserDetail, \
    StripeDetails, AnonymousUserDonation
from revolv.base.utils import ProjectGroup
from revolv.tasks.sfdc import send_donation_info
from sesame import utils

logger = logging.getLogger(__name__)
MAX_PAYMENT_CENTS = 99999999
stripe.api_key = settings.STRIPE_SECRET_KEY

from createsend import Transactional
from createsend import Subscriber



def stripe_address_sfdc(request):
    try:
        streetz = request.POST['stripestreet'] 
        suitez = request.POST['stripesuite']
        cityz = request.POST['formcity'] 
        statez = request.POST['formstate']

        firstnamez = request.POST['stripefirstname'] 
        lastnamez = request.POST['stripelastname'] 

        tshirtz = ''
        mailingstreetz = ''
        mailingsuitez = ''
        mailingcityz = ''
        mailingstatez = ''

        if request.POST.get("stripetshirt", None):
            tshirtz = request.POST['stripetshirt']
            mailingstreetz = request.POST['stripemailingstreet'] 
            mailingsuitez = request.POST['stripemailingsuite']
            mailingcityz = request.POST['stripemailingcity'] 
            mailingstatez = request.POST['stripemailingstate']

        # amount input session for campaign module donation is not rounded by decimal point
        amountz = request.session.get('amount_input')

        mainAmount = None

        if amountz:
            #print '---amountz---'
            mainAmount = float(amountz)
        

        if request.session._session:
            
            #print request.session._session

            emailz = request.session.get('email_input')
            zipz = request.session.get('zip_input')
            amountz = request.session.get('amount_input')
            project_sub = request.session.get('projectmain_input')
            project = request.session.get('project')

           
        #check if project monthly Donations
        if project == 'Monthly Donations':

            send_donation_info(emailz, mainAmount, emailz, project, project_sub , zipz, statez, streetz, suitez, cityz, emailz, firstnamez, lastnamez, mailingstatez, mailingstreetz, mailingsuitez, mailingcityz, tshirtz, address='')
                     
            #----- Campaign monitor --------
            auth = {'api_key': settings.CM_KEY }

            # The unique identifier for this smart email
            #smart_email_id = '16aa58f8-f16a-44af-bc8b-b2fef5ac4a7f'

            # Create a new mailer and define your message
            tx_mailer = Transactional(auth)

            donation_amount = mainAmount

            # donor name
            donor_name = firstnamez

            donor_email_cm = emailz

            my_data = {
                'x-apple-data-detectors': 'x-apple-data-detectorsTestValue',
                'href^="tel"': 'href^="tel"TestValue',
                'href^="sms"': 'href^="sms"TestValue',
                'owa': 'owaTestValue',
                'role=section': 'role=sectionTestValue',
                'style*="font-size:1px"': 'style*="font-size:1px"TestValue',
                'donation': donation_amount,
                'firstName': donor_name
            }

            # Add consent to track value
            consent_to_track = 'yes' # Valid: 'yes', 'no', 'unchanged'


            if donation_amount < 34:

                auth = {'api_key': settings.CM_KEY }

                # Create a new mailer and define your message
                tx_mailer = Transactional(auth)

                smart_email_id = '235b79ac-9e4b-42a5-afb0-055837854a90'
                # ---------------------------
                tx_mailer = Transactional(auth)

                donation_amount = mainAmount

                donor_email_cm = emailz

                # donor name
                donor_name = firstnamez

                my_data = {
                    'x-apple-data-detectors': 'x-apple-data-detectorsTestValue',
                    'href^="tel"': 'href^="tel"TestValue',
                    'href^="sms"': 'href^="sms"TestValue',
                    'owa': 'owaTestValue',
                    'role=section': 'role=sectionTestValue',
                    'style*="font-size:1px"': 'style*="font-size:1px"TestValue',
                    'donation': donation_amount,
                    'firstname': donor_name
                }

                consent_to_track = 'yes' # Valid: 'yes', 'no', 'unchanged'

                response = tx_mailer.smart_email_send(smart_email_id, donor_email_cm, consent_to_track, data = my_data)
                # ---------------------------
            elif donation_amount > 34:
                
                auth = {'api_key': settings.CM_KEY }

                # Create a new mailer and define your message
                tx_mailer = Transactional(auth)

                smart_email_id = '334df744-cfd2-4503-bac2-3e58bf2c7845'
                # ---------------------------
                tx_mailer = Transactional(auth)

                donation_amount = mainAmount

                donor_email_cm = emailz

                # donor name
                donor_name = firstnamez

                my_data = {
                    'x-apple-data-detectors': 'x-apple-data-detectorsTestValue',
                    'href^="tel"': 'href^="tel"TestValue',
                    'href^="sms"': 'href^="sms"TestValue',
                    'owa': 'owaTestValue',
                    'role=section': 'role=sectionTestValue',
                    'style*="font-size:1px"': 'style*="font-size:1px"TestValue',
                    'donation': donation_amount,
                    'firstname': donor_name
                }

                consent_to_track = 'yes' # Valid: 'yes', 'no', 'unchanged'

                response = tx_mailer.smart_email_send(smart_email_id, donor_email_cm, consent_to_track, data = my_data)
                # ---------------------------
        else:

            send_donation_info(emailz, mainAmount, emailz, project, project_sub , zipz, statez, streetz, suitez, cityz, emailz, firstnamez, lastnamez, mailingstatez, mailingstreetz, mailingsuitez, mailingcityz, tshirtz, address='')
            
        #send_donation_info(email, donation_cents / 100.0, email, 'Monthly Donations', 'Monthly Donations', postalcode, address='')

    except KeyError:
        logger.exception('stripe_payment called without required POST data')
        return HttpResponseBadRequest('bad POST data')

    print '============================================================================================================================='

    return redirect('email_confirm')

# @login_required
def stripe_payment(request, pk):
    try:
        token = request.POST['stripeToken']
        tip_cents = request.POST['metadata']
        amount_cents = request.POST['amount_cents']
        email = request.POST['stripeEmail']
        zipcode = request.POST['stripeBillingAddressZip']

        request.session['email_input'] = request.POST['stripeEmail']
        request.session['zip_input'] = request.POST['stripeBillingAddressZip']
        
        #request.session['amount_input'] = request.POST['amount_cents']

    except KeyError:
        logger.exception('stripe_payment called without required POST data')
        return HttpResponseBadRequest('bad POST data')

    try:
        tip_cents = int(tip_cents)
        amount_cents = int(amount_cents)
        if not (0 < amount_cents < MAX_PAYMENT_CENTS):
            raise ValueError('amount_cents cannot be negative')
        if not (0 <= tip_cents <= amount_cents):
            raise ValueError('tip_cents cannot be negative or more than project contribution')
    except ValueError:
        logger.exception('stripe_payment called with improper POST data')
        return HttpResponseBadRequest('bad POST data')

    project = get_object_or_404(Project, pk=pk)

    projectz = get_object_or_404(Project, pk=project.subfund_payment)

    project_matching_donors = ProjectMatchingDonors.objects.filter(project=project, amount__gt=0)

    donation_cents = amount_cents

    error_msg = None

    # pass through for sub fundraise on sfdc as main
    projectmain = projectz.title

    request.session['projectmain_input'] = projectmain

    # postal code for Opportunity
    postalcode = zipcode

    # emailz = request.POST['email']
    # Authenticate with your API Key
    auth = {'api_key': settings.CM_KEY }

    # The unique identifier for this smart email
    smart_email_id = 'ec6571f2-8519-4e95-8b97-0c960328be1b'

    # Create a new mailer and define your message
    tx_mailer = Transactional(auth)

    donation_value = donation_cents / 100.00

       
    request.session['amount_input'] = donation_value

    donor_email_cm = request.POST['stripeEmail']

    my_data = {
        'x-apple-data-detectors': 'x-apple-data-detectorsTestValue',
        'href^="tel"': 'href^="tel"TestValue',
        'href^="sms"': 'href^="sms"TestValue',
        'owa': 'owaTestValue',
        'role=section': 'role=sectionTestValue',
        'style*="font-size:1px"': 'style*="font-size:1px"TestValue',
        'donation': donation_value
    }

    # Add consent to track value
    consent_to_track = 'yes' # Valid: 'yes', 'no', 'unchanged'


    # anon and logged in users gets stripe email sends to that email
    # response = tx_mailer.smart_email_send(smart_email_id, 'Ryan Dexter <mark@re-volv.org>', consent_to_track, data = my_datax)

    response = tx_mailer.smart_email_send(smart_email_id, donor_email_cm, consent_to_track, data = my_data)
    # Send the message and save the response
    # response = tx_add.add(list_id, emailz, "Test name", [] , True, consent_to_track)
    # Send the message and save the response

    # -- Add to mailing list --
    list_id = settings.CM_LIST_ID
    emailz = email

    # Create a new mailer and define your message
    tx_add = Subscriber(auth)

    # Add to mailing list
    consent_to_track = 'yes' # Valid: 'yes', 'no', 'unchanged'
    
    response = tx_add.add(list_id, emailz, "", [] , True, consent_to_track)


    try:
        stripe.Charge.create(source=token, description="Donation for " + project.title, currency="usd",
                             amount=amount_cents)
    except stripe.error.CardError as e:
        body = e.json_body
        error_msg = body['error']['message']
    except stripe.error.APIConnectionError as e:
        body = e.json_body
        error_msg = body['error']['message']
    except Exception:
        error_msg = "Payment error. Re-volv has been notified."
        logger.exception(error_msg)
    if error_msg:
        return render(request, "project/project_donate_error.html", {
            "msg": error_msg, "project": project
        })

    if project_matching_donors:
        for donor in project_matching_donors:
            if donor.amount > donation_cents / 100:
                matching_donation = donation_cents / 100
                donor.amount = donor.amount - donation_cents / 100
                donor.save()
            else:
                matching_donation = donor.amount
                donor.amount = 0
                donor.save()

            tip = None

            Payment.objects.create(
                user=donor.matching_donor,
                entrant=donor.matching_donor,
                amount=matching_donation,
                project=project,
                tip=tip,
                payment_type=PaymentType.objects.get_stripe(),
            )
            #send_donation_info(donor.matching_donor.get_full_name(), matching_donation, donor.matching_donor.user.email, project.title, projectmain, postalcode, address='')

    if request.user.is_authenticated():
        user = request.user.revolvuserprofile
    else:
        user_id = User.objects.get(username='Anonymous').pk
        user = RevolvUserProfile.objects.get(user_id=user_id)

    tip = None
    if tip_cents > 0:
        tip = Tip.objects.create(
            amount=tip_cents / 100.0,
            user=user,
        )

    payment = Payment.objects.create(
    user=user,
    entrant=user,
    amount=donation_cents / 100.0,
    project=project,
    tip=tip,
    payment_type=PaymentType.objects.get_stripe(),
    )

    # if request.user.  (is SUBSSF )  , get project object id of original project,
    if project.org_name == 'SUBSF':

        paymentz = Payment.objects.create(
        user=user,
        entrant=user,
        amount=donation_cents / 100.0,
        project=projectz,
        tip=tip,
        payment_type=PaymentType.objects.get_stripe(),
        )


    if request.session.has_key("utm_params"):
        utm_params = request.session.get("utm_params")
        utm_source = utm_params.get("utm_source")
        utm_medium = utm_params.get("utm_medium")
        utm_campaign = utm_params.get("utm_campaign")
        utm_content = utm_params.get("utm_content")
        referral_source_track = ReferralSourceTrack.objects.create(
            source=utm_source,
            medium=utm_medium,
            campaign=utm_campaign,
            content=utm_content,
            payment=payment
        )

    if not request.user.is_authenticated():
        my_ip = load(urlopen('http://jsonip.com'))['ip']

        url = 'http://api.ipstack.com/' + my_ip + '?access_key=' + settings.IP_STACK_ACCESS_KEY

        url_timezone = 'http://ip-api.com/json/' + my_ip

        response = load(urlopen(url))
        response_timezone = load(urlopen(url_timezone))

        try:
            AnonymousUserDonation.objects.create(
                payment=payment,
                email=email,
                ip_address=my_ip,
                city=response['city'],
                region_code=response['region_code'],
                region_name=response['region_name'],
                time_zone=response_timezone['timezone'],
                country_name=response['country_name'],
                zip_code=response['zip']
            )
        except:
            AnonymousUserDonation.objects.create(email=email, payment=payment)
        request.session['payment'] = payment.id
        SITE_URL = settings.SITE_URL
        portfolio_link = SITE_URL + reverse('email_confirm')
        context = {}
        context['project'] = project
        context['amount'] = donation_cents / 100.0
        if tip_cents != 0:
            context['tip_cents'] = tip_cents / 100.0
        else:
            context['tip_cents'] = False
        context['amount_cents'] = amount_cents / 100.0
        context['portfolio_link'] = portfolio_link
        request.session['project'] = project.title
        previous_url = request.META.get('HTTP_REFERER')
        request.session['url'] = previous_url
        context['first_name'] = "RE-volv"
        context['last_name'] = "supporter"
        #send_donation_info(email, donation_cents / 100.0, email, project.title, projectmain, postalcode, address='')
        send_revolv_email(
            'post_donation',
            context, [email]
        )
        response = redirect('postdonation')
        response.set_cookie('last_project', payment.project.title)
        return response
    else:
        SITE_URL = settings.SITE_URL
        portfolio_link = SITE_URL + reverse('email_confirm')
        user = RevolvUserProfile.objects.get(user=request.user)
        context = {}
        context['project'] = project
        context['amount'] = donation_cents / 100.0
        if tip_cents != 0:
            context['tip_cents'] = tip_cents / 100.0
        else:
            context['tip_cents'] = False
        context['amount_cents'] = amount_cents / 100.0
        context['portfolio_link'] = portfolio_link + utils.get_query_string(request.user)
        context['first_name'] = request.user.first_name.title
        context['last_name'] = request.user.last_name.title

        amount = donation_cents / 100.0
        cover_photo = Project.objects.values_list('cover_photo', flat=True).filter(pk=pk)
        cover_photo = list(cover_photo)
        request.session['amount'] = str(amount)
        request.session['project'] = project.title
        previous_url = request.META.get('HTTP_REFERER')
        request.session['url'] = previous_url
        request.session['cover_photo'] = (SITE_URL + '/media/') + ''.join(cover_photo)
        request.session['social'] = "donation"
        #send_donation_info(user.get_full_name(), donation_cents / 100.0, user.user.email, project.title, projectmain, postalcode, address='')
        send_revolv_email(
            'post_donation',
            context, [request.user.email]
        )
        return redirect('postdonation')



# -----------------------------------------------------------------------------------------------

def stripe_operation_donation(request):
    try:
        token = request.POST['stripeToken']
        amount_cents = request.POST.get('donation_amount_cents')
        if not amount_cents:
            amount_cents = request.POST.get('donation_amount_in_cents')
        email = request.POST['stripeEmail']
        zipcode = request.POST['stripeBillingAddressZip']
        check = request.POST.get('check')

        request.session['email_input'] = request.POST['stripeEmail']
        request.session['zip_input'] = request.POST['stripeBillingAddressZip']

        # amount cents in monthly page module rounds it to a decimal point no need to divide to get the decimal point
        request.session['amount_input'] = amount_cents

    except KeyError:
        logger.exception('stripe_operation_donation called without required POST data')
        return HttpResponseBadRequest('bad POST data')

    project = get_object_or_404(Project, title='Operations')

    request.session['project'] = 'Operations'
    request.session['projectmain_input'] = 'Operations'

    postalcode = zipcode

    amount = round(float(amount_cents) * 100)

    if check == None:

        try:
            stripe.Charge.create(source=token, description="Donation for RE-volv operations donation", currency="usd",
                                 amount=int(amount))
        except stripe.error.CardError as e:
            body = e.json_body
            error_msg = body['error']['message']
            return HttpResponseBadRequest('bad POST data')

        except stripe.error.APIConnectionError as e:
            return HttpResponseBadRequest('bad POST data')

        except Exception:
            error_msg = "Payment error. Re-volv has been notified."
            logger.exception(error_msg)
            return HttpResponseBadRequest('bad POST data')

        if amount_cents > 0:
            if request.user.is_authenticated():
                user = RevolvUserProfile.objects.get(user=request.user)
                tip = None
                Payment.objects.create(
                    user=user,
                    entrant=user,
                    amount=amount / 100,
                    project=project,
                    tip=tip,
                    payment_type=PaymentType.objects.get_stripe(),
                )
            else:

                my_ip = load(urlopen('http://jsonip.com'))['ip']

                url = 'http://api.ipstack.com/' + my_ip + '?access_key=' + settings.IP_STACK_ACCESS_KEY

                response = load(urlopen(url))

                AnonymousUserDetail.objects.create(
                    email=email,
                    ip_address=my_ip,
                    amount=amount / 100,
                    city=response['city'],
                    region_code=response['region_code'],
                    region_name=response['region_name'],
                    country_name=response['country_name'],
                    zip_code=response['zip']
                )

                anonymous_user = User.objects.get(username='Anonymous')
                user = RevolvUserProfile.objects.get(user=anonymous_user)
                tip = None
                Payment.objects.create(
                    user=user,
                    entrant=user,
                    amount=amount / 100,
                    project=project,
                    tip=tip,
                    payment_type=PaymentType.objects.get_stripe(),
                )

            #send_donation_info(email,  amount / 100, email, 'Operations', 'Operations', postalcode, address='')

        context = {}
        if not request.user.is_authenticated():
            context['user'] = 'RE-volv Supporter'
        else:
            if not (request.user.first_name and request.user.last_name):
                context['user'] = 'RE-volv Supporter'
            else:
                context['user'] = request.user.first_name.title() + ' ' + request.user.last_name.title()

        context['amount'] = amount / 100.0

        request.session['result_module'] = 'singleModule'
        #----- old re-volv send emailer post donation  ---- 
        send_revolv_email(
            'Post_operations_donation',
            context, [email]
        )
        #----- Campaign monitor --------
        # emailz = request.POST['email']
        # Authenticate with your API Key
        auth = {'api_key': settings.CM_KEY }

        # The unique identifier for this smart email
        smart_email_id = 'ec6571f2-8519-4e95-8b97-0c960328be1b'

        # Create a new mailer and define your message
        tx_mailer = Transactional(auth)

        donation_amount = amount / 100.00

        donor_email_cm = request.POST['stripeEmail']

        my_data = {
            'x-apple-data-detectors': 'x-apple-data-detectorsTestValue',
            'href^="tel"': 'href^="tel"TestValue',
            'href^="sms"': 'href^="sms"TestValue',
            'owa': 'owaTestValue',
            'role=section': 'role=sectionTestValue',
            'style*="font-size:1px"': 'style*="font-size:1px"TestValue',
            'donation': donation_amount
        }

        # Add consent to track value
        consent_to_track = 'yes' # Valid: 'yes', 'no', 'unchanged'


        # anon and logged in users gets stripe email sends to that email

        # Send the message and save the response   
        # on request post data parameters -> transfer  
        # email -> placeholder  get email data - post -> email
        # donations to projects, wb etc for monthly donations function 
        # amount cents  data -> amount cents

        # response = tx_mailer.smart_email_send(smart_email_id, 'Ryan Dexter <mark@re-volv.org>', consent_to_track, data = my_datax)

        # Send the message and save the response
        # response = tx_add.add(list_id, emailz, "Test name", [] , True, consent_to_track)
        response = tx_mailer.smart_email_send(smart_email_id, donor_email_cm, consent_to_track, data = my_data)
 


        return HttpResponse(json.dumps({'status': 'donation_success', 'amount': amount / float(100)}),
                            content_type="application/json")


    else:
        if amount_cents > 0:
            if request.user.is_authenticated():
                user = RevolvUserProfile.objects.get(user=request.user)
                try:
                    stripeDetail = StripeDetails.objects.get(user=user, amount__gt=0.0)
                except StripeDetails.DoesNotExist:
                    stripeDetail = None
                if not stripeDetail:
                    amount = round(float(amount_cents) * 100)
                    try:
                        customer = stripe.Customer.create(
                            email=email,
                            description="Donation for RE-volv Operations",
                            source=token  # obtained with Stripe.js
                        )
                        plan = stripe.Plan.create(
                            amount=int(amount),
                            interval="month",
                            name="Operation Donation " + str(amount_cents),
                            currency="usd",
                            id="operation_donation" + "_" + customer["id"] + "_" + str(amount_cents))

                        subscription = stripe.Subscription.create(
                            customer=customer,
                            plan=plan,
                        )

                        request.session['result_module'] = 'monthlyModule'
                        request.session['project'] = 'Monthly Donations'

                    except stripe.error.CardError as e:
                        body = e.json_body
                        # error_msg = body['error']['message']
                        messages.error(request, 'Payment error')
                        return redirect('home')
                    except stripe.error.APIConnectionError as e:
                        body = e.json_body
                        # error_msg = body['error']['message']
                        messages.error(request, 'Internet connection error. Please check your internet connection.')
                        return redirect('home')
                    except Exception:
                        error_msg = "Payment error. RE-volv has been notified."
                        logger.exception(error_msg)

                        messages.error(request, 'Payment error. RE-volv has been notified.')
                        return redirect('home')

                else:
                    return HttpResponse(json.dumps({'status': 'already_exist'}), content_type="application/json")

            else:

                amount = round(float(amount_cents) * 100)
                try:
                    customer = stripe.Customer.create(
                        email=email,
                        description="Donation for RE-volv Operations",
                        source=token  # obtained with Stripe.js
                    )
                    plan = stripe.Plan.create(
                        amount=int(amount),
                        interval="month",
                        name="Operation Donation " + str(amount_cents),
                        currency="usd",
                        id="operation_donation" + "_" + customer["id"] + "_" + str(amount_cents))

                    subscription = stripe.Subscription.create(
                        customer=customer,
                        plan=plan,
                    )


                    # project name for data pass through SFDC
                    request.session['project'] = 'Monthly Donations'



                except stripe.error.CardError as e:
                    body = e.json_body
                    # error_msg = body['error']['message']
                    messages.error(request, 'Payment error')
                    return redirect('home')
                except stripe.error.APIConnectionError as e:
                    body = e.json_body
                    # error_msg = body['error']['message']
                    messages.error(request, 'Internet connection error. Please check your internet connection.')
                    return redirect('home')
                except Exception:
                    error_msg = "Payment error. RE-volv has been notified."
                    logger.exception(error_msg)

                    messages.error(request, 'Payment error. RE-volv has been notified.')
                    return redirect('home')

                my_ip = load(urlopen('http://jsonip.com'))['ip']

                url = 'http://api.ipstack.com/' + my_ip + '?access_key=' + settings.IP_STACK_ACCESS_KEY

                response = load(urlopen(url))

                AnonymousUserDetail.objects.create(
                    email=email,
                    ip_address=my_ip,
                    amount=amount / 100,
                    city=response['city'],
                    region_code=response['region_code'],
                    region_name=response['region_name'],
                    country_name=response['country_name'],
                    zip_code=response['zip']
                )
                anonymous_user = User.objects.get(username='Anonymous')
                user = RevolvUserProfile.objects.get(user=anonymous_user)

            StripeDetails.objects.create(
                user=user,
                stripe_customer_id=subscription.customer,
                subscription_id=subscription.id,
                plan=subscription.plan.id,
                stripe_email=email,
                amount=amount / float(100)
            )

            context = {}
            if not request.user.is_authenticated():
                context['user'] = 'RE-volv Supporter'
            else:
                if not (request.user.first_name and request.user.last_name):
                    context['user'] = 'RE-volv Supporter'
                else:
                    context['user'] = request.user.first_name.title() + ' ' + request.user.last_name.title()

            context['amount'] = amount / 100.0


            request.session['result_module'] = 'monthlyModule'
            #send_donation_info(email ,  amount / 100, email, 'Monthly Donations', 'Monthly Donations', postalcode, address='')

            send_revolv_email(
                'Post_operations_donation',
                context, [email]
            )

         
            return HttpResponse(json.dumps({'status': 'subscription_success', 'amount': amount / float(100)}),
                                content_type="application/json")


@require_POST
@csrf_exempt
def stripe_webhook(request):
    # Retrieve the request's body and parse it as JSON
    event_json = json.loads(request.body)
    event_id = event_json["id"]
    event_type = event_json["type"]
    data = event_json["data"]
    object = data["object"]
    try:
        if event_type == "invoice.payment_succeeded":
            customer_id = object["customer"]
            subscription_id = object["subscription"]
            lines = object['lines']['data'][0]
            plan_name = lines['plan']['name']
            amount = object['total']
            stripeDetails = StripeDetails.objects.get(stripe_customer_id=customer_id, subscription_id=subscription_id)
            tip = None
            if plan_name.find('Operation') == 0:
                project = get_object_or_404(Project, title='Operations')
                if stripeDetails:
                    user = stripeDetails.user
                    Payment.objects.create(
                        user=user,
                        entrant=user,
                        amount=round(amount / float(100), 2),
                        project=project,
                        tip=tip,
                        payment_type=PaymentType.objects.get_stripe(),
                    )
                    project = get_object_or_404(Project, title='Operations')
                    #send_donation_info(user.get_full_name(), round(amount / float(100), 2), user.user.email, project.title, address='')
            else:
                user = stripeDetails.user
                user.solar_seed_fund_pool = user.solar_seed_fund_pool + amount / 100
                user.save()
    except:
        pass

    return HttpResponse(json.dumps({'status': 'subscription_success', 'amount': amount / float(100)}),
                        content_type="application/json")


class DonationLevelFormSetMixin(object):
    """
    Mixin that gets the ProjectDonationLeveLFormSet for a page, specifically
    the Create Project and Update Project page.
    """

    def get_donation_level_formset(self, extra=2):
        """ Checks if the request is a POST, and populates the formset with current object as the instance
        """
        ProjectDonationLevelFormSet = forms.make_donation_level_formset(extra)

        if self.request.POST:
            return ProjectDonationLevelFormSet(self.request.POST, instance=self.object)
        else:
            return ProjectDonationLevelFormSet(instance=self.object)


class CreateProjectView(DonationLevelFormSetMixin, CreateView):
    """
    The view to create a new project. Redirects to the homepage upon success.

    Accessed through /project/create
    """
    model = Project
    template_name = 'project/edit_project.html'
    form_class = forms.ProjectForm

    def get_success_url(self):
        return reverse('project:view', kwargs={'title': self.object.project_url})

    # validates project, formset of donation levels, and adds categories as well
    def form_valid(self, form):

        formset = self.get_donation_level_formset()
        if formset.is_valid():
            new_project = Project.objects.create_from_form(form, self.request.user.revolvuserprofile)
            new_project.update_categories(form.cleaned_data['categories_select'])
            formset.instance = new_project
            formset.save()
            messages.success(self.request, new_project.title + ' has been created!')
        else:
            return self.render_to_response(self.get_context_data(form=form))

        return super(CreateProjectView, self).form_valid(form)

    # sets context to be the create view, doesn't pass in the id
    def get_context_data(self, **kwargs):
        context = super(CreateProjectView, self).get_context_data(**kwargs)
        context['valid_categories'] = Category.valid_categories
        context['GOOGLEMAPS_API_KEY'] = settings.GOOGLEMAPS_API_KEY
        context['donation_level_formset'] = self.get_donation_level_formset()
        context["active_projects"] = Project.objects.get_active()
        return context


class CreateProjectSubView(DonationLevelFormSetMixin, CreateView):
    """
    The view to create a new project. Redirects to the homepage upon success.

    Accessed through /project/create
    """
    model = Project
    template_name = 'project/edit_project3.html'
    form_class = forms.ProjectSubForm

    def get_success_url(self):

        auth = {'api_key': settings.CM_KEY }

        smart_email_id = '994775e0-b4d4-4bbc-8afc-9bbd6a97cdd8'

        tx_mailer = Transactional(auth)

        my_data = {
            'x-apple-data-detectors': 'x-apple-data-detectorsTestValue',
            'href': 'hrefTestValue',
            'style*="font-size:1px"': 'style*="font-size:1px"TestValue'
        }

        consent_to_track = 'yes' # Valid: 'yes', 'no', 'unchanged'

        response = tx_mailer.smart_email_send(smart_email_id, 'info@re-volv.org', consent_to_track, data = my_data)
        
        return reverse('project:view', kwargs={'title': self.object.project_url})

    # validates project, formset of donation levels, and adds categories as well
    def form_valid(self, form):

        formset = self.get_donation_level_formset()
        if formset.is_valid():
            new_project = Project.objects.create_from_form(form, self.request.user.revolvuserprofile)
            new_project.update_categories(form.cleaned_data['categories_select'])
            formset.instance = new_project
            formset.save()
            messages.success(self.request, new_project.title + ' has been created!')
        else:
            return self.render_to_response(self.get_context_data(form=form))

        return super(CreateProjectSubView, self).form_valid(form)

    # sets context to be the create view, doesn't pass in the id
    def get_context_data(self, **kwargs):
        context = super(CreateProjectSubView, self).get_context_data(**kwargs)
        context['valid_categories'] = Category.valid_categories
        context['GOOGLEMAPS_API_KEY'] = settings.GOOGLEMAPS_API_KEY
        context['donation_level_formset'] = self.get_donation_level_formset()
        context["active_projects"] = Project.objects.get_active()
        return context


class UpdateProjectView(DonationLevelFormSetMixin, UpdateView):
    """
    The view to update a project. It is the same view as creating a new
    project, though it prepopulates the existing field and passes in the
    project id. Redirects to the project page upon success.

    Accessed through /project/{project_id}/edit
    """
    model = Project
    template_name = 'project/edit_project2.html'
    form_class = forms.ProjectForm

    def get_initial(self):
        """
        Initializes the already selected categories for a given project.
        """
        return {'categories_select': self.get_object().categories}

    def get_success_url(self):
        messages.success(self.request, 'Project details updated')
        return reverse('project:view', kwargs={'title': self.get_object().project_url})

    def form_valid(self, form):
        """
        Validates project, formset of donation levels, and adds categories as well
        """
        formset = self.get_donation_level_formset()

        if formset.is_valid():
            project = self.get_object()
            project.update_categories(form.cleaned_data['categories_select'])
            formset.instance = project
            formset.save()
        else:
            return self.render_to_response(self.get_context_data(form=form))
        return super(UpdateProjectView, self).form_valid(form)

    # sets context to be the edit view by providing in the model id
    def get_context_data(self, **kwargs):
        context = super(UpdateProjectView, self).get_context_data(**kwargs)
        context['valid_categories'] = Category.valid_categories
        context['donation_level_formset'] = self.get_donation_level_formset()
        return context

class UpdateProjectSubView(DonationLevelFormSetMixin, UpdateView):
    """
    The view to update a project. It is the same view as creating a new
    project, though it prepopulates the existing field and passes in the
    project id. Redirects to the project page upon success.

    Accessed through /project/{project_id}/edit
    """
    model = Project
    template_name = 'project/edit_project4.html'
    form_class = forms.ProjectSubForm

    def get_initial(self):
        """
        Initializes the already selected categories for a given project.
        """
        return {'categories_select': self.get_object().categories}

    def get_success_url(self):
        messages.success(self.request, 'Project details updated')
        return reverse('project:view', kwargs={'title': self.get_object().project_url})

    def form_valid(self, form):
        """
        Validates project, formset of donation levels, and adds categories as well
        """
        formset = self.get_donation_level_formset()

        if formset.is_valid():
            project = self.get_object()
            project.update_categories(form.cleaned_data['categories_select'])
            formset.instance = project
            formset.save()
        else:
            return self.render_to_response(self.get_context_data(form=form))
        return super(UpdateProjectSubView, self).form_valid(form)

    # sets context to be the edit view by providing in the model id
    def get_context_data(self, **kwargs):
        context = super(UpdateProjectSubView, self).get_context_data(**kwargs)
        context['valid_categories'] = Category.valid_categories
        context['donation_level_formset'] = self.get_donation_level_formset()
        return context

class ReviewProjectView(UserDataMixin, UpdateView):
    """
    The view to review a project. Shows the same view as ProjectView, but at
    the top, has a button group through which an ambassador or admin can
    update the project status.

    Accessed through /project/{project_id}/review
    """
    model = Project
    form_class = forms.ProjectStatusForm
    http_method_names = [u'post']

    def get_success_url(self):
        if self.is_administrator:
            return "%s?active_project=%d" % (reverse('administrator:dashboard'), self.get_object().id)
        else:
            return reverse('project:view', kwargs={'title': self.get_object().project_url})

    # Checks the post request and updates the project_status
    def form_valid(self, form):
        project = self.object
        if '_approve' in self.request.POST:
            messages.success(self.request, project.title + ' has been approved and is live.')
            project.approve_project()
        elif '_stage' in self.request.POST:
            messages.success(self.request, project.title + ' has been staged to go live.')
            project.stage_project()
        elif '_unapprove' in self.request.POST:
            messages.success(self.request, project.title + ' is no longer live.')
            project.unapprove_project()
        elif '_propose' in self.request.POST:
            messages.success(self.request, project.title + ' is now pending approval.')
            project.propose_project()
        elif '_deny' in self.request.POST:
            messages.info(self.request, project.title + ' has been denied.')
            project.deny_project()
        elif '_complete' in self.request.POST:
            messages.success(self.request, project.title + ' has been completed.')
            project.complete_project()
        elif '_incomplete' in self.request.POST:
            messages.info(self.request, project.title + ' has been marked as active again (not yet completed).')
            project.mark_as_incomplete_project()
        elif '_repayment' in self.request.POST:
            repayment_amount = Decimal(self.request.POST['_repayment_amount'])
            PaymentService.create_repayment(self.user_profile, repayment_amount, project)
            messages.success(self.request, '$' + str(repayment_amount) + ' repaid by ' + project.org_name)
        return redirect(self.get_success_url())

    # pass in Project Categories and Maps API key
    def get_context_data(self, **kwargs):
        context = super(ReviewProjectView, self).get_context_data(**kwargs)
        context['GOOGLEMAPS_API_KEY'] = settings.GOOGLEMAPS_API_KEY
        return context


class TemplateProjectUpdateView(UserDataMixin, UpdateView):
    form_class = forms.EditProjectUpdateForm
    template_name = 'project/edit_project_update.html'

    def dispatch(self, request, *args, **kwargs):
        response = super(TemplateProjectUpdateView, self).dispatch(request, args, kwargs)
        if not self.is_ambassador:
            return self.deny_access()
        return response


class PostProjectUpdateView(TemplateProjectUpdateView):
    model = Project

    def get_success_url(self):
        return reverse('project:view', kwargs={'title': self.get_object().project_url})

    def form_valid(self, form):
        text = form.cleaned_data['update_text']
        project = self.get_object()
        project.add_update(text)
        return super(PostProjectUpdateView, self).form_valid(form)


class EditProjectUpdateView(TemplateProjectUpdateView):
    model = ProjectUpdate

    def get_success_url(self):
        return reverse('project:view', kwargs={'title': self.get_object().project_url})

    def form_valid(self, form):
        text = form.cleaned_data['update_text']
        update = self.get_object()
        update.update_text = text
        return super(EditProjectUpdateView, self).form_valid(form)


class ProjectReinvestView(UserDataMixin, DetailView):
    """
    The project view. Displays project details and allows for editing.

    Accessed through /project/{project_id}
    """
    model = Project
    template_name = 'project/project.html'

    # pass in Project Categories and Maps API key
    def get_context_data(self, **kwargs):
        context = super(ProjectReinvestView, self).get_context_data(**kwargs)
        context['stripe_publishable_key'] = settings.STRIPE_PUBLISHABLE
        context['GOOGLEMAPS_API_KEY'] = settings.GOOGLEMAPS_API_KEY
        context['updates'] = self.get_object().updates.order_by('date').reverse()
        context['donor_count'] = self.get_object().total_donors()
        context['project_donation_levels'] = self.get_object().donation_levels.order_by('amount')
        context["is_draft_mode"] = self.get_object().project_status == self.get_object().DRAFTED
        context['payments'] = Payment.objects.all()
        if self.user_profile:
            amount = self.user_profile.reinvest_pool + self.user_profile.solar_seed_fund_pool
        if self.user_profile and amount > 0.0:
            context["reinvestment_amount"] = self.user_profile.reinvest_pool + self.user_profile.solar_seed_fund_pool
            context["is_reinvestment"] = True
            # context["reinvestment_amount"] = self.user_profile.reinvest_pool
        return context


class ProjectView(UserDataMixin, DetailView):
    """
    The project view. Displays project details and allows for editing.

    Accessed through /project/{project_id}
    """
    # model = Project
    template_name = 'project/project2.html'

    def get_object(self):
        if self.kwargs['title'].isnumeric():
            object = get_object_or_404(Project, id=self.kwargs['title'])
        else:
            object = get_object_or_404(Project, project_url=self.kwargs['title'])
        return object

    # pass in Project Categories and Maps API key
    def get_context_data(self, **kwargs):


        subfund = self.get_object().subfund_payment
        profile_main = get_object_or_404(Project, pk=int(subfund))
        
        context = super(ProjectView, self).get_context_data(**kwargs)
        context['stripe_publishable_key'] = settings.STRIPE_PUBLISHABLE

        context['sub_main'] = subfund 
     

        context['profile_main'] = profile_main.title
        context['cover_main'] = profile_main.cover_photo

        context['GOOGLEMAPS_API_KEY'] = settings.GOOGLEMAPS_API_KEY
        context['updates'] = self.get_object().updates.order_by('date').reverse()
        context['donor_count'] = self.get_object().total_donors()
        context['project_donation_levels'] = self.get_object().donation_levels.order_by('amount')
        context['project_matching_donor'] = ProjectMatchingDonors.objects.filter(project=self.get_object(),
                                                                                 amount__gt=0)
        context["is_draft_mode"] = self.get_object().project_status == self.get_object().DRAFTED
        context["is_reinvestment"] = False
        if self.user_profile:
            amount = self.user_profile.reinvest_pool + self.user_profile.solar_seed_fund_pool
        if self.user_profile and amount > 0.0:
            context["reinvestment_amount"] = self.user_profile.reinvest_pool + self.user_profile.solar_seed_fund_pool
        else:
            context["reinvestment_amount"] = 0.0
        context["reinvestment_url"] = ''
        return context

    def dispatch(self, request, *args, **kwargs):
        # always populate self.user, etc
        super_response = super(ProjectView, self).dispatch(request, *args, **kwargs)
        project = self.get_object()
        if (project.is_active or project.is_completed or project.is_staged or
                (self.user.is_authenticated() and (
                        project.has_owner(self.user_profile) or self.is_administrator or self.is_ambassador))):
            return super_response
        else:
            return self.deny_access()


class SubmitDonationView(UserDataMixin, FormView):
    form_class = CreditCardDonationForm
    model = Project
    http_method_names = [u'post']

    def form_valid(self, form):
        project = Project.objects.get(pk=self.kwargs.get('pk'))
        form.process_payment(project, self.user)
        context = {}
        context['user'] = self.user
        context['project'] = project
        context['amount'] = form.cleaned_data.get('amount')

        send_revolv_email(
            'post_donation',
            context, [self.user.email]
        )
        try:
            amount = form.cleaned_data.get('amount')
            # send_donation_info.delay(self.user_profile.get_full_name(), float(amount),
            #                         project.title, self.user_profile.address)
        except:
            pass

        return JsonResponse({
            'amount': form.data['amount'],
        })

    def form_invalid(self, form):
        return JsonResponse({
            'error': form.errors,
        }, status=400)


class ProjectListReinvestmentView(UserDataMixin, TemplateView):
    """
    View List Project that are eligible to receive reinvestment funds.
    """
    template_name = 'base/projects-list.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectListReinvestmentView, self).get_context_data(**kwargs)
        context["is_reinvestment"] = True
        if not is_user_reinvestment_period():
            if self.user_profile.reinvest_pool > 0.0:
                context["error_msg"] = "You have ${0} to reinvest, " \
                                       "but the reinvestment period has ended for this month. " \
                                       "Please come back next month!" \
                    .format(self.user_profile.reinvest_pool)
            else:
                context["error_msg"] = "The reinvestment period has ended for this month. " \
                                       "Please come back next month!"
        else:
            active = Project.objects.get_eligible_projects_for_reinvestment()
            context["active_projects"] = filter(lambda p: p.amount_left > 0.0, active)
            if self.user_profile.reinvest_pool > 0.0:
                context["reinvestment_amount"] = self.user_profile.reinvest_pool
            else:
                context["error_msg"] = "You don't have funds to reinvest."
        return context


@login_required
@require_http_methods(['POST'])
def reinvest(request, pk):
    """View handle reinvestment action
    """
    amount = request.POST.get('amount')
    if not amount:
        return HttpResponseBadRequest()
    try:
        project = Project.objects.get(pk=pk)
    except (Project.DoesNotExist, Project.MultipleObjectsReturned):
        return HttpResponseBadRequest()

    available_amount = RevolvUserProfile.objects.get(user=request.user).reinvest_pool + RevolvUserProfile.objects.get(
        user=request.user).solar_seed_fund_pool
    if float(amount) > 0 and (float(format(round(available_amount,2))) - float(amount)) >= 0:
        UserReinvestment.objects.create(user=request.user.revolvuserprofile,
                                        amount=amount,
                                        project=project)
        messages.success(request, 'Reinvestment Successful')
        return redirect("project:view", title=project.project_url)
    elif float(amount) > available_amount > 0:
        return HttpResponse("error", status=308)
    else:
        return HttpResponse("error", status=404)
