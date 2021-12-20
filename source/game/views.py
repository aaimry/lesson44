from django.shortcuts import render

# Create your views here.

game_score = []


def index_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':

        context = {
            'numbers': request.POST.get('numbers').split(),
            'secret_numbers': ['1', '2', '3', '4'],
            'bulls': 0,
            'cows': 0,
            'result': None
        }
        if context['numbers'] != 4:
            context['result'] = 'The amount of integers should equal to 4!'
        elif len(context['numbers']) > len(set(context['numbers'])):
            context['result'] = 'The values should be unique!'
            game_score.append(context['result'])
        for i in map(int, (context['numbers'])):
            if i > 9 or i < 1:
                context['result'] = 'Numbers must be greater than 1 and less than 10!'
                game_score.append(context['result'])

        for i in range(len(context['secret_numbers'])):
            if context['secret_numbers'][i] == context['numbers'][i]:
                context['bulls'] += 1
            elif context['secret_numbers'][i] in context['numbers']:
                context['cows'] += 1
        if context['bulls'] == 4:
            context['result'] = 'You Win!'
            game_score.append(context['result'])
        elif context['bulls'] or context['cows']:
            context['result'] = f"You got {context['bulls']} bulls and {context['cows']} cows!"
            game_score.append(context['result'])
        else:
            context['result'] = ' You got no identical numbers!'
            game_score.append(context['result'])
        return render(request, 'index.html', context)


def score_view(request):
    context = {
        'score': game_score,
        'step': 1
    }
    if request.method == 'POST':
        context['step'] += 1
        for i in context['score']:
            return i
    return render(request, 'score.html', context)