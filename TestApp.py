import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.network.urlrequest import UrlRequest





class FirstApp(App) :
    def build(self) :
        def success(req, result) :
            print("done")

        def fail(req, result) :
            print("failed")

        req = UrlRequest("https://www.guya.moe/read/manga/Kaguya-Wants-To-Baae-Confessed-To/258/1/", on_success=success, on_failure=fail)

if __name__ == "__main__" :
    FirstApp().run()
