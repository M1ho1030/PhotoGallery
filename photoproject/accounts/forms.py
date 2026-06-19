# userCreationFormクラスをインポート
from django.contrib.auth.forms import UserCreationForm
# models.pyで定義したカスタムUserモデルをインポート
from .models import customUser

class customUserCreationForm(UserCreationForm):
    '''UserCreationFormsのサブクラス
    '''

    class Meta:
        '''UserCreationFormsのインナークラス
        Attributes:
            model:連携するUserモデル
            fields:フォームで使用するフィールド
        '''

        # 連携するUserモデルを設定
        model = customUser
        # フォームで使用するフィールドを設定
        # ユーザー名、メールアドレス、パスワード、パスワード（確認用）
        fields = ('username', 'email', 'password1', 'password2')

    