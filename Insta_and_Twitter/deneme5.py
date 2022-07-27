# import ttkbootstrap as ttk
# from ttkbootstrap.constants import *
# root = ttk.Window()
# ttk.Label(root,text=" label 1",bootstyle=INFO).pack(side=ttk.LEFT, padx=5, pady=10)
# ttk.Label(root,text=" label 2",bootstyle="inverse").pack(side=ttk.LEFT, padx=5, pady=10)
# ttk.Label(root,text=" label 3",bootstyle="inverse-danger").pack(side=ttk.LEFT, padx=5, pady=10)
# ttk.Label(root, text=" label 4", bootstyle=WARNING, font=(" Microsoft YaHei ", 15), background='#94a2a4').pack(side=LEFT, padx=5, pady=10)
# root.mainloop()

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
root = ttk.Window()
ttk.Button(root, text="Button 1", bootstyle=SUCCESS).pack(side=LEFT, padx=5, pady=10)
ttk.Button(root, text="Button 2", bootstyle=(INFO, OUTLINE)).pack(side=LEFT, padx=5, pady=10)
ttk.Button(root, text="Button 3", bootstyle=(PRIMARY, "outline-toolbutton")).pack(side=LEFT, padx=5, pady=10)
ttk.Button(root, text="Button 4", bootstyle="link").pack(side=LEFT, padx=5, pady=10)
ttk.Button(root, text="Button 5", bootstyle="success-link").pack(side=LEFT, padx=5, pady=10)
ttk.Button(root, text="Button 6", state="disabled").pack(side=LEFT, padx=5, pady=10) # Create button in disabled state root.mainloop()
root.mainloop()