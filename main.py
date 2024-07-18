from app import App
import config as c


def main():
    app = App(c.SCREEN_WIDTH, c.SCREEN_HEIGHT, c.CAPTION, c.FPS)
    app.run()


if __name__ == "__main__":
    main()
