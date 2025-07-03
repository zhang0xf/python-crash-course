# 由于Pygame没有内置创建按钮的方法，我们创建一个Button类，用于创建带标签的实心矩形
# 你可以在游戏中使用这些代码来创建任何按钮
import pygame.font

class Button():
    def __init__(self,ai_settings,screen,msg):
        """初始化按钮的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # 设置按钮的尺寸和其他属性
        self.width,self.height = 200,50
        self.button_color = (0,255,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48) # 参None让Pygame使用默认字体，而48指定了文本的字号
        # 创建按钮的rect对象，并使其居中
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center
        # 按钮的标签只需创建一次
        self.prep_msg(msg)

    # Pygame通过将你要显示的字符串渲染为图像来处理文本
    def prep_msg(self,msg):
        """将msg渲染为图像,并使其在按钮上居中"""
        # True:开启抗锯齿功能
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
        # 让文本图像在按钮上居中
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # 绘制一个用颜色填充的按钮，再绘制文本
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)