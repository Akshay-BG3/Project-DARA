import base64
from io import BytesIO
import matplotlib.pyplot as plt

def fig_to_base64(fig):
    buf = BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.close(fig)  # Close the figure after saving to buffer
    return image_base64
