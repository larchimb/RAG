try:
    from .main import main
    main()
except KeyboardInterrupt:
    print("[ERROR]: Keyboard interruption from the user")
except Exception as e:
    print(e)
