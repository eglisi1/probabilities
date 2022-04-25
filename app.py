from flask import Flask, render_template, request

from dto.birthday.birthday_dto import BirthdayDto
from dto.roulette.roulette_dto import RouletteDto
from service.birthday.birthday_service import calculate_probability
from service.roulette.roulette_service import RouletteService

app = Flask(__name__)
# Load Configurations
app.config.from_object('config_flask')


@app.route('/')
def home() -> str:
    return render_template(template_name_or_list='index.html')


@app.route('/roulette')
def roulette() -> str:
    return render_template(template_name_or_list='roulette/roulette.html')


@app.route('/roulette/result', methods=['POST'])
def calculate_roulette() -> str:
    budget = int(request.form['budget'])
    bet = int(request.form['bet'])
    service = RouletteService(budget=budget, bet=bet)
    amount_rounds = service.play()
    roulette_dto = RouletteDto(budget=budget, bet=bet, amount_rounds=amount_rounds)
    return render_template(template_name_or_list='roulette/roulette_result.html', dto=roulette_dto)


@app.route('/birthday')
def birthday() -> str:
    return render_template(template_name_or_list='birthday/birthday.html')


@app.route('/birthday/result', methods=['POST'])
def calculate_birthday() -> str:
    amount_people = int(request.form['amount_people'])
    probability = calculate_probability(amount_people=amount_people)
    birthday_dto = BirthdayDto(amount_people=amount_people, probability=probability)
    return render_template(template_name_or_list='birthday/birthday_result.html', dto=birthday_dto)


if __name__ == '__main__':
    app.run()
