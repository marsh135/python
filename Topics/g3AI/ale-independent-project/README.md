# Teach an Atari Game to an AI

Use our Breakout code to train an AI to play a different Atari game.

Your goal: **I can run your `watch.py` file and see your saved AI play.**

## 1. Get started

- Make your own copy of this repository and open it in PyCharm.
- Use the same Python setup we used for Breakout.
- In the PyCharm terminal, run:

```sh
python -m pip install -r requirements.txt
```

## 2. Train your AI

- Choose a game other than Breakout from the [game list](https://ale.farama.org/environments/).
- Complete the TODOs in `train.py`. Use our class code to help.
- Start with a short run to check that it works.
- Then increase `TOTAL_TIMESTEPS` and let your AI train. Your teacher will tell you how long to train.
- Find the saved `.zip` model in the folder printed by your program.

## 3. Watch it play

- Complete the TODOs in `watch.py` using the same game as your training code.
- Copy your final saved model into `models/` and name the copy `my_model.zip`.
- Run `watch.py`. A game window should open and your saved AI should play.
- Test this before submitting. Leave the model zipped.

## 4. Turn it in

Submit:

- Your completed `train.py` and `watch.py`.
- Your saved model: `models/my_model.zip`.
- Your short answers in `REPORT.md`.
- Any other files your code needs to run.

Push your code to GitHub. Upload `my_model.zip` with your assignment submission, since model files are left out of GitHub. Keep the name `my_model.zip` so your teacher can place it in `models/` and run `watch.py`.

**Your AI does not need to win. It does need to train, save, and play from the saved model.**
