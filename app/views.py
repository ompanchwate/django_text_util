from pickle import TRUE
from django.http import HttpResponse
from django.shortcuts import render
import string

# Create your views here.


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # Get the Text
    djtext = request.GET.get('text')

    # Get the Checkbox values
    removepunc = request.GET.get('removepunc', 'off')
    capitalize = request.GET.get('capitalize', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    spaceremover = request.GET.get('spaceremover', 'off')
    countchar = request.GET.get('countchar', 'off')

    # Initializing analyzed variable with empty text
    analyzed = ""

    # If djtext is not empty then
    if djtext != "":
        # If removepunc checkbox is ON then
        if removepunc == "on":
            # Check that the letters in the given text matches with the punctuations or not
            for char in djtext:
                # If char is not in string.punctuation then add the character with the analyzed
                if char not in string.punctuation:
                    analyzed = analyzed + char

            # send the data to the template
            params = {'purpose': 'remove punctuation',
                      'analyzed_text': analyzed}
            # Gives proper output when other checkbox are also on
            djtext = analyzed  # So that other conditions get the text with no punctuation

        # If capitalize text checkbox in ON then
        if (capitalize == 'on'):
            # Transform the text to uppercase
            analyzed = djtext.upper()
            # send the data to the template
            params = {'purpose': 'Capitalize the text',
                      'analyzed_text': analyzed}
            djtext = analyzed

        # If newlineremover checkbox in ON
        if newlineremover == 'on':
            analyzed = ""
            # Removes the new line Character
            # for char in djtext:
            #     if char != '\n' and char != '\r':
            #         analyzed = analyzed + char
            #     else:
            #         print("no")
            analyzed = djtext.replace("\n", "")
            analyzed = analyzed.replace("\r", "")
            # send the data to the template
            params = {'purpose': 'New line remover',
                      'analyzed_text': analyzed}
            djtext = analyzed

        # If remove spaceremover checkbox in ON
        if spaceremover == 'on':
            # Removes the spaces
            # split(no_argument) : breaks the string at whitespaces
            # " ".join() : add the whitespace
            analyzed = " ".join(djtext.split())
            # send the data to the template
            params = {'purpose': 'Remove unwanted spaces',
                      'analyzed_text': analyzed}
            djtext = analyzed

        if countchar == "on":
            count = 0
            for char in djtext:
                if char != " ":
                    count = count + 1
            analyzed = djtext + "\n\nCharacter Count = " + str(count)
            # send the data to the template
            params = {'purpose': 'Count Characters',
                      'analyzed_text': analyzed}
            djtext = analyzed

    # If djtext is empty then
    else:
        error = "No input given"
        params = {'purpose': 'Error : No text given',
                  'analyzed_text': analyzed}

    return render(request, 'analyze.html', params)
