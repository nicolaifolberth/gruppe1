package Core;

import Core.Clients.ConsoleClientLocal;

class ClientMainConsole {

    public static void main(String[] args) {
        ConsoleClientLocal consoleClientLocal = new ConsoleClientLocal();
        consoleClientLocal.start();
    }
}
