#!/usr/bin/env python3
import socket
import random
import dados_print
import time
import subprocess as sp
import threading as t

HOST = '127.0.0.1'
PORT = 5000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

def dice_roll():
    diceRoll = random.randint(1, 6)
    return diceRoll


def main():
    while True:
        empates = 0
        player1 = 0
        player1wins = 0
        player2 = 0
        player2wins = 0
        rounds = 1
        print("Juego de dados aleatorios. Quien obtenga un dado mayor gana la ronda. El mejor de 10 rondas es el ganador final.")
        time.sleep(3)
        while rounds != 10:
            sp.call('cls', shell=True)
            print("_______________\nRonda número: " + str(rounds) + " Puntaje: [J1]{} - {}[J2]\n".format(player1wins,player2wins))
            time.sleep(2)
            player1 = dice_roll()
            s.sendall(bytes("El jugador 1 saco: {} en la ronda {}".format(player1,rounds),"utf-8"))
            player2 = dice_roll()
            s.sendall(bytes("El jugador 2 saco: {} en la ronda {}".format(player2,rounds), "utf-8"))
            print("Jugador 1 tiró: ")
            time.sleep(2)
            dados_print.dado_print(int(player1))
            time.sleep(2)
            print("\nJugador 2 tiró: ")
            time.sleep(2)
            dados_print.dado_print(int(player2))
            time.sleep(2)

            if player1 == player2:
                print("Empate!\n")
                empates += 1
            elif player1 > player2:
                player1wins = player1wins + 1
                print("Jugador 1 gana!\n")
                time.sleep(2)
            else:
                player2wins = player2wins + 1
                print("Jugador 2 gana!\n")
                time.sleep(2)

            rounds = rounds + 1

        if player1wins == player2wins:
            print("Empate!")
            time.sleep(2)
        elif player1wins > player2wins:
            print("¡Jugador 1 ganador final!\nPuntaje: [J1]{} - {}[J2]\nEmpates: {}".format(player1wins,player2wins,empates))
            s.close()
            break
        else:
            print("¡Jugador 2 ganador final!\nPuntaje: [J1]{} - {}[J2]\nEmpates: {}".format(player1wins,player2wins,empates))
            s.close()
            break
 
main()