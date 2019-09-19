while True:
    try:
        a = int(input('Enter a number: '))
        print('No exception raised, here is your number back: {}\n'.format(a))
        break

    except ValueError:
        print('Incorrect Value Input Error.\n')

    except KeyboardInterrupt:
        print('Keyboard interupted, program is now exiting...\n')
        break

    finally:
        print('Input was taken.\n')